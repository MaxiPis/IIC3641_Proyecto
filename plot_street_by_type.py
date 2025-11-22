import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Cargar nodos y aristas
# node,x_norm,y_norm,street_count
df_nodes = pd.read_csv("nodes_info.csv", sep=";")
df_edges = pd.read_csv("edges_nuevo.csv", sep=",")     # u,v,...,Tipo_calle

# Unir coordenadas a las aristas
df_edges = df_edges.merge(
    df_nodes[['node', 'x_norm', 'y_norm']],
    left_on='u', right_on='node'
).rename(columns={'x_norm': 'x_u', 'y_norm': 'y_u'}).drop(columns=['node'])

df_edges = df_edges.merge(
    df_nodes[['node', 'x_norm', 'y_norm']],
    left_on='v', right_on='node'
).rename(columns={'x_norm': 'x_v', 'y_norm': 'y_v'}).drop(columns=['node'])

# Crear gráficos por tipo
for tipo in sorted(df_edges['Tipo_calle'].unique()):
    subset = df_edges[df_edges['Tipo_calle'] == tipo]

    plt.figure(figsize=(6, 6))
    for _, row in subset.iterrows():
        plt.plot(
            [row['x_u'], row['x_v']],
            [row['y_u'], row['y_v']],
            linewidth=1
        )

    plt.title(f"Grafo para Tipo_calle = {tipo}")
    plt.xlabel("x_norm")
    plt.ylabel("y_norm")
    plt.gca().invert_yaxis()  # Mantiene consistencia con mapas OSM
    plt.grid(True, alpha=0.3)
    plt.show()
