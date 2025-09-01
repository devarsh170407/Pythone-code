# Verify the Pythagorean identity: sin²θ + cos²θ = 1 for θ = [0, 30, 45, 60, 90] degrees.

import numpy as np

ad = np.array([0, 30, 45, 60, 90])

ar = np.deg2rad(ad)

i= np.sin(ar)**2 + np.cos(ar)**2

print("angles (degrees):",ad)
print("sin^2(theta) + cos^2(theta):", i)
