# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:18:39 2016

@author: TanMingjun
"""

import math
import pylab as py
class cannon_trajectory:
    def __init__(self,a):
        self.x = [0.0]
        self.y = [0.0]
        self.dt = 0.01
        self.v = [1800.0]
        self.v_x = 1800*math.cos(a*math.pi/180)
        self.v_y = 1800*math.sin(a*math.pi/180)
    def calculate(self):
        self.vx = [self.v_x]
        self.vy = [self.v_y]
        while self.y[-1] >= 0:
            x_N = self.x[-1] + self.vx[-1] * self.dt
            vx_N = self.vx[-1] - (1-(6.5*(10)**(-3))*self.y[-1]/300)**(2.5)*self.v[-1]*(4*(10)**(-5))*self.vx[-1]*self.dt
            y_N = self.y[-1] + self.vy[-1] * self.dt
            vy_N = self.vy[-1] - 9.8*((6371000/(6371000+self.y[-1]))**2)*self.dt - (1-(6.5*(10)**(-3))*self.y[-1]/300)**(2.5)*self.v[-1]*(4*(10)**(-5))*self.vy[-1]*self.dt
            v_N = math.sqrt(vx_N**2 + vy_N**2)
            self.x.append(x_N)
            self.vx.append(vx_N)
            self.y.append(y_N)
            self.vy.append(vy_N)
            self.v.append(v_N)
        r=-self.y[-2]/self.y[-1]
        xl = (self.x[-2]+r*self.x[-1])/(r+1)
        yl=0
        self.x[-1] = xl
        self.y[-1] = yl
        return(self.x,self.y)
    def show_results(self, color, label):
        py.plot(self.x, self.y,color)
        py.xlabel('x ($m$)')
        py.ylabel('y ($m$)')
        py.show()
A=cannon_trajectory(35)
A.calculate()
A.show_results('b','$35\degree$')
A1=cannon_trajectory(45)
A1.calculate()
A1.show_results('g','$45\degree$')
A2=cannon_trajectory(55)
A2.calculate()
A2.show_results('r','$55\degree$') 
py.title('Unifrom Air Drag')
py.show()