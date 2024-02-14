import numpy as np 

# defining specific matrixes --------------------------------------------------------------------------------------------------------------------

def ones(a,b):
    A = np.ones([a,b])
    return A

def zeros(a,b):
    A = np.zeros([a,b])
    return A

def eye(a,b):
    A = np.eye([a,b])
    return A

def diag(A):
    A = np.diag(A)
    return A

# matrix operations --------------------------------------------------------------------------------------------------------------------

# 1 MATRIX TRANSPOSE
def transpose(A):
    A = np.transpose(A)
    return A

# 2 MATRIX INVERSE 
def inv(A):
    if np.linalg.det(A) != 0:
        A = np.linalg.inv(A)
    else:
        print(" Singular EROR : Matrix which you entered can't be inversed ")
        A = ''
            
    return A 

# 3 MATRIX DETERMINANT 
def det(A):
    d = np.linalg.det(A)
    return d 

# 4 MATRIX MULTIPLICATION 
def multiply(A,B):
    A = np.asarray(A)
    B = np.asarray(B)
    Ac =  len(A[:][0])   
    Br = len(B[:])
    if (Ac == Br) :
        C = A@B
    else:
        print("Dimention error : Matrix dimensions are incompatible for multiplication")
    
    return C

# 5 MATRIX ADD / MINUS
def add(A,B):
    A = np.asarray(A)
    B = np.asarray(B)
    Bc =  len(A[:][0])   
    Ar = len(B[:])
    Ac =  len(A[:][0])   
    Br = len(B[:])
    if (Ac==Bc and Ar == Br):
        c = A+B
    else : 
        print("Dimention error : for adding two matrix together , the dimentions must be match")
        c = ''
    return c 

def Minus(A,B):
    A = np.asarray(A)
    B = np.asarray(B)
    Bc =  len(A[:][0])   
    Ar = len(B[:])
    Ac =  len(A[:][0])   
    Br = len(B[:])
    if (Ac==Bc and Ar == Br):
        c = A-B
    else : 
        print("Dimention error : for minusing two matrix from each other , the dimentions must be match")
        c = ''
    return c     

# 6 Condition number
def cond(A):
    A = np.asarray(A)
    c = np.linalg.cond(A)
    return c 

# 7 least square (parametric model)
def least_squer(A,L,p = 1):
    '''
     A = Coefficient Matrix 
     L = OBSERVATIONS 
     X = UNKNOWN 
    '''
    X = np.linalg.inv(A.T@p@A)@A.T@p@L
    return X




 


