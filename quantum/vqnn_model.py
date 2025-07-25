# quantum/vqnn_model.py
import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def vqnn_circuit(x, theta):
    qml.templates.AngleEmbedding(x, wires=[0,1])
    qml.templates.StronglyEntanglingLayers(theta, wires=[0,1])
    return qml.expval(qml.PauliZ(0))

def q_entropy_loss(y_true, y_pred, rho, q_noise, b_noise, lam=[0.6,0.3,0.1]):
    S = -np.trace(rho @ np.log(rho + 1e-10)).real
    ce = -y_true*np.log(y_pred) - (1-y_true)*np.log(1-y_pred)
    penalty = np.linalg.norm(q_noise - b_noise)**2
    return lam[0]*S + lam[1]*ce + lam[2]*penalty
