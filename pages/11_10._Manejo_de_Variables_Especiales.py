import streamlit as st
import pandas as pd

from Inicio import PAGE_CONFIG

# -------------------------- CONFIG --------------------------
# Config Page
st.set_page_config(**PAGE_CONFIG)
st.title('10. Manejo de Variables Especiales')
st.sidebar.success('Seleccionar página. ☝️')

# -------------------------- CONTENIDO -------------------------- #

st.markdown("""
            El manejo de variables especiales, como las fechas y horas (datetime), es fundamental en el análisis de datos.
             Pandas ofrece excelentes capacidades para trabajar con datos temporales y otras variables especiales.
             A continuación, exploraremos cómo manejar variables datetime en Pandas con ejemplos adicionales.
            
            #### Creación de Variables Datetime
            Para trabajar con fechas y horas en Pandas, primero debemos asegurarnos de que las columnas se reconozcan como variables datetime.
             Supongamos que tenemos un DataFrame df con una columna 'Fecha' que contiene fechas como cadenas de texto:
            """)
st.code("""
        import pandas as pd

        data = {
            'Fecha': ['2023-09-16', '2023-09-17', '2023-09-18'],
            'Valor': [100, 150, 120]
        }

        df = pd.DataFrame(data)
        """)
st.write("Para convertir la columna 'Fecha' a una variable datetime:")

st.code("""
        # Convertir la columna 'Fecha' a datetime
        df['Fecha'] = pd.to_datetime(df['Fecha'])

        print(df)
        """)

st.markdown("""
            #### Operaciones con Variables Datetime
            Una vez que las columnas son datetime, podemos realizar diversas operaciones,
             como extracción de componentes de fecha y cálculos. Por ejemplo:
            """)
st.code("""
        # Extraer el día de la semana
        df['Dia_de_la_Semana'] = df['Fecha'].dt.day_name()

        # Extraer el mes
        df['Mes'] = df['Fecha'].dt.month

        # Calcular el número de días transcurridos desde una fecha específica
        fecha_referencia = pd.to_datetime('2023-09-16')
        df['Dias_Transcurridos'] = (df['Fecha'] - fecha_referencia).dt.days

        print(df)
        """)

st.markdown("""
            #### Indexación por Datetime
            Pandas permite usar una columna datetime como índice.
             Esto puede ser útil para realizar selecciones basadas en fechas o realizar agregaciones temporales.
            """)
st.code("""
        # Establecer la columna 'Fecha' como índice
        df.set_index('Fecha', inplace=True)

        # Seleccionar datos por rango de fechas
        subset = df['2023-09-16':'2023-09-17']

        print(subset)

        """)

st.markdown("""
            #### Resampleo de Datos Temporales
            Pandas proporciona la función resample() que permite realizar agregaciones en datos temporales.
             Por ejemplo, para obtener la media semanal de los valores:
            """)
st.code("""
        # Resampleo para obtener la media semanal
        media_semanal = df['Valor'].resample('W').mean()

        print(media_semanal)
        """)

# Generación del Dataframe Ejemplo
data = {
        'Fecha': ['2023-09-16', '2023-09-17', '2023-09-18'],
        'Valor': [100, 150, 120]
        }
df = pd.DataFrame(data)
df['Fecha'] = pd.to_datetime(df['Fecha'])
# Establecer la columna 'Fecha' como índice
df.set_index('Fecha', inplace=True)

# Resampleo para obtener la media semanal
media_semanal = df['Valor'].resample('W').mean()
with st.expander("mostrar resultado:"):
    st.dataframe(media_semanal)

st.markdown("""
            #### Manejo de Zonas Horarias
            Pandas también puede manejar zonas horarias en datos datetime.
             Puedes convertir zonas horarias y realizar cálculos en diferentes zonas horarias según sea necesario.

            Supongamos que tenemos una columna 'Fecha_Hora' con zonas horarias:
            """)
st.code("""
        import pandas as pd

        data = {
            'Fecha_Hora': ['2023-09-16 08:00:00-04:00', '2023-09-17 09:00:00-05:00', '2023-09-18 10:00:00-06:00'],
            'Valor': [100, 150, 120]
        }

        df = pd.DataFrame(data)
        df['Fecha_Hora'] = pd.to_datetime(df['Fecha_Hora']).dt.tz_convert('UTC')

        print(df)
        """)

st.markdown("""
            El manejo de variables datetime en Pandas es esencial para análisis de series temporales
             y aplicaciones relacionadas con el tiempo.
             Estos ejemplos adicionales te ayudarán a comprender mejor cómo trabajar con fechas y horas en Pandas.
             ¡Sigue explorando y aprendiendo más sobre esta poderosa biblioteca!
            """)