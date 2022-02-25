#Funcion que imprime menu principal en pantalla
def menu_principal():
  print("\n\n--- Menu Principal ---")
  print("Seleccione opción:")
  print("1. Agregar estudiante")
  print("2. Buscar Estudiante")
  print("3. Modificar Estudiante")
  print("4. Cancelar Materia")
  print("5. Resultado por estudiante")
  print("6. Informe de Grupo")
  print("7. Salir")

#Función para crear un diccionario con la información del estudiante
def agrega_estudiante(identificacion , group):
    print("\n\n--- Agregar estudiante ---")
    nombre = input("Ingrese nombre: ")
    correo = input("Ingrese correo: ")
    telefono = input("Ingrese telefono: ")
    fec_nacimiento = input("Ingrese fecha de nacimiento: ")
    nota1 = float(input("Ingrese Nota 1: ")) #Convierte a número real
    nota2 = float(input("Ingrese Nota 2: ")) #Convierte a número real
    nota3 = float(input("Ingrese Nota 3: ")) #Convierte a número real
    nota4 = float(input("Ingrese Nota 4: ")) #Convierte a número real
    return {"Identificacion":identificacion, "Nombre":nombre, "Correo":correo, "Telefono":telefono, "Fecha de nacimiento":fec_nacimiento, "Nota 1": nota1, "Nota 2": nota2, "Nota 3": nota3, "Nota 4": nota4}

#Funcion para determinar si un estudiante existe en la lista del grupo, basado en la identificacion
def existe_estudiante(group):
  estudiante_existe = False
  identificacion = int(input("Ingrese identificación:")) #Convierte a numero entero
  for i in group:
    if i["Identificacion"] == identificacion:
      estudiante_existe = True
  return estudiante_existe , identificacion

#Funcion para imprimir la informacion de un estudiante, basado en la identificacion
def busca_estudiante(group):
  print("\n\n--- Buscar estudiante ---")
  estudiante_existe , identificacion = existe_estudiante(group)
  if estudiante_existe:    
    for i in group:
      if i["Identificacion"] == identificacion:
        for clave, valor in i.items():
          print(clave,valor)
  else:
      print("Estudiante no existe")

#Funcion para modificar las notas de un estudiante, basado en la identificacion
def modifica_estudiante(group):
  print("\n\n--- Modificar estudiante ---")
  estudiante_existe , identificacion = existe_estudiante(group)
  if estudiante_existe:    
    for i in group:
      if i["Identificacion"] == identificacion:
        i["nota1"]= float(input("Ingrese Nota 1: "))
        i["nota2"] = float(input("Ingrese Nota 2: "))
        i["nota3"] = float(input("Ingrese Nota 3: "))
        i["nota4"] = float(input("Ingrese Nota 4: "))
  else:
      print("Estudiante no existe")
  return group

#Funcion para eliminar un estudiante de la lista de grupo, basado en la identificación
def cancela_estudiante(group):
  print("\n\n--- Cancelar materia ---")
  estudiante_existe , identificacion = existe_estudiante(group)
  if estudiante_existe:    
    for i in range(len(group)):
      if grupo[i]["Identificacion"] == identificacion:
        indice_a_borrar = i
        print(f'El estudiante con identificación {identificacion} ha cancelado la materia.')
    group.pop(indice_a_borrar)
  else:
      print("Estudiante no existe")
  return group

def resultado_estudiante(group):
  print("\n\n--- Resultado Estudiante ---")
  estudiante_existe , identificacion = existe_estudiante(group)
  if estudiante_existe:    
    nota = nota_final(identificacion , group)
    print(f'Resultados del estudiante con identificación {identificacion}')
    print(f'Nota final: {nota}')
    promedio_grupo = nota_grupo(group)
    print(f'La nota promedio del grupo fue: {promedio_grupo}')
    if nota > promedio_grupo:
      print("La nota del estudiante fue mejor que el promedio del grupo")
    else: 
      print("La nota del estudiante fue peor que el promedio del grupo")
    if nota > 3:
      print("El estudiante ganó la materia")
    else: 
      print("El estudiante perdió la materia")
    percentil_estudiante = percentil(identificacion,group)
    print(f'El estudiante está en el percentil {percentil_estudiante}')
  else:
      print("Estudiante no existe")

def nota_final(identificacion , group):
  for i in group:
     if i["Identificacion"] == identificacion:
        nota = (i["Nota 1"] + i["Nota 2"] + i["Nota 3"] + i["Nota 4"]) / 4
  return nota

def nota_grupo(group):
  suma_nota = 0
  for i in group:
    suma_nota += nota_final(i["Identificacion"],group)
  promedio_grupo = suma_nota / len(group)
  return promedio_grupo

def percentil(identificacion, group):
  conteo = 0 #Defino una variable que cuente el estudiante a cuantos estudiantes de su grupo supera
  nota_estudiante = nota_final(identificacion,group)
  for i in grupo:
    nota_a_comparar = nota_final(i["Identificacion"],group)
    if nota_estudiante > nota_a_comparar:
      conteo += 1
  percentil = int(100 * (conteo + 1) / (len(group)))
  return percentil


## Menu principal
## Ciclo para mostrar el menu principal hasta que se escoja la opcion de salir
#grupo=[] #Se crea la lista de grupo
while True:
  menu_principal()
  seleccion = input("\nIngrese opción:")
  if seleccion == "1":
    estudiante_existe , identificacion = existe_estudiante(grupo)
    if estudiante_existe:
      print("Estudiante ya matriculado")
    else:
      grupo.append(agrega_estudiante(identificacion , grupo))
  elif seleccion == "2":
    busca_estudiante(grupo)
  elif seleccion == "3":
    modifica_estudiante(grupo)
  elif seleccion == "4":
    cancela_estudiante(grupo)
  elif seleccion == "5":
    resultado_estudiante(grupo)
  elif seleccion == "6":
    pass
  elif seleccion == "7":
    print("\n\nHasta pronto!")
    break
  else:
    print("--- Opción invalida. ---")