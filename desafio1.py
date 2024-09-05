import numpy as np

# Constante
cts = 5.67e-8
# Placa de acero
A = 0.15  # Área en m^2
e = 0.90  # Emisividad
T = 650  # Temperatura en K
error_T = 20  # Error en la temperatura

# usando la ley de Stefan-Boltzmann
H = A * e * cts * T**4
Tmax = T + error_T
Tmin = T - error_T
Hmax = A * e * cts * Tmax**4
Hmin = A * e * cts * Tmin**4

# Mostrar resultados
print("Solucion:")
print(f"H = {H:.2f} W")
print(f"H_min = {Hmin:.2f} W")
print(f"H_max = {Hmax:.2f} W")
