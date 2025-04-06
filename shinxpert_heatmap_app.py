import streamlit as st
from PIL import Image
import base64
import io

st.set_page_config(page_title="ShinXpert Dashboard", layout="centered")
st.title("⚽ ShinXpert Dashboard")
st.markdown("#### Smart Shin Guard Interface")

col1, col2 = st.columns(2)
with col1:
    st.metric("❤️ Heart Rate", "78 bpm")
    st.metric("📏 Distance", "4.6 km")
with col2:
    st.metric("🏃‍♂️ Speed", "22.5 km/h")
    st.metric("⚠️ Injury Risk", "4.0 %")

st.divider()

heatmap_base64 = """iVBORw0KGgoAAAANSUhEUgAAAAUA
AAAAF..."""
image_data = base64.b64decode(heatmap_base64)
image = Image.open(io.BytesIO(image_data))

st.subheader("📊 Heatmap (Simulation)")
st.image(image, use_column_width=True)

st.markdown("---")
st.markdown("Made with 💙 by ShinXpert Team")