#Quantum Computing Ratio vs Classical Ration in a Computing Continuum Framework

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters inspired by the Computing Continuum framework [based in Paper]
TOTAL_NODES = 100
QUANTUM_RATIO = 0.20  # Scenario requested: 30% Quantum nodes
CLASSICAL_RATIO = 0.80

# Energy/Performance Profiles [cite: 525, 552]
# HPC nodes: High consumption, linear scaling for massive workloads [cite: 534]
hpc_energy_cons = 250   # Watts
hpc_capacity = 100      # Classical tasks/sec

# Quantum nodes: Higher efficiency for complex kernels (Non-Von Neumann) [cite: 539, 72]
qpu_energy_cons = 80    # Watts (Cooling + Control)
qpu_capacity = 800      # Exponential speedup for specific optimization tasks [cite: 74, 75]

def calculate_sustainability(load):
    # Determine nodes in each category
    q_nodes = TOTAL_NODES * QUANTUM_RATIO
    c_nodes = TOTAL_NODES * CLASSICAL_RATIO
    
    # Total Energy Consumed (static + dynamic overhead) [cite: 552]
    total_cons = (q_nodes * qpu_energy_cons) + (c_nodes * hpc_energy_cons)
    
    # Energy Utilized (Work effectively performed at given load) [cite: 552]
    q_work = (q_nodes * qpu_capacity) * load
    c_work = (c_nodes * hpc_capacity) * load
    
    # Sustainability Index = Energy Utilized / Energy Consumed [cite: 551]
    return (q_work + c_work) / total_cons

# Generate Data
workload_range = np.linspace(0.1, 1.0, 50)
hybrid_index = [calculate_sustainability(l) for l in workload_range]

# Baseline: 100% Classical HPC cluster
baseline_index = [(TOTAL_NODES * hpc_capacity * l) / (TOTAL_NODES * hpc_energy_cons) for l in workload_range]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(workload_range * 100, hybrid_index, label='Hybrid (20% QPU)', color='teal', linewidth=2.5)
plt.plot(workload_range * 100, baseline_index, label='Baseline (100% HPC)', color='gray', linestyle='--')
plt.title('Digital Twin: Sustainability Index in Hybrid Architectures', fontsize=14)
plt.xlabel('System Workload (%)', fontsize=12)
plt.ylabel('Sustainability Index (Work/Energy)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.2)
plt.show()
