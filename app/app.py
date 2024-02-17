import streamlit as st
from PIL import Image
import io
from utils import query, query2



st.title("Aplicativo Entregable 2")
col1, col2 = st.columns(2)
with col1:
      st.text('Generador Automatico de Imagenes')
      texto = st.text_input("Ingrese un texto")

      if st.button("Generar imagen"):
        image_bytes = query({"inputs": texto ,})
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Imagen Generada", use_column_width=True)


with col2:
  
    st.text('Clasificador de Imagenes')
    uploaded_file = st.file_uploader("Elige una imagen", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image2 = Image.open(uploaded_file)
        st.image(image2, caption="Imagen Subida", use_column_width=True)
        image2.save("/prediccion", "JPEG")
        output = query("prediccion.jpeg")
        st.text(output)


       

#if __name__ == "__main__":
   # main()

