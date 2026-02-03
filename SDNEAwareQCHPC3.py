# SDN-Based Carbon-Aware Routing - Simulation

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Simulation Configuration
# --------------------------------------------------
np.random.seed(7)

num_interactions = 30
quantum_ratio = 0.30

# Device counts
quantum_edge_devices = 4
classical_edge_devices = 12

# --------------------------------------------------
# Power Models (Watts)
# --------------------------------------------------
power_classical_edge = 250          # Classical edge device
power_quantum_edge = 5000           # Quantum edge device (control + cooling)
power_hpc = 25e6                    # Classical HPC data center (25 MW)
power_big_qpu = 75e3                # Large-scale quantum computer (75 kW)

# --------------------------------------------------
# Execution Time per Task (seconds)
# --------------------------------------------------
time_classical_edge = 2.0
time_quantum_edge = 0.3
time_hpc = 1.5
time_big_qpu = 0.2

# --------------------------------------------------
# Carbon Intensity (kg CO2 / kWh)
# --------------------------------------------------
carbon_hpc = 0.45                   # Fossil-dominated grid
carbon_big_qpu_green = 0.05         # Renewable-powered quantum site

# --------------------------------------------------
# Results Storage
# --------------------------------------------------
energy_classical = []
energy_sdn_quantum = []
carbon_classical = []
carbon_sdn = []

# --------------------------------------------------
#  Simulation Loop
# --------------------------------------------------
for _ in range(num_interactions):

    # Incoming workload burst
    tasks = np.random.randint(80, 120)

    quantum_tasks = int(tasks * quantum_ratio)
    classical_tasks = tasks - quantum_tasks

    # ---------- Classical-only execution (HPC baseline) ----------
    energy_hpc = tasks * power_hpc * time_hpc
    energy_classical.append(energy_hpc)

    carbon_classical.append(
        (energy_hpc / 3.6e6) * carbon_hpc
    )

    # ---------- SDN-Based Carbon-Aware Hybrid Execution ----------
    # Classical tasks processed at the edge
    energy_classical_edge = (
        classical_tasks / classical_edge_devices
        * power_classical_edge
        * time_classical_edge
    )

    # Quantum tasks processed at quantum edge devices
    energy_quantum_edge = (
        quantum_tasks / quantum_edge_devices
        * power_quantum_edge
        * time_quantum_edge
    )

    # SDN routes heavy quantum tasks (40%) to green Big QPU
    heavy_quantum_tasks = int(0.4 * quantum_tasks)
    energy_big_qpu = (
        heavy_quantum_tasks
        * power_big_qpu
        * time_big_qpu
    )

    total_energy = (
        energy_classical_edge
        + energy_quantum_edge
        + energy_big_qpu
    )

    energy_sdn_quantum.append(total_energy)

    carbon_sdn.append(
        (energy_big_qpu / 3.6e6) * carbon_big_qpu_green
    )

# --------------------------------------------------
# Visualization (Scatter Plot + Grid + External Legend)
# --------------------------------------------------
plt.figure(figsize=(8, 4))

plt.scatter(
    range(num_interactions),
    energy_classical,
    label="Classical HPC Only",
     marker="o",
    color="orange"
)

plt.scatter(
    range(num_interactions),
    energy_sdn_quantum,
    label="SDN Carbon-Aware Quantum Computing Continuum",
    marker="o",
    color="green"
)

plt.xlabel("Interaction Index")
plt.ylabel("Energy Consumption (Joules)")
plt.title("Digital Twin Energy Behavior with SDN-Based Carbon-Aware Routing")

# Grid in background
plt.grid(True)

# Legend outside, lower center
plt.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.25),
    ncol=2,
    frameon=False
)

plt.tight_layout()
plt.show()

# --------------------------------------------------
# Summary Metrics
# --------------------------------------------------
print("Average Energy (Classical HPC):",
      np.mean(energy_classical), "J")

print("Average Energy (SDN Quantum):",
      np.mean(energy_sdn_quantum), "J")

print("Average Carbon (Classical HPC):",
      np.mean(carbon_classical), "kg CO2")

print("Average Carbon (SDN Quantum):",
      np.mean(carbon_sdn), "kg CO2")

