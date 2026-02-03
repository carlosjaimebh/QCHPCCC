#Simulation Parameters based into Multiscale HPC analysis 


import numpy as np
import matplotlib.pyplot as plt

# Simulation Parameters based on the Multiscale HPC Paper
TOTAL_NODES = 100
QUANTUM_RATIO = 0.30  # 30% Quantum Units
CLASSICAL_RATIO = 1 - QUANTUM_RATIO

# Energy and Performance Profiles (Synthetic based on paper's metrics)
# HPC nodes focus on high throughput but high consumption
hpc_energy_cons = 250  # Watts per node
hpc_workload_cap = 100 # Tasks/sec

# Quantum nodes (Tight Integration) - Lower energy for complex tasks
qpu_energy_cons = 50   # Watts per node (QPU cooling/control)
qpu_workload_cap = 500 # Exponential speedup for specific kernels

def simulate_continuum(load_level):
    """Simulates Sustainability Index across different system loads."""
    # Node distribution
    q_nodes = TOTAL_NODES * QUANTUM_RATIO
    c_nodes = TOTAL_NODES * CLASSICAL_RATIO
    
    # Calculate Energy Consumed (Static + Dynamic)
    total_energy = (q_nodes * qpu_energy_cons) + (c_nodes * hpc_energy_cons)
    
    # Calculate Energy Utilized (Work done based on load)
    # Quantum units are more efficient at high complexity tasks
    q_util = (q_nodes * qpu_workload_cap) * load_level
    c_util = (c_nodes * hpc_workload_cap) * load_level
    
    # Sustainability Index = Energy Utilized / Energy Consumed
    sustainability_index = (q_util + c_util) / total_energy
    return sustainability_index, total_energy

# Run Simulation for 0% to 100% Load
loads = np.linspace(0.1, 1.0, 10)
indices_hybrid = [simulate_continuum(l)[0] for l in loads]

# Baseline (0% Quantum)
def simulate_baseline(load_level):
    total_energy = TOTAL_NODES * hpc_energy_cons
    total_util = (TOTAL_NODES * hpc_workload_cap) * load_level
    return total_util / total_energy

indices_baseline = [simulate_baseline(l) for l in loads]

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(loads*100, indices_hybrid, 'c-o', label='Hybrid Architecture (30% Quantum Elements)')
plt.plot(loads*100, indices_baseline, 'y-*', label='Classical HPC Baseline')
plt.title('Digital Twin: Sustainability Index vs System Load')
plt.xlabel('System Workload (%)')
plt.ylabel('Sustainability Index (Work/Energy)')
plt.legend()
plt.grid(True)
plt.show()
