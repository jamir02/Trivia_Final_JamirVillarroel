#Trivia de videojuegos
#Autor: Jamir Villarroel Segovia
#Fecha: 11/09/2022

#La trivia de videojuegos consta de 5 preguntas con 4 alternativas cada una, donde solo una es correcta. Cada pregunta también tiene una respuesta correcta secreta. Tambien presionando "x" tendrán la opción de conseguir una pista en cada pregunta. Al final se adicionan puntos por tu edad y por la ruleta de puntos adicionales. Puedes realizarlo cuantas veces quieras. Finalmente, se mostrara tu puntaje final en cada uno de los intentos, así como tu puntaje acumulado total de todos los intentos como jugador de la trivia. 

#¡Mucha suerte!


#Importamos las librerias a utilizar

import random #Importamos la libreria random
import time # Importamos la libreria time para usar la funcion time.sleep() 
import os #Importamos la libreria os para llamar a la funcion clearConsole()

#Constantes de los colores

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#creamos una variable llamada "puntaje", la cual inicializamos en un numero aletatorio entre 0 y 10

puntaje = random.randint(0,10)

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.


# Almaceno en una lista los resultados finales de los intentos que realiza el usuario en mi trivia

result_intentos =[]

# Alternativas de la pregunta 2
alternativa_2 =["a) Akira Toriyama", "b) Shigeru Miyamoto", "c) Satoshi Tajiri", "d) Junichi Masuda"]

#Alternativas de la pregunta 3

alternativa_3 =["a) Overwatch", "b) Dota 2", "c) Valorant", "d) Path of Exile"]

#Alternativas de la pregunta 4

alternativa_4 =["a) Lionel Messi", "b) Neymar", "c) Kylian Mbappé", "d) Robert Lewandowski"]

#Funcion para limpiar la consola
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)



# Palabras de bienvenida a la trivia
print (GREEN+"Bienvenido a mi trivia sobre videojuegos"+RESET)
print (GREEN+"Pondremos a prueba tus conocimientos"+RESET)


if puntaje == 1:
  print("Comenzarás con",puntaje,"punto")
else:
  print("Comenzarás con",puntaje,"puntos")

# Puntaje maximo
total = puntaje + 200
print("¡Animate a conseguir esos" ,total, "puntos o más!")

#Se solicita ingresar el nombre y edad del jugador

nombre = input(YELLOW+"Ingresa tu nombre: "+RESET)
edad = int(input(YELLOW+"Ingresa tu edad: "+RESET))

# Se brinda instrucciones sobre cómo jugar:
print(GREEN+"\nHola", nombre,"\n\nResponde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n"+RESET)


