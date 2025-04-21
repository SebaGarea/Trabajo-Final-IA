import streamlit as st
import google.generativeai as genai
import os

# --- Configuración Inicial ---
st.set_page_config(page_title="Inventos por País", page_icon="💡")
st.title("💡 Descubre Inventos por País con Gemini")
st.caption("Una app para explorar inventos notables y su impacto.")

# --- Configuración de la API de Gemini ---
try:
    # Intenta obtener la clave API desde los secretos de Streamlit
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest') # Usamos el modelo flash
except KeyError:
    st.error("⚠️ Clave API de Google no encontrada. Asegúrate de configurarla en st.secrets.")
    st.stop() # Detiene la ejecución si no hay clave API
except Exception as e:
    st.error(f"🚨 Error al configurar Gemini: {e}")
    st.stop()

# --- Interfaz de Usuario ---
paises = [
    "Selecciona un país...", "Argentina", "México", "España", "Colombia", "Perú",
    "Chile", "Estados Unidos", "Reino Unido", "Alemania", "Francia",
    "Japón", "China", "India", "Brasil", "Canadá", "Italia", "Corea del Sur"
    # Puedes añadir más países aquí
]

pais_seleccionado = st.selectbox("Elige un país:", paises)

# --- Lógica del Botón y Llamada a la API ---
if st.button("Buscar Inventos"):
    if pais_seleccionado != "Selecciona un país...":
        st.write(f"Buscando un invento destacado de {pais_seleccionado}...")

        # Prepara el prompt para Gemini
        prompt = f"""
        Describe un invento destacado originado en {pais_seleccionado}.
        Incluye:
        1. El nombre del invento.
        2. Una breve explicación de qué es y cómo funciona.
        3. Su impacto principal en la sociedad o en un campo específico.
        Sé conciso y claro.
        """

        try:
            # Muestra un spinner mientras se genera la respuesta
            with st.spinner('🧠 Pensando... Gemini está generando la respuesta...'):
                response = model.generate_content(prompt)

            # Muestra la respuesta
            st.subheader(f"Invento Destacado de {pais_seleccionado}:")
            st.markdown(response.text) # Usamos markdown para mejor formato

        except Exception as e:
            st.error(f"🚨 Ocurrió un error al contactar a Gemini: {e}")
            st.warning("Intenta de nuevo más tarde o revisa tu conexión/clave API.")

    else:
        st.warning("Por favor, selecciona un país de la lista.")

# --- Pie de página (Opcional) ---
st.markdown("---")
st.caption("Desarrollado con Streamlit y Google Gemini.")
