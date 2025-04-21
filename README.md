# Inventos Destacados por País

Una aplicación de Streamlit que utiliza la IA de Google Gemini 2.0-flash para mostrar inventos destacados de diferentes países y su impacto en la sociedad.

## Descripción

Esta aplicación permite a los usuarios:

- Seleccionar un país de un menú desplegable
- Obtener información sobre un invento destacado originado en ese país
- Ver detalles como el inventor, año, descripción e impacto social del invento

La información es generada utilizando el modelo de IA Gemini 2.0-flash de Google, que proporciona datos precisos y contextualizados sobre inventos de todo el mundo.

## Requisitos

Para ejecutar esta aplicación, necesitas tener instalado:

- Python 3.7 o superior
- Las bibliotecas especificadas en `requirements.txt`
- Una API Key de Google Gemini

## Instalación

1. Clona este repositorio o descarga los archivos
2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## Obtener una API Key de Google Gemini

Para utilizar esta aplicación, necesitas una API Key de Google Gemini:

1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crea una cuenta si no tienes una
3. Genera una nueva API Key
4. Copia la API Key para usarla en la aplicación

## Ejecución

Para ejecutar la aplicación:

```bash
streamlit run app.py
```

La aplicación se abrirá en tu navegador web predeterminado. Si no se abre automáticamente, puedes acceder a ella en `http://localhost:8501`.

## Uso

1. Ingresa tu API Key de Google Gemini cuando se te solicite (solo la primera vez)
2. Selecciona un país del menú desplegable en la barra lateral
3. Haz clic en el botón "Buscar Inventos"
4. Explora la información sobre el invento destacado de ese país

## Notas

- La precisión de la información depende del modelo de IA de Google Gemini
- La aplicación requiere conexión a internet para funcionar correctamente
- Cada consulta consume créditos de la API de Google Gemini según sus términos de servicio
