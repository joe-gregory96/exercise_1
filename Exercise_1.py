import numpy as np

n = input('n = ')
print(n)

n = int(n)
M = np.ndarray((n, n))

a = 0
b = -1
i = 0
j = 0

while j < n:
    if j == i:
        M[i,j] = a
    elif j == i + 1 or j == i - 1:
        M[i,j] = b
    else:
        M[i,j] = 0.00
    if i == n - 1:
        i = 0
        j = j + 1
    else:
        i = i + 1
    


print(M)

#M = np.ndarray((3, 3)) # A 3x3 matrix
#M[0,0] = 5.00
#M[0,1] = 5.00
#M[0,2] = 5.00
#M[1,0] = 5.00
#M[1,1] = 5.00
#M[1,2] = 5.00
#M[2,0] = 5.00
#M[2,1] = 5.00
#M[2,2] = 5.00
#print(M)

def get_evals(str):
    evals, evecs = np.linalg.eig(M)
    print(sorted(evals))
    return

get_evals(M)

#evals, evecs = np.linalg.eig(M)
#print(sorted(evals))

#MI = np.identity(4) # A 4x4 identity matrix
#print(MI)
#Mz = np.zeros((4, 4)) # A 4x4 zero matrix
#print(Mz.shape) # Get the size of a matrix (a,b) means a x b
#lc = Mz.shape[0] # Number of columns in Mz
#for i in range(lc):
#    Mz[i, lc-i-1] = 1 # Max a matrix whose backwards diagonal elements are 1
#M2 = Mz + MI # Add matrices together
#evals, evecs = np.linalg.eig(M2) # get the eigenvalues and vectors
#print(sorted(evals)) # print a sorted list of eigenvalues
