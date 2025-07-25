# quantum/week4_federated.py
import numpy as np

def federated_average(weights, volumes):
    """
    Quantum-volume weighted FedAvg
    weights: list of local model arrays
    volumes: list of int (Quantum Volume)
    """
    weights = np.array(weights, dtype=object)
    volumes = np.array(volumes)
    global_weights = np.average(weights, axis=0, weights=volumes)
    return global_weights
  
