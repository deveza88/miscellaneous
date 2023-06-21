import geopandas as gpd

# Carregando a shapefile original
shapefile_original = gpd.read_file('Export_Output.shp')

# Obtendo os valores únicos da coluna desejada
valores_unicos = shapefile_original['Municipio'].unique()

# Criando uma shapefile para cada valor único da coluna
for valor in valores_unicos:
    # Filtrando os dados com base no valor da coluna
    shapefile_filtrada = shapefile_original[shapefile_original['Municipio'] == valor]

    # Salvando a shapefile filtrada em um novo arquivo
    nome_arquivo = f'./{"RVF_" + valor}.shp'
    shapefile_filtrada.to_file(nome_arquivo, driver='ESRI Shapefile')
