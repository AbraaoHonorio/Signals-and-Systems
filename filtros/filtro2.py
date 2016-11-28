# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Abraão Állysson dos Santos Honório
"""

from numpy import *
from matplotlib.pyplot import *

omega_ini = -20.0
omega_f = 20.0 
omega = linspace(omega_ini, omega_f,1000)
omega_cpa = 1.0
omega_cpb = 4.0
# O W(omega) de PB tem que ser maior do que W(omega) de PA


def H_pb(omega):
    return 1/(1+1j*omega/omega_cpb)
    
def H_pa(omega):
    return 1j*(omega/omega_cpb)/(1+1j*omega/omega_cpb)

def H_pf(omega):
    return H_pa(omega) * H_pb(omega)
   
figure(1) 
plot(omega, abs(H_pb(omega)), label = 'passa-baixas' )
plot(omega, abs(H_pa(omega)), label = 'passa-altas' )
xlabel('$\\omega$')
ylabel('$|H(j\\omega)|$')
legend()

figure(2)
plot(omega, angle(H_pb(omega)), label = 'passa-baixas' )
plot(omega, angle(H_pa(omega)), label = 'passa-altas' )
xlabel('$\\omega$')
ylabel('angle$(H(j//omega))$')
legend()

figure(3)
plot(omega, angle(H_pf(omega)), label = 'Angle passa-faixa' )
plot(omega, abs(H_pf(omega)), label = 'ABS passa-faixa' )
xlabel('$\\omega$')
ylabel('angle$(H(j//omega))$')
legend()
