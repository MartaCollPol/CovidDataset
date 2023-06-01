import pandas as pd

# Cargar el conjunto de datos desde el archivo CSV.
df = pd.read_csv("datasets\country_vaccinations.csv")

# Convertir la columna 'date' al tipo de datos de fecha.
df['date'] = pd.to_datetime(df['date'])

# Obtener la fila con la fecha más reciente para cada país.
df_latest = df.loc[df.groupby('country')['date'].idxmax()]

# Guardado del conjunto final.
df_latest.to_csv('generated_datasets\fully_vaccinated.csv', index=False)