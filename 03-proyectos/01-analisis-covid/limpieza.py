import pandas as pd


def cargar_datos():
    try:
        df_covid = pd.read_csv("03-proyectos/01-analisis-covid/data/fallecidos_covid.csv", delimiter=";", parse_dates=["FECHA_CORTE", "FECHA_FALLECIMIENTO"])
        df_covid.head()

        df_covid["Año"] = df_covid["FECHA_FALLECIMIENTO"].dt.year
        df_covid["Mes"] = df_covid["FECHA_FALLECIMIENTO"].dt.month_name()

        orden_meses = [
            "January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"
        ]
        df_covid["Mes"] = pd.Categorical(
            df_covid["Mes"], 
            categories=orden_meses, 
            ordered=True
        ) 

#REEMPLAZEMOS EL DEPARTAMENTO LIMA METROPOLITANA POR LIMA
        df_covid["DEPARTAMENTO"] = df_covid["DEPARTAMENTO"].replace("LIMA METROPOLITANA", "LIMA")


#SE ENCONTRARON TEXTOS QUE NO CORRESPONDEN EN LA COLUMNA DEPARTAMENTO Y SE ESTAN CORRIGIENDO:

        df_covid.loc[df_covid["UUID"] == 117420, "DEPARTAMENTO"]  = df_covid.loc[df_covid["UUID"] == 117420]["DEPARTAMENTO"].replace("MASCULINO", "TACNA")
        df_covid.loc[df_covid["UUID"] == 15162227, "DEPARTAMENTO"]  = df_covid.loc[df_covid["UUID"] ==15162227]["DEPARTAMENTO"].replace("MASCULINO", "HUANCAVELICA")

        

        df_covid = df_covid.sort_values(by=["Año", "Mes"])
        df_covid = df_covid.reset_index(drop=True)

        return df_covid
    except FileNotFoundError:
        raise FileNotFoundError("El archivo no se encontró. Por favor revisar la ruta.")
    
    except Exception as e:
        raise Exception(f"Error al cargar los datos: {e}")


