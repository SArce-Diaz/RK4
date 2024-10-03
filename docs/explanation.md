## Método Runge-Kutta de orden 4 (RK4)

En general, un modelo dinámico intenta resolver la trayectoria temporal de alguna cantidad física como función de algún generador dinámico; este último usualmente representado de forma funcional.

En algunos casos, podemos modelar la dinámica de un estado genérico $y$ mediante la ecuación dinámica
\begin{equation}
\frac{dy}{dt} = f(t, y),
\end{equation}
sujeta a la condición inicial
\begin{equation}
y(t_0) = y_0.
\end{equation}

En esta notación, $y$ corresponde a un estado del sistema. Este estado puede ser representado mediante diferentes objetos matemáticos: desde cantidades escalares hasta matrices que representan cierto operador lineal. En la ecuación anterior, $t$ corresponde a la variable temporal.

El problema dinámico descrito anteriormente es usualmente conocido en el campo de las matemáticas aplicadas como **problema de condición inicial**. 


El método Runge-Kutta de orden 4 (RK4) sirve para estimar la solución a un punto temporal $y_n$.
Tenemos: 

\begin{aligned}
    y_{n+1} &= y_n + \frac{1}{6} \left(k_1 + 2k_2 + 2k_3 + k_4\right) \quad \\
    k_1 &= h f(t_n, y_n) \quad \\
    k_2 &= h f\left(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right)\quad \\
    k_3 &= h f\left(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right)\quad \\
    k_4 &= h f\left(t_n + h, y_n k_3\right) \quad \\
\end{aligned}

donde $\textit{h}$ corresponde al espaciamiento temporal.
