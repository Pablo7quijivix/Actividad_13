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
                    'carrera_programa':carrera_programa
                }
                print(f"==DATOS DEL ESTUDIANTE GUARDADOS EXITOSAMENTE===")


            case "2":#opcion 2, agregar curso con nota
                while True:
                    id_buscado= input(f"===INGRESE EL ID DEL ESTUDIANTE===: ")
                    id_buscado2 = id_buscado.len()
                    if id_buscado2 == 7:
                        print(f"__ESTUDIANTE ENCONTRADO__")
                        break
                    else:
                        print(f"_____ID NO ENCONTRADO, INTENTELO DE NUEVO_____")
                nombre_curso = input(f"===INGRESE EL NOMBRE DEL CURSO===: ")
                nota_final = input(f"===INGRESE NOTA FINAL DEL CURSO (0-100 )===: ")
                while True:
                    if  0 <=nota_final<= 100:
                        print(f"_____NOTA GUARDADA CORRECTAMENTE_____)")
                        #el break lo colocamos en la parte del if, ya que si verifica la nota dentro del rango
                        # ya no hay necesidad de ir al "else"
                        break
                    else:
                        # MUESTRA UN MENSAJE QUE DEBE INGREASER UNA NOTA CORRECTA
                        print(f"=== INGRESE UNA NOTA CORRECTA (0-100) ===")
                # le asignamos el nombre del curso y la nota final al estudiante correspondiente
                # a traves de una clave "id" y su valor "name" que es un clave que el valor es tanto el curso como la nota
                #uso de diccionario anidado.
                if id_buscado in estudiantes:
                    # ejemplo: '1578125':Pablo Quijivix
                    estudiantes[id] = {
                        'name':name
                        'nombre_curso': nombre_curso,
                        'nota_final': nota_final
                    }



            case "3": #consultar estudiante











