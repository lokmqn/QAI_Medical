# quantum/noise_profiler.py
from qiskit_aer import Aer
import numpy as np

def simulated_t1t2():
    """Return simulated T1 and T2 in μs"""
    return 50.0, 30.0

def dcr_from_t1t2(T1, T2):
    """Decoherence-Clock Rate (Hz)"""
    return 0.5 * ((1/T1) + (1/T2)) * 1e6
