import numpy as np
import pandas as pd

# CREATING ORIANTATION MATRIX (THIS WILL BE USE IN THE INTERSECTION CASE)
def rotation_matrix_kapa(kapa):
    return np.array([
        [np.cos(kapa), np.sin(kapa), 0],
        [-np.sin(kapa), np.cos(kapa), 0],
        [0, 0, 1]
    ])

def rotation_matrix_phi(phi):
    return np.array([
        [np.cos(phi), 0, -np.sin(phi)],
        [0, 1, 0],
        [np.sin(phi), 0, np.cos(phi)]
    ])

def rotation_matrix_omega(omega):
    return np.array([
        [1, 0, 0],
        [0, np.cos(omega), np.sin(omega)],
        [0, -np.sin(omega), np.cos(omega)]
    ])

def orientation_matrix(omega, phi, kappa):
    R_omega = rotation_matrix_omega(omega)
    R_phi = rotation_matrix_phi(phi)
    R_kappa = rotation_matrix_kapa(kappa)
    return R_kappa.dot(R_phi).dot(R_omega)



#  showing all table 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# loading AND DEFINING datas 
data = pd.read_csv('data.csv')
data_GCP = pd.read_csv('gcp.csv')
focal_length = 153.692


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
data.insert(loc=11, column='pic_num', value=0)



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
kappa = np.zeros((14,1))
c = 0
p = np.pi 
for i in range(14):

                       #b dx     #a dy
    k0 = np.arctan(u_p[c+1]/u_p[c])
    if u_p[c+1] > 0 and u_p[c] > 0 : 
        kappa[i] = k0 
    if u_p[c+1] > 0 and u_p[c] < 0 : 
        kappa[i] =p - k0
    if u_p[c+1] < 0 and u_p[c] < 0 :
        kappa[i] = k0 + p
    if u_p[c+1] < 0 and u_p[c] > 0 :
        kappa[i] =2*p - k0 
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

# CALCULATING Z0 AND ZM
Z0 = np.zeros((14,1))
Zm = np.mean(data_GCP['Z'])

for i in range(14):
    Z0[i] = landa[i]*focal_length + Zm


# CREATING EOP 
eop_column = ['ran', 'photo' , 'X0' , 'Y0' , 'Z0' ,'W','phi', 'k','landa']
EOP = pd.DataFrame(0, index=range(14), columns=eop_column)
EOP.loc[0:7, 'ran'] = 1
EOP.loc[7:, 'ran'] = 2
for i in range(7):
    EOP.loc[i, 'photo'] = i+1  
    EOP.loc[i+7, 'photo'] = i+1 
EOP['X0'] = X0
EOP['Y0'] = Y0
EOP['Z0'] = Z0
EOP['k'] = k
EOP['landa'] = landa

# EVALUATE UVW (LEFT AND RIGHT )
tie_points_number =max(data['num_Tie'])
UVW_left = np.zeros((tie_points_number*3,1))
UVW_right = np.zeros((tie_points_number*3,1))



# CREATING UVW and k 
def U(w,phi,k,x,y,x0,y0,c):
    M = orientation_matrix(w,phi,k)
    return M[0,0]*(x-x0) + M[1,0]*(y-y0) + M[2,0]*(-c)

def V(w,phi,k,x,y,x0,y0,c):
    M = orientation_matrix(w,phi,k)
    return M[0,1]*(x-x0) + M[1,1]*(y-y0) + M[2,1]*(-c)

def W(w,phi,k,x,y,x0,y0,c):
    M = orientation_matrix(w,phi,k)
    return M[0,2]*(x-x0) + M[1,2]*(y-y0) + M[2,2]*(-c)

def K(X0l, X0r, Y0l, Y0r, Ul, Ur, Vl, Vr):
    return ((X0r - X0l)*Vl - (Y0r - Y0l)*Ul)/(Vr*Ul - Vl*Ur)
    
 
 # adding a column to numbering photos from 1 to 14
for k in range(len(data)):
    i = data.loc[k, "ran"]
    j = data.loc[k, "photo"]
    if i == 1:
        data.loc[k, "pic_num"] = j
    elif i == 2:
        data.loc[k, "pic_num"] = j + 7         


c = 0
for i in range(len(data)):

    if data.loc[i, "POINT.TYPE"] == 0:

        code_temp = data.loc[i, "code"]
        code_list_temp = pd.DataFrame(new_data[code_temp])
        code_list_temp2 = code_list_temp.index[code_list_temp[code_temp] == 1][0:2]
        
        i_l, i_r = code_list_temp2[0], code_list_temp2[1]


        i_r_df = data[(data["code"] == code_temp) & (data["pic_num"] == i_r+1)].index
        i_l_df = data[(data["code"] == code_temp) & (data["pic_num"] == i_l+1)].index
        y_r = data.loc[i_r_df[0], "y"]
        x_r = data.loc[i_r_df[0], "x"]
        x_l = data.loc[i_l_df[0], "x"]
        y_l = data.loc[i_l_df[0], "y"]
        print(x_l)
        kapa_l = kappa[i_l,0]
        kapa_r = kappa[i_r,0]


        # UVW_left[c,0] = U(0,0,kapa_l,x_l,y_l,0,0,focal_length)
        # UVW_left[c+1,0] = V(0,0,kapa_l,x_l,y_l,0,0,focal_length)
        # UVW_left[c+2,0] = W(0,0,kapa_l,x_l,y_l,0,0,focal_length)
        # UVW_right[c,0] = U(0,0,kapa_r,x_r,y_r,0,0,focal_length)
        # UVW_right[c+1,0] = V(0,0,kapa_r,x_r,y_r,0,0,focal_length)
        # UVW_right[c+2,0] = W(0,0,kapa_r,x_r,y_r,0,0,focal_length)
        # c=c+3 




        
        


        






    








# print(data)









