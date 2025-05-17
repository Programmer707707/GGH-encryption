# 🔐 GGH Encryption Scheme (Goldreich–Goldwasser–Halevi)

This repository contains a Python implementation of the **GGH public-key encryption scheme**, a foundational lattice-based cryptosystem. The GGH cryptosystem relies on the hardness of lattice problems such as the Closest Vector Problem (CVP), and serves as a basic example of post-quantum encryption techniques.

## 📌 Features

- Full key generation (good and bad lattice bases)
- Encryption using the public (bad) basis
- Decryption using the private (good) basis
- Simple and readable Python code in a single file
- Useful for educational and research purposes

## 🧠 How GGH Works

1. **Key Generation**  
   - Generate a *good basis* `B` (short and nearly orthogonal lattice basis).
   - Multiply with a unimodular matrix `U` to produce a *bad basis* `B' = U × B`.

2. **Encryption**  
   - Convert the plaintext message into a small integer vector `m`.
   - Compute ciphertext `c = B' × m + e`, where `e` is a small random error vector.

3. **Decryption**  
   - Use the private good basis `B` to recover the original message `m` by solving a closest vector problem.

## 🚀 Getting Started

### Requirements

- Python 3.8 or higher
- `numpy` (for matrix and vector operations)

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/ggh-encryption.git
cd GGH-encryption.py
pip install numpy
