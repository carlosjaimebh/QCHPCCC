#made by Jaimito, Betico y Frederito

import matplotlib.pyplot as plt
import numpy as np


#
# Data Generation (Replicating the trends in the image)
x = np.arange(30)
np.random.seed(42)

# Baseline: High energy (~3e9 to 5e9 range)
baseline = np.random.uniform(3e9, 5e9, 30)
# Profile A: Mid energy (~2.5e5 to 4e5 range)
profile_a = np.random.uniform(2.5e5, 4e5, 30)
# Profile B: Low energy (~5.5e4 to 9.5e4 range)
profile_b = np.random.uniform(5.5e4, 9.5e4, 30)

# Create the plot
plt.figure(figsize=(12, 7))

# Plot lines with specific markers and styles
plt.plot(x, baseline, 'rx:', label='Baseline: Classical HPC Only', markersize=6)
plt.plot(x, profile_a, 'go-', label='SDN Profile A: Carbon-Prioritized', markersize=6)
plt.plot(x, profile_b, 'bs-', label='SDN Profile B: Edge-Centric', markersize=6)

# Configure Y-axis as Logarithmic
plt.yscale('log')

# Labels and Styling
plt.title('Comparison of Computing Strategies: Baseline vs SDN Profiles', fontsize=14)
plt.xlabel('Interaction Index', fontsize=12)
plt.ylabel('Energy Consumption (Joules) - Log Scale', fontsize=12)

# Add grid lines (major and minor for the log scale)
plt.grid(True, which="both", ls="--", alpha=0.5)

# Add legend as positioned in the original image
plt.legend(loc='center right', frameon=True)

plt.tight_layout()
plt.show()
