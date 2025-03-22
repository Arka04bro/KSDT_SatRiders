
import numpy as np

size = 10e-3  
E = 2.1e9  
nu = 0.38  
rho = 1.27e3  
g = 9.81  
G = 6  
F_per_volume = rho * G * g  
elems = 8  
nodes = elems + 1  

def stiffness_matrix(E, nu):
    C = E / ((1 + nu) * (1 - 2 * nu)) * np.array([
        [1 - nu, nu, nu, 0, 0, 0],
        [nu, 1 - nu, nu, 0, 0, 0],
        [nu, nu, 1 - nu, 0, 0, 0],
        [0, 0, 0, (1 - 2 * nu) / 2, 0, 0],
        [0, 0, 0, 0, (1 - 2 * nu) / 2, 0],
        [0, 0, 0, 0, 0, (1 - 2 * nu) / 2]
    ])
    return C

K_global = np.zeros((3 * nodes, 3 * nodes))  
C = stiffness_matrix(E, nu)

for i in range(elems):
    for j in range(3):  
        for k in range(3):
            K_global[3*i + j, 3*i + k] += C[j, k]
            K_global[3*i + j, 3*(i+1) + k] += C[j, k + 3]
            K_global[3*(i+1) + j, 3*i + k] += C[j + 3, k]
            K_global[3*(i+1) + j, 3*(i+1) + k] += C[j + 3, k + 3]

F = np.zeros(3 * nodes)  
F[3:] = F_per_volume * (size**3 / elems)  

fixed_dofs = np.arange(3)  
free_dofs = np.arange(3, 3 * nodes)  
K_mod = K_global[np.ix_(free_dofs, free_dofs)]
F_mod = F[free_dofs]

U_mod = np.linalg.solve(K_mod, F_mod)
U = np.zeros(3 * nodes)
U[free_dofs] = U_mod  

for i in range(nodes):
    print(f"Узел {i}: Смещение = {U[3*i]:.6e} м, {U[3*i+1]:.6e} м, {U[3*i+2]:.6e} м")
