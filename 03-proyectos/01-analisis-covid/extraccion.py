import pandas as pd
 
def extraccion_fallecidos_por_anio(df_covid, variable_anio):
    df_covid_fallecidos_por_año_mes = (df_covid.groupby(["Año", "Mes"], observed=True)["UUID"]
                                      .count()
                                      .reset_index()
                                      .rename(columns={"UUID": "Fallecidos"})
                                      )
   

    años_unicos = df_covid_fallecidos_por_año_mes["Año"].unique()
    
    if variable_anio != "Todos" :

        if variable_anio.isdigit()  and (int(variable_anio) in años_unicos) :
            df_filtrado = df_covid_fallecidos_por_año_mes[df_covid_fallecidos_por_año_mes["Año"] == int(variable_anio)]
        else:
            return None  
    else:       
        df_filtrado = df_covid_fallecidos_por_año_mes

    return df_filtrado


def extraccion_demografico(df_covid, variable_anio):

    años_unicos = df_covid["Año"].unique()

    if variable_anio != "Todos" :
        if variable_anio.isdigit()  and (int(variable_anio) in años_unicos) :
            df_covid_filtro = df_covid[df_covid["Año"] == int(variable_anio)]
        else:
         return None  
    else:
        df_covid_filtro = df_covid      

    return df_covid_filtro


def extraccion_genero(df_covid, variable_anio):
    
    años_unicos = df_covid["Año"].unique()

    if variable_anio != "Todos" :
        
        if variable_anio.isdigit()  and (int(variable_anio) in años_unicos) :
            df_covid_filtro = df_covid[df_covid["Año"] == int(variable_anio)]
            
            df_covid_filtro = (df_covid_filtro.groupby(["SEXO"])["UUID"]
                                .count()
                                .reset_index()                                
                                )            
            df_covid_filtro.columns = ["Sexo", "Total"]
        else:
         return None 
    else:

        df_covid_filtro =   (df_covid.groupby(["SEXO"])["UUID"]
                                .count()
                                .reset_index()                                
                                )     
        df_covid_filtro.columns = ["Sexo", "Total"]

    return df_covid_filtro


def extraccion_fallecidos_por_departamento_mapa(df_covid, variable_anio):
    años_unicos = df_covid["Año"].unique()

    if variable_anio.isdigit():
        if int(variable_anio) in años_unicos:
            df_covid_filtro = df_covid[df_covid["Año"] == int(variable_anio)]

            df_covid_filtro = (df_covid_filtro.groupby(["DEPARTAMENTO", "Mes"], observed=True)["UUID"]
                                .count() 
                                .unstack()                             
                                )

        else:
            return None 
    else:
        return None
 
    
    return df_covid_filtro

def extraccion_fallecidos_por_departamento(df_covid, variable_anio):

    años_unicos = df_covid["Año"].unique()
    if variable_anio.isdigit():
        if int(variable_anio) in años_unicos:
            df_covid_filtro = df_covid[df_covid["Año"] == int(variable_anio)]
            
            df_covid_filtro = (df_covid_filtro.groupby(["DEPARTAMENTO"], observed=True)["UUID"]
                                .count()                            
                                .reset_index()
                                .rename(columns={"UUID": "Total"})
                                )
        
        else:
            return None 
    else:
        return None
    
    return df_covid_filtro
