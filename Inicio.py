import streamlit as st

# -------------------------- CONFIG -------------------------- #
PAGE_CONFIG = {"page_title":"Pandas Mini-Tutorial", 
               "page_icon":"🐼", 
               "layout":"wide", 
               "initial_sidebar_state":"expanded",
               "menu_items":{
                            'Get Help': 'https://github.com/yamilb87/pandas-mini-tutorial/blob/main/README.md',
                            'Report a bug': "https://github.com/yamilb87/pandas-mini-tutorial/issues",
                            'About': "https://github.com/yamilb87/pandas-mini-tutorial"
                            }
                }
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('Introducción a Pandas 🐼', anchor='title-pg1')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            Pandas es una de las bibliotecas más poderosas y ampliamente utilizadas en el mundo de la ciencia de datos en Python.
             Su nombre deriva del término **"panel data"**.
            
            Ofrece una variedad de herramientas para manipular y analizar datos de manera eficiente.
             En este tutorial, exploraremos los conceptos fundamentales de Pandas que
             te ayudarán a trabajar con datos de una manera efectiva.
            
            A continuación, se presenta un resumen de los temas que cubriremos en este tutorial:
            """)

st.markdown("""
            #### 1. Leer y Escribir Archivos:                

            Comenzaremos aprendiendo cómo importar datos desde diferentes fuentes, como archivos _**CSV**_, _**Excel**_, _**SQL**_, _**JSON**_ y más.
            
            Aprendremos cómo utilizar las funciones [read_csv()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html),
            [read_excel()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html),
            [read_sql()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html), y otras para cargar datos en un DataFrame,
            así como también cómo exportar datos desde un DataFrame a varios formatos usando
            [to_csv()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html),
            [to_excel()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html), etc.
            """)

st.markdown("""
            #### 2. Bases de los DataFrames:

            Los DataFrames son la estructura de datos central en Pandas. Aprenderás cómo crear DataFrames desde cero, explorar su estructura,
             conocer sus dimensiones y entender cómo se almacenan los datos en ellos.
            """)

st.markdown("""
            #### 3. Seleccionar Columnas
            
            Aprenderemos cómo acceder y seleccionar columnas específicas de un DataFrame utilizando la notación de corchetes y el operador de punto.
             Además, juntos realizaremos selecciones basadas en condiciones lógicas.
            """)

st.markdown("""
            #### 4. Seleccionar por Tipos de Datos _([dtypes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html))_
            Exploraremos cómo filtrar y seleccionar columnas basadas en el tipo de dato que contienen,
             lo que puede ser útil para trabajar con datos heterogéneos.
            """)

st.markdown("""
            #### 5. Filtrado de Datos (Uso de "loc" e "iloc")

            Usaremos las funciones [loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)
             e [iloc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html) 
            para realizar filtrado avanzado de datos basado en etiquetas de filas o índices enteros. ¡Vamos a resolver problemas juntos!
            """)

st.markdown("""
            #### 6. Consultas (Queries)

            Aprenderemos a realizar consultas complejas en un DataFrame utilizando la función 
            [query()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html),
             lo que nos permitirá filtrar datos de manera más eficiente y legible.
            """)

st.markdown("""
            #### 7. Agrupar (Uso de "groupby")

            Juntos, exploraremos cómo utilizar la función [groupby()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)
             para agrupar datos según una o más columnas, facilitando el análisis de resúmenes y agregaciones de datos.
            """)

st.markdown("""
            #### 8. Datos Faltantes ("Missing Data")

            Manejar datos faltantes es crucial en el análisis de datos. Aprenderemos a identificar, manejar y limpiar valores faltantes en un DataFrame.            
            """)

st.markdown("""
            #### 9. Combinar Datos (usos de _[concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)_ y _[merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html))_
            
            Veremos cómo combinar DataFrames mediante concatenación y fusiones, lo que es esencial para trabajar con datos de múltiples fuentes o realizar análisis complejos. Trabajaremos en proyectos colaborativos.
            """)

st.markdown("""
            #### 10. Manejo de Variables Especiales
            
            Finalmente, exploraremos cómo trabajar con columnas de fecha y hora (datetime) en Pandas,
             incluyendo la conversión de datos de texto en objetos de fecha y hora y la realización de
             operaciones relacionadas con el tiempo.
        

            ¡Estamos emocionados de aprender y crecer juntos en este viaje de Pandas!
             Sigue adelante con los siguientes capítulos de este tutorial para descubrir cómo
             aprovechar al máximo esta biblioteca en Python y no dudes en hacer preguntas o compartir 
             tus propias experiencias a lo largo del camino.
             ¡Vamos a aprender y crecer juntos como una comunidad de entusiastas de los datos!
            """)

