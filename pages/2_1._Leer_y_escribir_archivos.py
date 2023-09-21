import streamlit as st
import numpy as np
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG -------------------------- #
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('1. Lectura y escritura de Archivos')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            Comencemos nuestro viaje en Pandas aprendiendo cómo cargar y guardar datos desde y hacia una variedad de fuentes y formatos.
             Pandas hace que esta tarea sea sencilla y versátil. A continuación, exploraremos cómo hacerlo con ejemplos prácticos.
            """)

# Lectura de Archivos
# CSV
st.markdown("""
            #### Leer Archivos
            ##### a) Archivos CSV:

            Supongamos que tenemos un archivo CSV llamado _'datos.csv'_ con datos tabulares. 
            Podemos cargarlo en un DataFrame de la siguiente manera:        
            """)

st.code("""
        import pandas as pd

        # Cargar datos desde un archivo CSV
        df = pd.read_csv('datos.csv')
        """)

# Excel
st.markdown("""
            ##### b) Archivos Excel:
            Si tenemos un archivo Excel llamado _'datos.xlsx'_, Pandas también nos permite cargarlo fácilmente:
            """)
st.code("""
        import pandas as pd

        # Cargar datos desde un archivo Excel
        df = pd.read_excel('datos.xlsx')
        """)

# SQL
st.markdown("""
            ##### c) Datos desde una Base de Datos SQL:
            Podemos leer datos directamente desde una base de datos SQL utilizando Pandas.
             Supongamos que tenemos una base de datos SQLite con una tabla llamada _'empleados'_:
            """)
st.code("""                
        import pandas as pd
        import sqlite3

        # Conectar a la base de datos
        conn = sqlite3.connect('mi_base_de_datos.db')

        # Cargar datos desde SQL a un DataFrame
        query = "SELECT * FROM empleados"
        df = pd.read_sql(query, conn)
        """)

# Escritura de archivos
# CSV
st.markdown("""
            ---
            #### Escribir Archivos
            Pandas también facilita la exportación de datos de un DataFrame a diferentes formatos.

            ##### a) Archivos CSV:
            Para guardar un DataFrame en un archivo CSV, puedes hacerlo de la siguiente manera:
            """)

st.code("""
        # Guardar el DataFrame en un archivo CSV
        df.to_csv('nuevo_datos.csv', index=False)  # El argumento index=False evita la escritura del índice en el archivo.
        """)

# Excel
st.markdown("""            
            ##### b) Archivos Excel:
            Guardar un DataFrame en un archivo Excel es igual de simple:
            """)

st.code("""
        # Guardar el DataFrame en un archivo Excel
        df.to_excel('nuevo_datos.xlsx', index=False)
        """)


st.markdown("""
            Estos son solo algunos ejemplos iniciales de cómo Pandas nos permite cargar y guardar datos desde y hacia diferentes fuentes y formatos.
            A medida que avancemos en este tutorial, exploraremos más opciones y técnicas avanzadas para manipular datos con Pandas.
            ¡Sigue aprendiendo y descubriendo todas las capacidades de esta increíble biblioteca!
            """)