# quantum/week2_vqnn.py
import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev)
def vqnn(x, theta):
    qml.templates.AngleEmbedding(x, wires=range(4))
    qml.templates.StronglyEntanglingLayers(theta, wires=range(4))
    return qml.expval(qml.PauliZ(0))

def init_theta():
    return np.random.randn(2, 4, 3)  # depth=2, 4 qubits, 3 params per gate
