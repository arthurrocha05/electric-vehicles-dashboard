import streamlit as st
import pandas as pd 
import plotly.express as px

# Configuração da Página para WideScreen
st.set_page_config(layout="wide")

# Título e subtítulo
st.title("Electric Vehicles")
st.markdown("Tracking the Growth and Distribution of Electric Vehicles Across the US")

# Leitura dos dados do arquivo CSV usando Pandas
df_electric_vehicle_data = pd.read_csv("datasets/Electric_Vehicle_Data.csv")

# Extração de latitude e longitude da coluna 'Vehicle Location'
df_electric_vehicle_data[['Longitude', 'Latitude']] = df_electric_vehicle_data['Vehicle Location'].str.extract(r'POINT \(([^ ]+) ([^ ]+)\)').astype(float)

# Definição de valor mínimo e máximo para o alcance elétrico
value_max = df_electric_vehicle_data["Electric Range"].max()
value_min = df_electric_vehicle_data["Electric Range"].min()

# Criação de um slider na barra lateral para filtrar por alcance elétrico
max_range = st.sidebar.slider("Electric Range", value_min, value_max, value_max)
df_range = df_electric_vehicle_data[df_electric_vehicle_data["Electric Range"] <= max_range]

# Exibição do DataFrame filtrado
st.dataframe(df_range)

# Criação de gráficos usando Plotly
# Gráfico de barras para contagem de veículos por ano de modelo
fig = px.bar(df_electric_vehicle_data["Model Year"].value_counts(), title="Number of Vehicles by Model Year")

# Histograma para tipos de veículos elétricos
fig2 = px.histogram(df_electric_vehicle_data, x="Electric Vehicle Type", title="Distribution of Electric Vehicle Types")

# Contagem do número de marcas e criação de um DataFrame
make_counts = df_electric_vehicle_data["Make"].value_counts().reset_index()
make_counts.columns = ["Make", "Count"]
make_counts = make_counts.head(10)

# Gráfico de pizza para distribuição das marcas de veículos elétricos
fig3 = px.pie(make_counts, names="Make", values="Count", title="Distribution of Electric Vehicle Brands")

# Contagem do número de veículos por cidade e criação de um DataFrame
city_counts = df_electric_vehicle_data["City"].value_counts().reset_index()
city_counts.columns = ["City", "Count"]
city_counts = city_counts.head(10)

# Gráfico de pizza para distribuição de veículos elétricos por cidade
fig4 = px.pie(city_counts, names="City", values="Count", title="Distribution of Electric Vehicles per City")



# Divisão da tela em duas colunas e exibição dos gráficos
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col1.plotly_chart(fig3)
col2.plotly_chart(fig4)
col2.plotly_chart(fig2)

