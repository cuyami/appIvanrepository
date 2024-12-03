import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Mi Negocio",
    page_icon=":briefcase:",
    layout="wide"
)

# Función para cargar imágenes
def cargar_imagenes():
    return [
        "imagenes/trabajo1.jpg",
        "imagenes/trabajo2.jpg",
        "imagenes/trabajo3.jpg"
    ]

# Función para mostrar la galería
def mostrar_galeria():
    st.title("Nuestros Trabajos")
    st.write("Aquí puedes ver algunos de los proyectos que hemos realizado.")
    imagenes = cargar_imagenes()

    # Crear columnas para la galería
    cols = st.columns(3)
    for i, img_path in enumerate(imagenes):
        with cols[i % 3]:
            img = Image.open(img_path)
            # Cambiar use_column_width por use_container_width
            st.image(img, use_container_width=True, caption=f"Trabajo {i + 1}")


# Menú lateral
st.sidebar.title("Menú")
pagina = st.sidebar.radio(
    "Selecciona una página",
    ["Inicio", "Formulario de Contacto", "Petición de Trabajo", "Nuestros Trabajos"]
)
# Estilo personalizado para el menú lateral
st.markdown(
    """
    <style>
    /* Cambiar el tamaño de la fuente del menú lateral */
    [data-testid="stSidebar"] * {
        font-size: 1.03em; /* Cambia este valor según lo necesario */
    }
    </style>
    """,
    unsafe_allow_html=True
)




# Navegación entre páginas
if pagina == "Inicio":
    st.title("Bienvenidos a Mi Negocio")
    st.write("Dirección: Calle Ejemplo, 123, Ciudad")
    st.write("Teléfono: +34 123 456 789")
    st.write("Correo: contacto@minegocio.com")
    logo = Image.open("imagenes/logo.png")
    st.image(logo, width=200)

elif pagina == "Formulario de Contacto":
    st.title("Formulario de Contacto")
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo")
    mensaje = st.text_area("Mensaje")
    if st.button("Enviar"):
        st.success("¡Gracias por contactarnos!")

elif pagina == "Petición de Trabajo":
    st.title("Petición de Trabajo")
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo")
    archivos = st.file_uploader("Adjunta tus archivos (máximo 3)", accept_multiple_files=True)
    observaciones = st.text_area("Observaciones")
    if st.button("Enviar"):
        st.success("¡Gracias por tu solicitud!")

elif pagina == "Nuestros Trabajos":
    mostrar_galeria()
