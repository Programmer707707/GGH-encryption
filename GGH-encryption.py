import numpy as np

def build(n):
    while True:
        mat = np.random.randint(-3, 4, size=(n, n))
        if abs(round(np.linalg.det(mat))) == 1:
            return mat

def prep_keys(n=3):
    B = np.eye(n, dtype=int) * 3  #[[1, 0, 0], [0, 1, 0], [0, 0, 1]]        
    B_inv = np.linalg.inv(B)
    U = build(n)              
    U_inv = np.linalg.inv(U)
    B_pub = U @ B                    
    return B, B_inv, U, U_inv, B_pub

def encrypt(B_pub, m, error_range=1):
    e = np.random.randint(-error_range, error_range+1, size=B_pub.shape[0])
    c = m @ B_pub + e                    
    return c

def decrypt(c, B_inv, U_inv):
    y = c @ B_inv                        
    y_rounded = np.round(y)             
    m = y_rounded @ U_inv               
    return np.round(m).astype(int)

def main():
    B, B_inv, U, U_inv, B_pub = prep_keys(n=3)

    print("Secret Basis B:\n", B)
    print("Public Basis B' = U × B:\n", B_pub)

    print("Uni-modular Matrix: \n", U)
    
    m = np.array([12, -11, 10])           
    print("\nOriginal Message m:\n", m)

    c = encrypt(B_pub, m, error_range=1)
    print("Encrypted Ciphertext c:\n", c)

    m_recovered = decrypt(c, B_inv, U_inv)
    print("Recovered Message m:\n", m_recovered)

if __name__ == "__main__":
    main()
