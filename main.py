# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:38:35 2016

@author: Abraão Állysson dos Santos Honório

Algoritmo
1 - Determinar X(jw)
2 - Determinar H(jw)
3 - Cálcular o y(jw) = X(jw)*h(jw)
4 - Cálcular y(t) = F^-1{y(jw)} 
"""
from numpy import *
from numpy.fft import *
from matplotlib.pyplot import *


    ### Entrada - primeira/segunda questão ####

t0 = -10.0
tf = 10.0
dt = 0.01
N = int((tf-t0)/dt+1)
t = linspace(t0, tf, N)
T = t[1] - t[0]

omega_c = 2*pi
omega = 2*pi*fftfreq(N)/T

    ### Definição do sinal de entrada(1) ->  x(t) = δ(t) ###

x = zeros(N) #inicializando o x com tamanho N e com valores zeros.
x[N/2] = 1.0/dt # definicição de impulso unitário

#DEBUG - código referente o gráfico da função x(t)
"""
figure(funcao x(t))
plot(t, x, lw = 2, c = 'k')
xlabel('t')
ylabel('x(t)')
"""

    ###   Cálculo do sinal de entrada(1) ->  X(t) = δ(t) ### 
X = fft(x) 
#DEBUG - código referente o gráfico da transformada de fourier x(t)

"""
plot(omega, X.real, label = 'parte real')
plot(omega, X.imag, label = 'parte imaginaria')
"""


    ### Cálculo do filtro passa-baixas de segunda ordem H(jw) ######
def H_Pb_so(omega):
    return 1/(1+1j*omega/omega_c) 

H_sis = H_Pb_so(omega)
#calculando a primeira ordem
Y = X*H_sis 
#calculando a segunda ordem
Y = Y*H_sis 
"""
plot(omega, Y.real, label = 'parte real')
plot(omega, Y.imag, label = 'parte imaginaria')
"""

########## Saída y(t) = F^-1{y(jw)} - transformada inversa de Y ##########
y = ifft(Y)
plot(t, x, label = 'entrada')
plot(t, y, label = 'saida')
xlabel = 't'
ylavel = 'sinais'
legend()
