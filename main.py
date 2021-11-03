import os, math

os.system("cls")


def comprueba_edad_y_mes (edad:int, mes:int) -> int:
    """ Función que comprueba que la edad del alumno y su mes de nacimiento se encuentren en rango permitido o no

    Args:
        edad (entero): edad del alumno
        mes (entero): mes de nacimiento del alumno

    Returns:
        int: 
            1 si edad está fuera de rango
            0 si tanto edad como mes están dentro de rango
            -1 si mes está fuera de rango
            None para cualquier parametro ilegal
    """

    try:
        # lo convertimos a entero por si nos pasan datos float
        edad = int(edad)
        mes = int(mes)

        if edad<6 or edad>12:
            return 1
        elif mes<1 or mes>12:
            return -1
    
        return 0
    except ValueError:
        return None



def tablas_alumno (edad: int, mes: int) -> tuple:
    """ Función que identifica el rango al que pertenece el alumno según su edad y mes de nacimiento

    Args:
        edad (entero): edad del alumno
        mes (entero): mes de nacimiento del alumno

    Returns:
        tuple: las tablas de multiplicar que le correspoden al alumno
    """

    try:
        par = esPar(mes)
        if edad>=6 and edad<=8:
            if par:
                return (2,4)
            else:
                return (1,3,5)
        elif edad>8 and edad<=10:
            if par:
                return (6,8,10)
            else:
                return (7,9)
                    
        return (11,12,13)
    except TypeError:
        return None



def esPar (mes: int) -> bool:
    """Comprueba si un mes es par o no

    Args:
        mes (entero): mes de nacimiento del alumno

    Returns:
        bool:
            True si el mes es par
            False si el mes no es par o es menor o igual a 0
            None si se le pasa un parámetro ilegal
    """

    try:
        mes = int(mes)
        if mes>=0:
            if mes%2==0:
                return True

        return False
    except ValueError:
        return None



def imprime_tabla(numero: int):
    contador = 1
    while contador <= 10:
        print(f" {numero} x {contador} = {numero*contador}")

        contador += 1



def cabecera ():
    print("***********************************************")
    print("PROGRAMA DE GENERACIÓN DE TABLAS: Antonio Ramos")
    print("-----------------------------------------------")



def genera_tablas(edad: int, mes: int):
    # Imprimimos el rango al que pertenece el alumno en función de su edad
    print(f"Edad: {edad}.",end=" ")
    if edad>=6 and edad<=8:
        print("El alumno está dentro del rango [6-8].")
    elif edad>8 and edad<=10:
        print("El alumno está dentro del rango (8-10].")
    elif edad>10 and edad<=12:
        print("El alumno está dentro del rango (10-12].")


    # Seguido imprimimos el conjunto de tablas que le pertenecen al alumno
    par = esPar(mes) # comprobando si el mes es par o no
    tablas = tablas_alumno(edad,mes)
    if par:
        print("El mes es par.",end="")
    else:
        print("El mes es impar.",end="")

    print(f"Le corresponden las tablas {tablas}.")


    # Imprimimos las tablas de multiplicar recogidas anteriormente
    for t in tablas:
        print(f"TABLA DEL {t}\n" + "*"*13)
        imprime_tabla(t)
    
    print("-"*47 + "\n" + "*"*47)



def main():
    while True:
        try:
            # Solicitamos los datos necesarios referentes al alumno
            edad = int(input("Edad: "))
            mes = int(input("Mes: "))

            print("")

            # Y hacemos la comprobación de si son correctos o no
            result = comprueba_edad_y_mes(edad,mes)

            cabecera()
            if result==1:
                print(f"Edad: {edad} No se contempla esta edad.")
                print("*"*47)
            elif result==-1:
                print(f"Mes: {mes}. El mes es erroneo.")
                print("*"*47)
            else:
                genera_tablas(edad, mes)
                break

            print("\n")
        except ValueError:
            print(" >>> OJO!! Has introducido un dato no numérico.\n")



if __name__=="__main__":
    main()