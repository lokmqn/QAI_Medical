# math/week1_qentropy.py
import numpy as np

def q_entropy_loss(y_true, y_pred, rho, q_noise, b_noise, lam=[0.6,0.3,0.1]):
    S = -np.trace(rho @ np.log(rho + 1e-10)).real
    ce = -y_true*np.log(y_pred) - (1-y_true)*np.log(1-y_pred)
    penalty = np.linalg.norm(q_noise - b_noise)**2
    return lam[0]*S + lam[1]*ce + lam[2]*penalty

if __name__ == "__main__":
    print("Week-1 Q-Entropy Loss demo:", q_entropy_loss(1, 0.9, np.eye(2)/2, 0.2, 0.1))
