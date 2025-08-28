import streamlit as st
import pickle

# Cargar el modelo entrenado
with open("modelo_notas.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Predicción de Nota Final :D")
st.write("Ingresa tus datos para predecir tu nota:")

# Entradas del usuario
hours_studied = st.number_input("Horas estudiadas", min_value=0, max_value=24*7, value=5)
previous_scores = st.number_input("Nota previa (0-100)", min_value=0, max_value=100, value=70)
extracurricular = st.selectbox("¿Participa en actividades extracurriculares?", ["Yes", "No"])
sleep_hours = st.number_input("Horas de sueño diarias", min_value=0, max_value=12, value=7)
sample_papers = st.number_input("Exámenes de práctica realizados", min_value=0, max_value=100, value=5)

# Convertir extracurricular a 0/1 si tu modelo lo espera como numérico
extracurricular_num = 1 if extracurricular == "Yes" else 0

# Botón para predecir
if st.button("Predecir mi nota"):
    entrada = [[hours_studied, previous_scores, extracurricular_num, sleep_hours, sample_papers]]
    prediccion = model.predict(entrada)
    st.success(f"Tu nota predicha es: {prediccion[0]:.2f}")
