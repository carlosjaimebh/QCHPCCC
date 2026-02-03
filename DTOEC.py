import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range for Computational Scale (Resolution) and Workload Intensity (Iterations)
# These represent the 'Multiscale' aspect of the paper
resolution = np.linspace(10, 100, 50)  # Grid Resolution
intensity = np.linspace(100, 1000, 50)  # Workload Intensity (Iterations)
R, I = np.meshgrid(resolution, intensity)

# Sustainability Index (Z) based on the paper's findings:
# Efficiency increases with resolution but plateaus, 
# and improves significantly with intensity (energy utilization over consumption).
def calculate_sustainability_3d(r, i):
    # Logarithmic growth for resolution (hardware saturation limit)
    # Linear-to-asymptotic growth for intensity (energy amortization)
    return (np.log(r) * (i / 500)) / (1 + (r * i) / 50000)

S = calculate_sustainability_3d(R, I)

# Create 3D Figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(R, I, S, cmap='viridis', edgecolor='none', alpha=0.8)

# Labels and Titles
ax.set_title('3D Operational Energy Consumption & Sustainability Model', fontsize=14)
ax.set_xlabel('Computational Scale (Resolution)', fontsize=10)
ax.set_ylabel('Workload Intensity (Iterations)', fontsize=10)
ax.set_zlabel('Sustainability Index', fontsize=10)

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

