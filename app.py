import streamlit as st

# Titre de l'application
st.set_page_config(page_title="ShinXpert Dashboard", layout="centered")
st.title("⚽ ShinXpert Dashboard")
st.subheader("Smart Shin Guard Interface")

# Colonnes pour afficher les métriques
col1, col2 = st.columns(2)

with col1:
    st.metric(label="❤️ Heart Rate", value="78 bpm")
    st.metric(label="📏 Distance", value="4.6 km")

with col2:
    st.metric(label="🏃‍♂️ Speed", value="22.5 km/h")
    st.metric(label="⚠️ Injury Risk", value="4.0 %")

# Espacement
st.markdown("---")

# Heatmap image
st.subheader("📊 Heatmap (Simulation)")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Heatmap_example.png/640px-Heatmap_example.png", use_column_width=True)

# Footer
st.markdown("Made with 💙 by ShinXpert Team")