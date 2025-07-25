# quantum/week1_qhi.py
import numpy as np

def qhi(noise, health_score, t1, t1_ref, w=[1.0, 2.0, -0.5]):
    """
    Quantum-Health Index
    noise ∈ [0,1] : device noise
    health_score ∈ [0,1] : AI diagnosis confidence
    """
    z = w[0]*noise + w[1]*health_score + w[2]*(t1/t1_ref)
    return 1.0 / (1.0 + np.exp(-z))

if __name__ == "__main__":
    print("Week-1 QHI example:", qhi(0.3, 0.8, 50, 60))
