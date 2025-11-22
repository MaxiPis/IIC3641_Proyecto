import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset (cambia la ruta)
# usa sep="," si tu CSV viene con coma
df = pd.read_csv("nodes_info.csv", sep=";")

# Plot
plt.figure(figsize=(7, 7))
plt.scatter(
    df["x_norm"],
    df["y_norm"],
    c=df["street_count"],   # color por atributo
    s=10,                   # tamaño del punto
)
plt.xlabel("x_norm")
plt.ylabel("y_norm")
plt.title("Nodos coloreados por street_count")
plt.colorbar(label="street_count")

plt.show()
