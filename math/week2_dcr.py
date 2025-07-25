# math/week2_dcr.py
from quantum.noise_profiler import simulated_t1t2, dcr_from_t1t2

T1, T2 = simulated_t1t2()
print("Week-2 DCR =", dcr_from_t1t2(T1, T2), "Hz")
