#funcion de bienvenida
def bienvenida():
    return print(f"BIENVENIDO AL\n_SISTEMA DE GESTION ACADEMICA")
bienvenida()

#funcion muestra el menu principal
def menu_principal():
    print(f"__op.1 AGREGAR ESTUDIANTE")
    print(f"__op.2 AGREGAR CURSO CON NOTA")
    print(f"__op.3 CONSULTAR ESTUDIANTE")
    print(f"__op.4 VERIFICAR SI APRUEBA")
    print(f"__op.5 MOSTRAR TODOS LOS ESTUDIANTES")
    print(f"__op.6 SALIR DEL SISTEMA")
menu_principal()

try:
    estudiantes ={}
    while True:
        print(menu_principal)
        opcion_principal = input(f"_ELIGA UNA OPCIÓN (1-6)_: ")
        match opcion_principal:
            case "1": #opcion uno, agregar estudiantes
                while True:
                    # parte de agregar n cantidad de estudiantes
                    cantidad_estudiantes = int(input(f"__¿CUANTOS ESTUDIANTES DESEA INGRESAR?__: "))
                    for i in range(cantidad_estudiantes):
                        print(f"\n__DATOS PARA EL ESTUDIANTE_{i+1}_")
                        id= input(f"___INGRESE EL ID DEL ESTUDIANTES (ÚNICO)___: ")
                        name = input(f"___INGRESE NOMBRE COMPLETO___: ")
                        carrera_programa = input(f"___INGRESE CARRERA O PROGRAMA ACADEMICO___: ")
                    print(f"==DATOS DEL ESTUDIANTE GUARDADO EXITOSAMENTE===")

                    estudiantes[id]={
                        'nombre':name,
                        'cursos':{
                            'nombre_curso':nombre_curso,
                            'nota final': nota_final

                        }

                    }

            case "2": #opcion 2, agregar curso con nota
                id2=(f"===INGRESE EL ID DEL ESTUDIANTE===: ")
                nombre_curso = input(f"===INGRESE EL NOMBRE DEL CURSO===: ")
                nota_final = input(f"===INGRESE NOTA FINAL DEL ESTUIDANTE (0-100 )===: ")








