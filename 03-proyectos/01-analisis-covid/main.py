import limpieza
import reportes

def main():

    df_covid = limpieza.cargar_datos()

    Mensaje = (
    "\n=====================================================================\n"
    "Hola! bienvenido al reporte de consultas COVID 2020-2024 PERÚ:\n"
    "En este espacio podrás consultar reporte historico, demografia, por género, por departamento, sobre los fallecidos.\n"
    "Si quieres consultar alguno de estos reportes, solo debes escoger uno de ellos ingresando el número:\n"
    "Que reporte quieres consultar:\n"
    "\n"
    "1. Reporte Histórico Fallecidos.\n"
    "2. Reporte Demográfico Fallecidos.\n"
    "3. Reporte Mapa de calor Fallecidos por Departamento. \n"
    "4. Reporte Fallecido por Género. \n"
    "5. Reporte Fallecidos por Departamento.\n"
)
    print(Mensaje)

    dict_reportes = {
        1: ["Ingrese el año que quieres consultar, si quieres ver todos, ingresa 'Todos': ",reportes.Reporte_por_año_mes],
        2: ["Ingrese el año que quieres consultar, si quieres ver todos, ingresa 'Todos': ", reportes.Reporte_demografico],
        3: ["Ingrese el año que quieres consultar: ", reportes.Reporte_mapa_calor_fallecidos_por_departamento],
        4: ["Ingrese el año que quieres consultar, si quieres ver todos, ingresa 'Todos': ", reportes.Reporte_by_genero],
        5: ["Ingrese el año que quieres consultar: ", reportes.Reporte_by_departamento]
    }

    while True:

        ingrese_el_numero = input("Ingrese el número del reporte que quieres consultar: ")
        
        if not ingrese_el_numero.isdigit():
            print("============WARNING=============\n Debes ingresar un número válido. Inténtalo de nuevo.")
            print(Mensaje)
            continue
        try:

            if dict_reportes.get(int(ingrese_el_numero)):                
                ingresar_consulta = dict_reportes[int(ingrese_el_numero)][0]
                ejecutar_funcion_reporte = dict_reportes[int(ingrese_el_numero)][1]

                ingrese_el_año = input(ingresar_consulta) 
                mensaje = ejecutar_funcion_reporte(df_covid, ingrese_el_año)
                print(mensaje) 
            else:
                print("============WARNING=============\n Debes ingresar un número que referencie al reporte.")
                print(Mensaje)
                continue

            continuar = input("Deseas continuar Si/No: ")
            if continuar.upper() == "NO":
                break
            else:                    
                print(Mensaje)

        except ValueError as e:
            raise ValueError(f"Error al cargar los datos: {e}")


if __name__ == "__main__":
    main()