while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, se repite o realiza un nuevo intento:
  intentos += 1 #numero de intentos
  if intentos > 1: #si el numero de intentos es mayor a 1, se reseteará tu puntaje inicial asignado
    puntaje = random.randint(0,10)
    if puntaje == 1:
      print("\nComenzarás con",puntaje,"punto")
    else:
      print("\nComenzarás con",puntaje,"puntos")
  print(YELLOW+"\nIntento número:"+RESET, intentos)
  input("Presiona Enter para continuar")

  # Cuenta regresiva para el inicio de la trivia
  
  for numero_carga in range(5,0,-1):
    print(numero_carga)
    time.sleep(1)

  
  clearConsole() #Se limpia la consola

  # Pregunta 1
  print (YELLOW+"1) ¿Qué videojuego representa a un gorila arrojando barriles por un tramo de escaleras?" + RESET)
  print ("a) Top Gear")
  print ("b) Tetris")
  print ("c) Pac-Man")
  print ("d) Donkey Kong")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input(YELLOW+"\nIngresa tu respuesta: "+RESET)

  # Si el usuario no ingresa ni a,b,c,d o k, entonces se le enviara un mensaje de que debe ingresar nuevamente una respuesta. Si ingresa x, se le brindara la pista.
  
  while respuesta_1 not in ("a","b","c","d","k"):
    print(nombre, end= "")
    print(", debes responder a, b, c o d.")
    if respuesta_1 == "x":
      print(GREEN+"Pista: Es un videojuego de Nintendo donde aparece Mario, quien debe rescatar a una dama de un gorila\n"+RESET)
    respuesta_1 =input(YELLOW+"Ingresa nuevamente tu respuesta: "+RESET)
  #Si el usuario selecciona la alternativa a:  
  if respuesta_1 == "a":
    puntaje_resta =  random.randint(1,6) #se le asigna un numero aleatorio entre 1 y 6 para restar el puntaje del usuario por seleccionar la opcion incorrecta
    puntaje-= puntaje_resta
    print(RED+"\nRespuesta incorrecta, Top Gear es un videojuego de carreras para la consola Super Nintendo."+RESET )
    #Si el usuario selecciona la alternativa b: 

  elif respuesta_1 == "b":
    puntaje_resta =  random.randint(1,6)
    puntaje-= puntaje_resta
    print(RED+ "\nRespuesta incorrecta, Tetris es un juego de rompecabezas el cual es el más famoso del mundo."+RESET )
    #Si el usuario selecciona la alternativa c: 
  elif respuesta_1 == "c":
    puntaje_resta =  random.randint(1,6)
    puntaje-= puntaje_resta
    print(RED+"\nRespuesta incorrecta, Pac-Man consiste en una bola amarilla que suma puntos cuando come aquello que encuentra a su paso, bolitas y diferentes frutas, pero debe esquivar a cuatro fantasmas."+RESET )
    #Si el usuario selecciona la letra k para la respuesta correcta secreta: 
  elif respuesta_1 == "k":
    puntaje+= 30
    print(BLUE+"\n¡Respuesta secreta correcta!, el videojuego es Donkey Kong, ganaste 30 puntos\n"+RESET)
  #Si el usuario selecciona la alternativa d: 
  else:
    puntaje+= 20
    print(BLUE+"\n¡Respuesta Correcta!"+RESET)
    print(BLUE+"Muy bien", nombre,"!"+RESET)

  # Se muestra el puntaje actual del usuario
  if puntaje == 1:
    print(nombre,"actualmente tienes",puntaje,"punto\n")
  else:
    print(nombre,"actualmente tienes",puntaje,"puntos\n")
  
  # Se espera 5 segundos para la lectura del texto del usuario
  time.sleep(5)
  # Se limpia la consola
  clearConsole()

  #Pregunta 2
  
  print (YELLOW+"2) ¿Quién creo a Mario Bros?" + RESET)
  # Se creo una lista con las alternativas de la pregunta 2, por lo que se imprima cada alternativa con un for
  
  for element in alternativa_2:
    print(element)
  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input(YELLOW+"\nIngresa tu respuesta: "+RESET)
  # Si el usuario no ingresa ni a,b,c,d o l, entonces se le enviara un mensaje de que debe ingresar nuevamente una respuesta. Si ingresa x, se le brindara la pista.
  while respuesta_2 not in ("a","b","c","d","l"):
    print(nombre, end= "") # se usa el end = "" para evitar el \n automatico del print
    print(", debes responder a, b, c o d.")
    if respuesta_2 == "x": # Pista
      print(GREEN+"Pista: Es considerado el padre de los videojuegos modernos por haber creado algunas de las franquicias más influyentes de la industria\n"+RESET)
    respuesta_2 =input(YELLOW+"Ingresa nuevamente tu respuesta: "+RESET)
    
  if respuesta_2 == "a":
    puntaje_resta =  random.randint(1,6)#se le asigna un numero aleatorio entre 1 y 6 para restar el puntaje del usuario por seleccionar la opcion incorrecta
    puntaje-= puntaje_resta
    print(RED+"\nRespuesta incorrecta, Akira Toriyama es un mangaka y diseñador de personajes japonés conocido por ser creador de la obra Dragon Ball."+RESET )
  elif respuesta_2 == "d":
    puntaje_resta =  random.randint(1,6)
    puntaje-= puntaje_resta
    print(RED+ "\nRespuesta incorrecta, Junichi Masuda es un compositor, director, desarrollador, productor y programador de videojuegos japonés, conocido principalmente por sus trabajos en la serie de videojuegos Pokémon."+RESET )
  elif respuesta_2 == "c":
    puntaje_resta =  random.randint(1,6)
    puntaje-= puntaje_resta
    print(RED+"\nRespuesta incorrecta, Satoshi Tajiri es un diseñador de videojuegos japonés, creador de Pocket Monsters (Pokémon)."+RESET )
  elif respuesta_2 == "l":
    puntaje+= 30 #se suma 30 puntos al puntaje total por encontrar la respuesta correcta secreta
    print(BLUE+"\n¡Respuesta secreta correcta!, el creador de Mario Bros es Shigeru Miyamoto, ganaste 30 puntos\n"+RESET)
  
  else:
    
    puntaje+= 20 #respuesta correcta se le suma 20 puntos
    print(BLUE+"\n¡Respuesta Correcta!"+RESET) # Se le felicita al jugador
    print(BLUE+"Muy bien", nombre,"!"+RESET)
  #Se le hace saber al jugador sobre su puntaje actual
  if puntaje == 1:
    print(nombre,"actualmente tienes",puntaje,"punto\n")
  else:
    print(nombre,"actualmente tienes",puntaje,"puntos\n")
  # Se espera 5 segundos para la lectura del texto del usuario
  time.sleep(5)
  #Se limpia la consola
  clearConsole()
  
  
  
    #Pregunta 3
  
  print (YELLOW+"3) ¿Cuál de los siguiente juegos pertenece a la compañía de Riot Games?" + RESET)
  for element in alternativa_3:
    print(element)
  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input(YELLOW+"\nIngresa tu respuesta: "+RESET)
  
  while respuesta_3 not in ("a","b","c","d","m"):
    print(nombre, end= "")
    
    print(", debes responder a, b, c o d.")
    if respuesta_3 == "x":
      print(GREEN+"Pista: Es un juego shooter en primera persona multijugador gratuito.\n"+RESET)
    respuesta_3 =input(YELLOW+"Ingresa nuevamente tu respuesta: "+RESET)
    
  if respuesta_3 == "a":
    puntaje_resta =  random.randint(1,6)
    puntaje-= puntaje_resta
    print(RED+"\nRespuesta incorrecta, Overwatch fue desarrollado por la empresa Blizzard Entertainment"+RESET )
  elif respuesta_3 == "b":
    puntaje_resta =  random.randint(1,6)
    puntaje-= puntaje_resta
    print(RED+ "\nRespuesta incorrecta, Dota 2 fue creado y desarrollado por la empresa Valve Corporation."+RESET )
  elif respuesta_3 == "d":
    puntaje_resta =  random.randint(1,6)
    puntaje-= puntaje_resta
    print(RED+"\nRespuesta incorrecta, Path of Exile fue desarrollado por Grinding Gear Games."+RESET )
  elif respuesta_3 == "m":
    puntaje+= 30
    print(BLUE+"\n¡Respuesta secreta correcta!, Valorant pertenece a la empresa de Riot Games, ganaste 30 puntos\n"+RESET)
  
  else:
    # Se añade 20 puntos por respuesta correcta
    puntaje+= 20
    print(BLUE+"\n¡Respuesta Correcta!"+RESET)
    print(BLUE+"Muy bien", nombre,"!"+RESET)
  
  if puntaje == 1:
    print(nombre,"actualmente tienes",puntaje,"punto\n")
  else:
    print(nombre,"actualmente tienes",puntaje,"puntos\n")
  # Se espera 5 segundos para la lectura del texto del usuario
  time.sleep(5)
  #Se limpia la consola
  clearConsole()

      #Pregunta 4
  
  print (YELLOW+"4) ¿Quién está en la portada del videojuego FIFA 2021?" + RESET)
  for element in alternativa_4:
    print(element)
  # Almacenamos la respuesta del usuario en la variable "respuesta_4"
  respuesta_4 = input(YELLOW+"\nIngresa tu respuesta: "+RESET)
  
  while respuesta_4 not in ("a","b","c","d","n"):
    print(nombre, end= "")
    
    print(", debes responder a, b, c o d.")
    if respuesta_4 == "x":
      print(GREEN+"Pista: Tiene el numero 7 en la camiseta del Paris Saint Germain.\n"+RESET)
    respuesta_4 =input(YELLOW+"Ingresa nuevamente tu respuesta: "+RESET)
    
  if respuesta_4 == "a":
    puntaje_resta =  random.randint(1,6)
    puntaje-= puntaje_resta
    print(RED+"\nRespuesta incorrecta, Lionel Messi salio en las portadas del Fifa 13, 14, 15 y 16."+RESET )
  elif respuesta_4 == "b":
    puntaje_resta =  random.randint(1,6)
    puntaje-= puntaje_resta
    print(RED+ "\nRespuesta incorrecta, Neymar es un gran jugador; sin embargo, no ha salido en ninguna portada del videojuego FIFA."+RESET )
  elif respuesta_4 == "d":
    puntaje_resta =  random.randint(1,6)
    puntaje-= puntaje_resta
    print(RED+"\nRespuesta incorrecta, Robert Lewandowski es un gran jugador; sin embargo, no ha salido en ninguna portada del videojuego FIFA."+RESET )
  elif respuesta_4 == "n":
    puntaje+= 30
    print(BLUE+"\n¡Respuesta secreta correcta!, Kylian Mbappé está en la portada del videojuego FIFA 2021, ganaste 30 puntos\n"+RESET)
  
  else:
    
    puntaje+= 20
    print(BLUE+"\n¡Respuesta Correcta!"+RESET)
    print(BLUE+"Muy bien", nombre,"!"+RESET)
  
  if puntaje == 1:
    print(nombre,"actualmente tienes",puntaje,"punto\n")
  else:
    print(nombre,"actualmente tienes",puntaje,"puntos\n")
  # Se espera 5 segundos para la lectura del texto del usuario
  time.sleep(5)
  # Se limpia la consola
  clearConsole()
  
  # Pregunta 5
  
  print (YELLOW+"5) ¿Qué videojuego de la compañia Rockstar Games es el más esperado actualmente?"+RESET)
  print ("a) Grand Theft Auto VI")
  print ("b) Grand Theft Auto V")
  print ("c) Grand Theft Auto VII")
  print ("d) Grand Theft Auto IV")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_5"
  respuesta_5 = input(YELLOW+"\nIngresa tu respuesta: "+RESET)
  
  while respuesta_5 not in ("a","b","c","d","6"):
    print(nombre, end= "")
    
    print(", debes responder a, b, c o d.")
    if respuesta_5 == "x": #pista
      print(GREEN+"Pista: El ultimo videojuego de Grand Theft Auto lanzado por Rockstar Games fue Grand Theft Auto V"+RESET)
    respuesta_5 =input(YELLOW+"Ingresa nuevamente tu respuesta: "+RESET)
    
  if respuesta_5 == "d":
    puntaje = int(puntaje/2) #el puntaje se divide entre 2
    print(RED+"\nRespuesta incorrecta, Grand Theft Auto IV fue lanzado el 29 de abril del 2008. Se ha dividido tu puntaje."+RESET)
    
  elif respuesta_5 == "b":
    puntaje= puntaje -10 #se restan 10 puntos si el usuario escoge la alternativa b
    print(RED+"\nRespuesta incorrecta, Grand Theft Auto V fue lanzado el 17 de setiembre del 2013. Se resto 10 puntos a tu puntaje."+RESET)
  elif respuesta_5 == "c":
    puntaje= puntaje 
    print(RED+"\nRespuesta incorrecta, Grand Theft Auto VII no tiene fecha de lanzamiento, debido a que aun no se encuentra en desarrollo ni se sabe si será lanzado. Se mantiene tu puntaje."+RESET)
  elif respuesta_5 == "6":
    puntaje= puntaje * 2 #Se duplica el puntaje si el usuario descrubre la respuesta secreta correcta
    print(BLUE+"\n¡Respuesta secreta correcta!, el videojuego es Grand Theft Auto VI, se duplico tu puntaje.\n"+RESET)
  
  else:
    
    puntaje+= 20
    print(BLUE+"\n¡Respuesta Correcta!"+RESET)
    print(BLUE+"Muy bien", nombre,"!"+RESET)
  # Se brinda informacion acerca del puntaje del usuario
  if puntaje == 1:
    print(nombre,"actualmente tienes",puntaje,"punto\n")
  else:
    print(nombre,"actualmente tienes",puntaje,"puntos\n")
  
  #Mensaje final de la trivia
  
  # Se añadira mas puntaje adicional por la edad del usuario. Se añadira mas cuanto menos años tenga el jugador
  # Se calcula el puntaje adicional por la edad 
  puntaje_edad = int((119 - edad)/5)
  print(BLUE+"Se añadieron",puntaje_edad, "puntos adicionales por tu edad\n"+RESET)
  puntaje= puntaje + puntaje_edad # Se añade al puntaje total del usuario

  if puntaje == 1:
    print(nombre,"actualmente tienes",puntaje,"punto\n")
  else:
    print(nombre,"actualmente tienes",puntaje,"puntos\n")
  # Se espera 6 segundos para la lectura del texto del usuario
  time.sleep(6)
  # Se limpia la consola
  clearConsole()
    
  #Ruleta de puntaje final
  # Se lanzaran 3 veces el dado, los cuales añadiran puntaje adicional al usuario
  print(GREEN+ "RULETA DE PUNTAJE FINAL")
  print(GREEN+"Es hora de la ruleta de puntaje final adicional. Se lanzara un dado unas 3 veces y aumentara su puntaje final.\n"+RESET)
  time.sleep(3)
  for dados in range(3,0,-1): #se lanzan los dados
  
    dado =random.randint(1,6)
    puntaje = puntaje+dado
    print(BLUE+"Se lanzo el dado: "+RESET,dado)
    print(nombre,"actualmente tienes",puntaje,"puntos\n")
    time.sleep(2)
  
  print(YELLOW+"Gracias",nombre,"por jugar mi trivia, alcanzaste",puntaje,"puntos"+RESET) #agradecimiento por jugar la trivia
  result_intentos.append(puntaje) # se guarda el puntaje final en una lista de puntajes totales de los intentos que haga el usuario
  print(YELLOW+"\n¿Deseas intentar la trivia nuevamente?"+RESET)# se le pregunta al usuario si desea realizar otro intento
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  clearConsole()

  if repetir_trivia != "si":  # != significa "distinto"
    print(GREEN+"\nEspero",nombre, "que lo hayas pasado bien, hasta pronto!\n"+RESET) #mensaje de despedida
    print("Los puntajes de tus intentos fueron los siguientes:\n")
    for numbers in range(0,intentos):
      print("Intento", numbers+1, ":", result_intentos[numbers])
    print(YELLOW+"\nTu puntaje acumulado de todos los intentos es:"+RESET, sum(result_intentos)) # se calcula el puntaje acumulado de los intentos 
    iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.