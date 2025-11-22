En edges.csv tenemos:

-   Primeras columnas del target a predecir
-   Luego un one-hot
    -   Tipo_calle_adoquin
    -   Tipo_calle_asfalto
    -   Tipo_calle_concreto
    -   Tipo_calle_mixto
-   Luego Direccion_calle: Si 1 significa que va a un sentido (sentido dado por el orden de los nodos u,v) y si es 0 va en ambos sentidos.

# Luego entonces si es 0 se agrega otra fila donde sea (v,u)

-   Señal_cerda_el_paso si es 1, hay uno
-   Señal_pare si es 1, htambien hay uno
-   Calle_recta es 1 si la calle es recta y en otro caso, la calle es curva o puede ser una rotonda.
-   Despues tenemos información de las calles (no es un one hot) calle_prioridad (indica si la calle esta pensada para ser de peatones), calle_principal (calle relativa a las autopistas o a grandes calles), calle residencail (calle de transito de personas), calle secundaria y terciarias (guarda la relación con el tipo de calle si se conecta con las primarias y si se conecta con las secundarias, respectivamente).
-   Depues el largo de la calle esta normalizado, en términos simple lo que hice fue dejar los datos dstribucidos de forma que igualesn una gaussiana y sean más continos respestando la distancia: 0.1 esta muy cercano a 0.2 (calles cortas), pero 0.4 esta muy alejado de 0.5 (calles muy largas)
