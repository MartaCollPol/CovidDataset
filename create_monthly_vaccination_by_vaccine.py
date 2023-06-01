import pandas as pd

# Cargar el conjunto de datos desde el archivo CSV.
df = pd.read_csv("archive\country_vaccinations_by_manufacturer.csv")

# Eliminar la columna location.
df.drop('location', axis=1, inplace=True)

# Convertir la columna 'fecha' al tipo de datos de fecha.
df['date'] = pd.to_datetime(df['date'])

# Agrupar por mes, tipo de vacuna y calcular el total de vacunas mensuales.
df_monthly = df.groupby([df['date'].dt.to_period('M'),
                         'vaccine'])['total_vaccinations'].sum().reset_index()

# Guardado del conjunto final.
df_monthly.to_csv('archive\monthly_vaccinations_by_manufacturer_world.csv',\
                  index=False)