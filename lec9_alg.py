import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10**6, 100)
 
def radio_function(m, t):
    dmdt = - k * m
    return dmdt
 
m_0 = 10
k = 1.61 * 10**(-6) # Постоянная распада для Висмута 210

 # Решение дифференциального уравнения функцией odeint
m_t = odeint(radio_function, m_0, t)
 
# Построение решения в виде графика функции
plt.plot(t, m_t[:,0], label='Распад Висмута 210')
plt.xlabel('Период распада, секунды')
plt.ylabel('Функция распада')
plt.title('Радиоактивный распад')
plt.legend()
 
plt.show()

if __name__=='__main__':
    radio_function()