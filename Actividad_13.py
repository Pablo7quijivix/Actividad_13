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
    estudiantes ={} #ejemoplo de usuario guardado estudiante={'123':Maria Carmen} clave el id y el valor es el nombre
    while True:
        print(menu_principal)
        opcion_principal = input(f"_ELIGA UNA OPCIÓN (1-6)_: ")
        match opcion_principal:
            case "1": #opcion uno, agregar estudiantes
                print(f"\n___DATOS PARA EL ESTUDIANTE___")
                while True:
                    #pedimos que el carnet del usuario tenga unicamente 7 caracteres, para que sea más facil de ingresarlo de nuevo.
                    id= input(f"___INGRESE EL ID DEL ESTUDIANTES (ÚNICO, (UNICAMENTE 7 DIGITOS))___: ")
                    id2 = id.len()
                    if id2 == 7:
                        print(f"__ID GUARDADO EXITOSAMENTE__")
                        break
                    else:
                        print(f"_____ID NO VALIDO, DEBE CONTENER 7 CARACTERES, INTENTELO DE NUEVO_____")

                name = input(f"___INGRESE NOMBRE COMPLETO___: ")
                carrera_programa = input(f"___INGRESE CARRERA O PROGRAMA ACADEMICO___: ")
                #el id se vuelve clave principal y contiene 2 claves que son los valores
                # del nombre estudiante y su carrera vinculado al id
                #ejemplo: '1578125':Pablo Quijivix
                estudiantes[id] ={
                    'nombre':name,
                    'carrera':carrera_programa
                }
                print(f"==DATOS DEL ESTUDIANTE GUARDADOS EXITOSAMENTE===")


            case "2":#opcion 2, agregar curso con nota
                while True:
                    id_buscado= input(f"===INGRESE EL ID DEL ESTUDIANTE===: ")
                    if id_buscado in estudiantes:
                        es_encontrado = estudiantes[id_buscado]
                        print(f"=====ESTUDIANTE ENCONTRADO=====")
                        nombre_curso = input(f"===INGRESE EL NOMBRE DEL CURSO A AGREGAR===: ")
                        while True:
                            nota_final = input(f"===INGRESE NOTA FINAL DEL CURSO DE: {nombre_curso} (0-100 )===: ")
                            if 0 <= nota_final <= 100:
                                print(f"_____NOTA GUARDADA CORRECTAMENTE_____)")
                                # el break lo colocamos en la parte del if, ya que si verifica la nota dentro del rango
                                # ya no hay necesidad de ir al "else"
                                break
                            else:
                                # MUESTRA UN MENSAJE QUE DEBE INGREASER UNA NOTA CORRECTA
                                print(f"=== INGRESE UNA NOTA CORRECTA (0-100) ===")
                print(f"==========CURSO:{nombre_curso} y NOTA DEL MISMO: {nota_final} GURDADAS CON EXITO PARA EL ESTUDIANTE: {es_encontrado}")
                estudiantes[es_encontrado] = {'nombre': name, 'carrera': carrera_programa, 'nuevo_curso': {'curso_nuevo': nombre_curso,'nota_nueva': {'nueva_nota': nota_final}}}


            case "3": #consultar estudiante e imprimir todos sus datos vinculados
                consultar= input("_________INGRESA UN ID PARA CONSULTAR ESTUDIANTE__________: ")
                if consultar in estudiantes:
                    consultando= estudiantes[consultar]
                    print(f"_____NOMBRE DEL ESTUDIANTE:{consultando['nombre']}" )
                    print(f"_____CARRERA O PROGRAMA: {consultando['carrera']}")
                    print(f"_____NOMBRE DEL CURSO: {consultando['nuevo_curso']['curso_nuevo']}")
                    print(f"_____NOTA DEL CURSO DE: {consultando['nuevo_curso']['curso_nuevo']}, ES IGUAL A: {consultando['nuevo_curso']['nota_nueva']['nueva_nota']}")

            case "4":














