"""
CTQW Hash generator
"""
import numpy as np

def ctqw_hash(state_vec):
    """Continuous-Time Quantum Walk hash"""
    n = len(state_vec)
    laplacian = np.eye(n) - np.ones((n, n)) / n
    eigvals, eigvecs = np.linalg.eigh(laplacian)
    ctqw_state = np.exp(-1j * eigvals) @ state_vec
    return np.abs(np.fft.fft(ctqw_state)) ** 2
