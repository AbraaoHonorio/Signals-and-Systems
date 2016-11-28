# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

@author: Abraão Állysson dos Santos Honório
"""

from numpy import *
from matplotlib.pyplot import *

omega_ini = -20.0
omega_f = 20.0 
omega = linspace(omega_ini, omega_f,1000)
omega_c  = 2.0


def H_pb(omega):
    return 1/(1+1j*omega/omega_c)
    
def H_pa(omega):
    return 1j*(omega/omega_c)/(1+1j*omega/omega_c)
    
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