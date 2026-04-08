import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de la página
st.set_page_config(page_title="Spotify Strategic Insights 2026", layout="wide")

@st.cache_data
def load_data():
    url = "https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset/resolve/main/dataset.csv"
    df = pd.read_csv(url)
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    return df

st.title("🎵 Dashboard de Decisiones Estratégicas: Spotify Dataset")
data = load_data()

# --- FILAS DE KPIs ---
col1, col2 = st.columns(2)

with col1:
    # KPI 1: Géneros Dominantes
    st.subheader("1. Cuota de Mercado por Género")
    genre_pop = data.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(10).reset_index()
    fig1 = px.bar(genre_pop, x='popularity', y='track_genre', orientation='h', color='popularity', color_continuous_scale='Viridis')
    st.plotly_chart(fig1, width='stretch')
    st.info("Justificación: Identifica géneros para inversión publicitaria.")

with col2:
    # KPI 2: Mood Analysis (Scatter)
    st.subheader("2. Target de Audiencia (Mood)")
    sample = data.sample(1000)
    fig2 = px.scatter(sample, x='valence', y='energy', color='popularity', hover_data=['track_name'])
    st.plotly_chart(fig2, width='stretch')
    st.info("Justificación: Define si la playlist es para Relax o Energía.")

col3, col4 = st.columns(2)

with col3:
    # KPI 3: Contenido Explícito
    st.subheader("3. Impacto del Contenido Explícito")
    explicit_count = data['explicit'].value_counts().reset_index()
    fig3 = px.pie(explicit_count, values='count', names='explicit', hole=0.4, title="¿Es la música explícita más común?")
    st.plotly_chart(fig3, width='stretch')
    st.info("Justificación: Determina la viabilidad en canales familiares.")

with col4:
    # KPI 4: Bailabilidad vs Popularidad
    st.subheader("4. Correlación Danceability/Éxito")
    # Agrupamos por rangos de bailabilidad
    data['dance_range'] = pd.cut(data['danceability'], bins=5)
    dance_pop = data.groupby('dance_range', observed=True)['popularity'].mean().reset_index()
    dance_pop['dance_range'] = dance_pop['dance_range'].astype(str)
    fig4 = px.line(dance_pop, x='dance_range', y='popularity', markers=True)
    st.plotly_chart(fig4, width='stretch')
    st.info("Justificación: Ayuda a decidir el ritmo de los próximos lanzamientos.")

# --- TABLA REQUERIDA ---
st.divider()
st.subheader("📊 Tabla de Datos Crudos (Muestra)")
st.dataframe(data.head(20), width='stretch')