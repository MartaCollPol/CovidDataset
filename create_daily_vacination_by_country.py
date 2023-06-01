import pandas as pd
import io

# Cargar los conjuntos de datos desde el archivo CSV.
df_vaccines = pd.read_csv("datasets\country_vaccinations_by_manufacturer.csv")
df_pos = pd.read_csv("datasets\geopositions_countries.csv", sep=",")

# Localizar diferencias en nombres de países de ambos conjuntos de datos.
column1 = df_vaccines['location']
column2 = df_pos['location']

values_not_in_column2 = column1[~column1.isin(column2)].tolist()
with io.open("tmp/notfound.txt", 'w', encoding='utf-8') as f:
    for value in values_not_in_column2:
        f.write(str(value) + '\n')

# Cambio de formato de fecha.
df_vaccines['date'] = pd.to_datetime(df_vaccines['date'])
df_vaccines['date'] = df_vaccines['date'].dt.strftime('%d/%m/%Y')

# Se suman todas las vacunaciones del dia por país.
df_sum_vaccine = df_vaccines.groupby(['location',
                                      'date'])['total_vaccinations'].sum().reset_index()

# Merge de los datasets para añadir las longitudes y latitudes.
df_merged = pd.merge(df_sum_vaccine, df_pos, on='location')

# Corrección de formato en longitudes y latitudes.
df_merged['longitude'] = df_merged['longitude'].str.replace(',', '.')
df_merged['latitude'] = df_merged['latitude'].str.replace(',', '.')

# Borrado de columnas no usadas.
df_merged = df_merged.drop(columns=['x', 'y'])

# Se guarda el resultado final.
df_merged.to_csv('generated_datasets\daily_vaccination.csv', index=False)