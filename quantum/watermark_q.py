"""
Quantum watermark generator & verifier
"""
import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev)
def watermark_circuit(x, key):
    qml.templates.AngleEmbedding(x, wires=range(4))
    qml.RY(key, wires=0)
    return qml.density_matrix(wires=range(2))

def embed_watermark(image_vec, key):
    return watermark_circuit(image_vec, key)

def verify_watermark(rho1, rho2):
    fidelity = np.trace(np.sqrt(rho1 @ rho2 @ rho1)).real ** 2
    return fidelity < 0.95   # tamper flag
