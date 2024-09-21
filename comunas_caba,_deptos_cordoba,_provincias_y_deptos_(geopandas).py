# -*- coding: utf-8 -*-
"""comunas caba, deptos cordoba, provincias y deptos (geopandas).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FkaXJGOKl4MIDczV_pARxdIHc60164NI
"""

import geopandas as gpd

df_deptos_cordoba = gpd.read_file("https://raw.githubusercontent.com/aaizemberg/2023/main/elecciones/geo/deptos_cordoba.json")
# df_deptos_cordoba.head()
# df_deptos_cordoba.plot();
df_deptos_cordoba.plot(column='personas', cmap='Wistia');

url = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-educacion/comunas/comunas.geojson"
df_caba_comunas = gpd.read_file(url)

df_caba_comunas.head()

df_caba_comunas.plot();

# coloreando a las comunas, por su perimetro.
#
df_caba_comunas.plot(column='PERIMETRO', cmap='Wistia');

url_provincias = "https://aaizemberg.github.io/geo-data/ar/provincias_indec_2010.geojson"
df_provincias = gpd.read_file(url_provincias)
df_provincias.head()

df_provincias.plot();

url_deptos = "https://aaizemberg.github.io/geo-data/ar/deptos_indec_2010.geojson"
df_deptos = gpd.read_file(url_deptos)
df_deptos.head()

# pasa esto, porque hay muchos poligonos que corresponden al mismo ID
#
print('El archivo df_deptos (indec) tiene ' + str(df_deptos.shape[0]) + ' registros')
print('pero el campo "link" que vendria a ser el identificador del depto, tiene ' + str(df_deptos['LINK'].unique().size))
print('Hay varios registros con el mismo LINK, porque los multipoligonos estan desagregados.')

df_deptos.plot();

# url_deptos_IGN = "https://wms.ign.gob.ar/geoserver/ign_riesgo/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=ign_riesgo%3Apoblacion_departamentos_indec_2022&maxFeatures=600&outputFormat=application%2Fjson"
url_deptos_IGN = "https://github.com/aaizemberg/geo-data/blob/gh-pages/ar/ign/poblacion_departamentos_indec_2022.json?short_path=c3c2c86"

df_deptos_ign = gpd.read_file(url_deptos_IGN)

'El archivo df_deptos_ign tiene ' + str(df_deptos_ign.shape[0]) + ' registros.'

df_deptos_ign.info()

"""https://geopandas.org/en/stable/gallery/choropleths.html"""

df_deptos_ign.crs