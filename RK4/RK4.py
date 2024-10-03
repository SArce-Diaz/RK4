#!/usr/bin/env python

import numpy as np

def dyn_generator(oper, state):
    """Generador de dinámica temporal para un estado genérico.

    Examples:
        >>> import numpy as np
        >>> oper = np.array([[0, 1], [1, 0]])  # Operador
        >>> state = np.array([[1, 0], [0, 0]]) # Estado inicial
        >>> dyn_generator(oper, state)


    Args:
        oper (np.array): Matriz que representa el operador lineal.
        state (np.array): Matriz que representa el estado actual del sistema.

    Returns:
        (np.array): Retorna el cambio del estado respecto al tiempo debido al operador.
    """

def rk4(func, oper, state, h):
    """Método de integración Runge-Kutta de orden 4 para resolver un problema de valor inicial.

    Examples:
        >>> import numpy as np
        >>> rk4(dyn_generator, np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]), 0.1)

    Args:
        func (callable): Función que representa la ecuación diferencial.
        oper (np.array): Matriz que representa el operador lineal.
        state (np.array): Matriz que representa el estado actual del sistema.
        h (float): Variable que contiene el espaciamiento temporal.

    Returns:
        (np.array): Retorna el estado después de un paso temporal h 
    """
