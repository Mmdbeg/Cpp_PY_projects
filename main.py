import numpy as np
import pandas as pd


#  showing all table 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# loading datas 
data = pd.read_csv('data.csv')
data_GCP = pd.read_csv('gcp.csv')

#  adding point type col to the data table (0,1,2,3) 
data.insert(loc=5, column='POINT.TYPE', value=0)

#  giving each point its code based on its type
for i in range(len(data)):
    for j in range(len(data_GCP)):
        if data.iloc[i, 2] == data_GCP.iloc[j, 0]:
            if pd.isnull(data_GCP.iloc[j, 3]):
                data.iloc[i, 5] = 2
            elif pd.isnull(data_GCP.iloc[j, 1]) and pd.isnull(data_GCP.iloc[j, 2]):
                data.iloc[i, 5] = 3
            else:
                data.iloc[i, 5] = 1

# Numbring Tie points .................................................................................................................

# Adding columns for numbring points ................................................................................................
data.insert(loc=6, column='num_Tie', value=0)
data.insert(loc=7, column='num_full_ctrl', value=0)
data.insert(loc=8, column='num_plan_ctrl', value=0)
data.insert(loc=9, column='num_alt_ctrl', value=0)
data.insert(loc=10, column='num_tie_alt', value=0)

# Numbring Tie points .................................................................................................................
temp_tie_code = []    
count_tie = 1
for i in range(len(data)):
    a, b = data.loc[i, ["code", "POINT.TYPE"]]
    if b == 0:
        temp_tie_code.append(a)
        if temp_tie_code.count(a) >= 2:
            data.loc[i, "num_Tie"] = data.loc[data.index[data["code"] == a][0], "num_Tie"]
            continue
        else:
            data.loc[i, "num_Tie"] = count_tie
            count_tie += 1

# Numbring Full control points ......................................................................................
temp_full_ctrl_code = []    
count_full = 1
for i in range(len(data)):
    a, b = data.loc[i, ["code", "POINT.TYPE"]]
    if b == 1:
        temp_full_ctrl_code.append(a)
        if temp_full_ctrl_code.count(a) >= 2:
            data.loc[i, "num_full_ctrl"] = data.loc[data.index[data["code"] == a][0], "num_full_ctrl"]
            continue
        else:
            data.loc[i, "num_full_ctrl"] = count_full
            count_full += 1

# Numbring planer control points ......................................................................................
temp_plan_ctrl_code = []    
count_plan = 1
for i in range(len(data)):
    a, b = data.loc[i, ["code", "POINT.TYPE"]]
    if b == 2:
        temp_plan_ctrl_code.append(a)
        if temp_plan_ctrl_code.count(a) >= 2:
            data.loc[i, "num_plan_ctrl"] = data.loc[data.index[data["code"] == a][0], "num_plan_ctrl"]
            continue
        else:
            data.loc[i, "num_plan_ctrl"] = count_plan
            count_plan += 1

# Numbring Altitude control points ......................................................................................
temp_alt_ctrl_code = []    
count_alt = 1
for i in range(len(data)):
    a, b = data.loc[i, ["code", "POINT.TYPE"]]
    if b == 3:
        temp_alt_ctrl_code.append(a)
        if temp_alt_ctrl_code.count(a) >= 2:
            data.loc[i, "num_alt_ctrl"] = data.loc[data.index[data["code"] == a][0], "num_alt_ctrl"]
            continue
        else:
            data.loc[i, "num_alt_ctrl"] = count_alt
            count_alt += 1
# Numbring Tie points + Altitude ....................................................................................
temp_tie_alt_code = []    
count_tie_alt = 1
for i in range(len(data)):
    a, b = data.loc[i, ["code", "POINT.TYPE"]]
    if b == 0 or b==3:
        temp_tie_alt_code.append(a)
        if temp_tie_alt_code.count(a) >= 2:
            data.loc[i, "num_tie_alt"] = data.loc[data.index[data["code"] == a][0], "num_tie_alt"]
            continue
        else:
            data.loc[i, "num_tie_alt"] = count_tie_alt
            count_tie_alt += 1


# removing duplicate datas & selecting tie ppints 
code_df = data[data["POINT.TYPE"]==0]['code'].drop_duplicates()
code_list = list(code_df)

