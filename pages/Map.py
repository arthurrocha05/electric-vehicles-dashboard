import streamlit as st
import pandas as pd 
import plotly.express as px


# Título 
st.title("Top 10 Cities with Electric Vehicles")


# Leitura dos dados do arquivo CSV usando Pandas
df_electric_vehicle_data = pd.read_csv("datasets/Electric_Vehicle_Data.csv")

# Extração de latitude e longitude da coluna 'Vehicle Location'
df_electric_vehicle_data[['Longitude', 'Latitude']] = df_electric_vehicle_data['Vehicle Location'].str.extract(r'POINT \(([^ ]+) ([^ ]+)\)').astype(float)

# Mapa de dispersão para as 10 principais cidades
# Supondo que o DataFrame tenha colunas 'Latitude' e 'Longitude' para as coordenadas das cidades
fig5 = px.scatter_mapbox(df_electric_vehicle_data.head(10), lat="Latitude", lon="Longitude", size="Electric Range", hover_name="City", 
                        zoom=5, height=700)
fig5.update_layout(mapbox_style="open-street-map")

# Exibição do mapa
st.plotly_chart(fig5)