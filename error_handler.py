"""
Error handling module for the Inventos por País application.
"""

import streamlit as st
import logging
import traceback
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app_errors.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("inventos_app")

class AppError(Exception):
    """Base exception class for application errors."""
    pass

class APIKeyError(AppError):
    """Exception raised for API key related errors."""
    pass

class ModelError(AppError):
    """Exception raised for model related errors."""
    pass

class NetworkError(AppError):
    """Exception raised for network related errors."""
    pass

def handle_error(error, show_traceback=False):
    """
    Handle exceptions and display appropriate error messages to the user.
    
    Args:
        error: The exception that was raised
        show_traceback: Whether to show the full traceback in the UI (for debugging)
    """
    # Log the error
    logger.error(f"Error: {str(error)}")
    logger.error(traceback.format_exc())
    
    # Determine the error type and display appropriate message
    if isinstance(error, APIKeyError):
        st.error("Error de API Key: Verifica que tu API Key de Google Gemini sea válida.")
        st.info("Puedes obtener una nueva API Key en: https://makersuite.google.com/app/apikey")
    elif isinstance(error, ModelError):
        st.error("Error del modelo: Hubo un problema al generar la respuesta.")
        st.info("Intenta nuevamente o selecciona un país diferente.")
    elif isinstance(error, NetworkError):
        st.error("Error de conexión: No se pudo conectar con la API de Google Gemini.")
        st.info("Verifica tu conexión a internet e intenta nuevamente.")
    elif "API key not valid" in str(error).lower() or "api key" in str(error).lower():
        st.error("Error de API Key: La API Key proporcionada no es válida o ha expirado.")
        st.info("Verifica tu API Key o genera una nueva en: https://makersuite.google.com/app/apikey")
    elif "rate limit" in str(error).lower() or "quota" in str(error).lower():
        st.error("Error de límite de uso: Has alcanzado el límite de consultas permitidas.")
        st.info("Espera un momento antes de intentar nuevamente o verifica los límites de tu cuenta.")
    else:
        st.error(f"Error inesperado: {str(error)}")
        st.info("Intenta nuevamente o contacta al administrador si el problema persiste.")
    
    # Show traceback for debugging if enabled
    if show_traceback:
        st.expander("Detalles técnicos del error", expanded=False).code(traceback.format_exc())
