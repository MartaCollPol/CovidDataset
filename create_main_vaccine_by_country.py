import pandas as pd

# Cargar el conjunto de datos desde el archivo CSV.
df_vaccines = pd.read_csv("datasets\country_vaccinations_by_manufacturer.csv")

# Se suman todas las vacunaciones por país y vacuna.
df_sum_vaccine = df_vaccines.groupby(['location',
                                      'vaccine'])['total_vaccinations'].sum().reset_index()

# Se obtiene la vacuna mayoritaria en cada país. 
df_max_vaccine = df_sum_vaccine.groupby(['location'])['total_vaccinations'].idxmax()
df_max_vaccine = df_sum_vaccine.iloc[df_max_vaccine]

# Se guarda el resultado final.
df_max_vaccine.to_csv('generated_datasets\main_vaccine.csv', index=False)