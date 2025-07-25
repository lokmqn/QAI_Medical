# quantum/week4_ctw_hash.py
import numpy as np

def ctqw_hash(state_vec):
    """
    Continuous-Time Quantum Walk Hash
    Returns 256-bit digest
    """
    n = len(state_vec)
    lap = np.eye(n) - np.ones((n,n))/n
    eigvals, eigvecs = np.linalg.eigh(lap)
    ctqw = np.exp(-1j * eigvals) @ state_vec
    digest = np.abs(np.fft.fft(ctqw))**2
    return digest[:32]  # 256 bits
