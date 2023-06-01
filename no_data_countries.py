import pandas as pd
import io

# Cargar los conjuntos de datos desde el archivo CSV.
df_vaccines = pd.read_csv("datasets\country_vaccinations_by_manufacturer.csv")
df_pos = pd.read_csv("datasets\world_locations.csv", sep=",")

# Localizar diferencias en nombres de países de ambos conjuntos de datos.
column1 = df_pos['locations']
column2 = df_vaccines['location']

values_not_in_column2 = column1[~column1.isin(column2)].tolist()
with io.open("tmp/notfound2.txt", 'w', encoding='utf-8') as f:
    for value in values_not_in_column2:
        f.write(str(value) + '\n')