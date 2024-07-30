import numpy as np

temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4.0, -4.0, 12.0, -12.0])

hot_days_indices = np.where(temperatures > 35)[0]
hot_days_temperatures = temperatures[hot_days_indices]

cold_days_indices = np.where(temperatures < 5)[0]
cold_days_temperatures = temperatures[cold_days_indices]

print("Hot Days:")
print("Day  Temperature (°C)")
for i in range(len(hot_days_indices)):
    print(f"{hot_days_indices[i]+1}    {hot_days_temperatures[i]:.1f}")

print("\nCold Days:")
print("Day  Temperature (°C)")
for i in range(len(cold_days_indices)):
    print(f"{cold_days_indices[i]+1}    {cold_days_temperatures[i]:.1f}")
