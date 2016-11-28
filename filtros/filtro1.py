# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Abraão Állysson dos Santos Honório

This is a temporary script file.
"""

from numpy import *
from matplotlib.pyplot import *

omega_ini = -20.0
omega_f = 20.0 
omega = linspace(omega_ini, omega_f,1000)
omega_c  = 2.0


def H(omega):
    return 1/(1+1j*omega/omega_c)
    
figure(1) 
plot(omega, abs(H(omega)))
xlabel('$\\omega$')
ylabel('$|H(j\\omega)|$')

figure(2)
plot(omega, angle(H(omega))) 
xlabel('$\\omega$')
ylabel('angle$(H(j//omega))$')