# Create a new DataFrame 'new_data' with zeros
new_data = pd.DataFrame(0, index=range(14), columns=code_df)
new_data.insert(0, 'Ran', 0)
new_data.insert(1, 'Pic', 0)
new_data.loc[0:7, 'Ran'] = 1
new_data.loc[7:, 'Ran'] = 2

for i in range(7):
    new_data.loc[i, 'Pic'] = i+1  
    new_data.loc[i+7, 'Pic'] = i+1 

for i in range(len(new_data)): 
    for j in range(2, len(code_list)+2): 
        a =code_list[j-2]
        for k in range(len(data)):  
            if new_data.loc[i, 'Ran'] == data.loc[k, 'ran'] and new_data.loc[i, 'Pic'] == data.loc[k, 'photo']: 
                if a == data.loc[k, 'code']:  
                    new_data.iloc[i,j] = 1 
                     
# creating coefficient matrix  and calculating appriximates values by comformal model //////////////////////////

# -----------------------------------------------------------------------------------------

number_photo = 14
Au = np.zeros((2*len(data), number_photo*4))

# CREATING AG MATRIX ----------------------------------------------------------------------------
for k in range(len(data)):
    if data.loc[k, "ran"] == 1:
        j = data.loc[k, "photo"] 
    elif data.loc[k, "ran"] == 2:
        j = data.loc[k, "photo"] + 7
    Au[2*k, (4*j-3)-1] = data.loc[k, "x"]
    Au[2*k, (4*j-2)-1] = -data.loc[k, "y"]
    Au[2*k, (4*j-1)-1] = 1
    Au[2*k, (4*j)-1]   = 0
    Au[2*k+1, (4*j-3)-1] = data.loc[k, "y"]
    Au[2*k+1, (4*j-2)-1] = data.loc[k, "x"]
    Au[2*k+1, (4*j-1)-1] = 0
    Au[2*k+1, (4*j)-1]   = 1


Ag = np.zeros((2*len(data), max(data["num_tie_alt"])*2))

# CREATING AE MATRIX ----------------------------------------------------------------------------

for k in range(len(data)):
    i = data.loc[k, "num_tie_alt"]
    if i != 0:
        Ag[2*k, (2*i-1)-1] = -1
        Ag[2*k+1, (2*i)-1] = -1


A = np.concatenate((Au, Ag), axis=1)
#print(A.shape)

# CREATING OBSERVATION MATRIX 
obs = np.zeros(((len(data)*2),1))

for point_conter in range(len(data)):
    for i in range(len(data_GCP)):
        if (data.loc[point_conter,'POINT.TYPE'] == 1 or data.loc[point_conter,'POINT.TYPE'] == 2) and data.loc[point_conter,'code'] == data_GCP.loc[i,'code'] :
            obs[2*point_conter]   = data_GCP.loc[i,'X']
            obs[2*point_conter+1] = data_GCP.loc[i,'Y']

# USING LEAST SQUARE METHODE TO CALCULATE UNKNOWNS
u_p = (np.linalg.inv(A.T@A))@A.T@obs

#print(u_p.shape)


# CACULATING LANDA
landa = np.zeros((14,1))
c = 0
for i in range(14):
    landa[i] = np.sqrt(u_p[c]**2+u_p[c+1]**2)
    c = c+4 
#print(landa.shape)

# CALULATING K 
k = np.zeros((14,1))
c = 0
p = np.pi 
for i in range(14):

                       #b dx     #a dy
    k0 = np.arctan(u_p[c+1]/u_p[c])
    if u_p[c+1] > 0 and u_p[c] > 0 : 
        k[i] = k0*180/p 
    if u_p[c+1] > 0 and u_p[c] < 0 : 
        k[i] =180 - k0*180/p 
    if u_p[c+1] < 0 and u_p[c] < 0 :
        k[i] = k0*180/p + 180
    if u_p[c+1] < 0 and u_p[c] > 0 :
        k[i] =360 - k0*180/p 
    c = c+4    
#print(k)

# CALCULATING X0 Y0 
X0 = np.zeros((14,1))
Y0 = np.zeros((14,1))
c = 0
for i in range(14):
    X0[i] = u_p[c+2]
    Y0[i] = u_p[c+3]
    c = c+4 
















