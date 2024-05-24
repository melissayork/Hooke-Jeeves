import numpy as np

def f(arreglo):
    return(arreglo[0]+ 2*arreglo[1] - 7)**2 + (2*arreglo[0] +arreglo[1]-5)**2

punto_inicial=[-5, -2.5]
delta=[0.5, 0.25]

def movimiento_exploratorio(f, punto_inicial, delta):
    xexp = punto_inicial.copy()
    if len(punto_inicial) == len(delta):
        nuevo_punto = []
        for i in range(0, len(punto_inicial)):
            funcion = punto_inicial[i]
            f_suma = punto_inicial[i] + delta[i]
            f_resta = punto_inicial[i] - delta[i]
            xexp[i] = funcion
            evaluar_funcion = f(xexp)
            xexp[i] = f_suma
            evalua_suma = f(xexp)
            xexp[i] = f_resta 
            evalua_resta =f(xexp)
            minimo = min(evaluar_funcion, evalua_suma, evalua_resta)
            if minimo == evaluar_funcion:
                nuevo_punto.append(funcion)
            elif minimo == evalua_suma:
                nuevo_punto.append(f_suma)
            else:
                nuevo_punto.append(f_resta)
        return nuevo_punto
    else:
        print("No son de la misma dimension")


def pattern_move():
    pass

print(movimiento_exploratorio(f, punto_inicial, delta))






