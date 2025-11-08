import open3d as o3d
import numpy as np
import pandas as pd

df = pd.read_csv('dataset/nucleus_position.csv')
# Convertir las columnas a un array de numpy (x, y, z)
points = df[['pt_position_x', 'pt_position_y', 'pt_position_z']].to_numpy()

# Crear el objeto de nube de puntos
pcd = o3d.geometry.PointCloud()

# Asignar las posiciones
pcd.points = o3d.utility.Vector3dVector(points)

# Mostrar en ventana interactiva
o3d.visualization.draw_geometries([pcd])
