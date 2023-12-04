import streamlit as st
from models.Chomsky import Chomsky

myChomsky = Chomsky()



data = []

def convertir_lista_a_texto(lista_de_listas):
    texto = ""
    for lista in lista_de_listas:
        texto += ' '.join(map(str, lista)) + '\n'
    return texto


def analizarEstructura( entrada:str ):
    
    lineas = entrada.split('\n')
    label = []
    data.clear()
    resultado = "data...."
    
    
    for i, linea in enumerate(lineas, start=1):
        
        linea = linea.strip()                   
        response =  myChomsky.classifyInput(linea)
        if(not(response == None)):
            data.append(response)
        
    
    print(data)
    

    return resultado

# analizarEstructura('imprimir("hola cero")')

# Interfaz de usuario con Streamlit
st.title("Analizador de Estructura")
st.title(':blue[CodeSphere] :sunglasses:')
option = st.radio("Seleccione la fuente de entrada:", ("Entrada de texto", "Cargar archivo"))

if option == "Entrada de texto":
    inputUser = st.text_area("Ingrese la estructura:")
else:
    file = st.file_uploader("Cargar archivo", type=["txt"])
    if file is not None:
        contenido = file.read()
        inputUser = contenido.decode("utf-8")

if st.button("Analizar"):
    if not inputUser:
        st.write("Por favor, ingrese la estructura o cargue un archivo.")
    else:        
        resultado = analizarEstructura(inputUser)
        st.markdown(resultado, unsafe_allow_html=True)
        st.write(data)