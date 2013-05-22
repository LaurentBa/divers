#!/usr/bin/env python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

"""
Copyright (c) 2010 BARATTERO Laurent
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


balistik.py - Script de balistique

ref :  
ipython :
    http://ipython.org/
matplotlib : 
    http://matplotlib.org/index.html
numpy :
    http://numpy.scipy.org/
balistique :
    http://fr.wikipedia.org/wiki/Balistique
    http://gilbert.gastebois.pagesperso-orange.fr/java/balistique/theorie_balistique.htm
python :
    http://docs.python.org/3/tutorial/
le decorateur property (je connais ca depuis pas lomptemps, c'est bien pythonique) :
    http://docs.python.org/2/library/functions.html#property

Exemple d'utilisation :

In [1]: ball1 = Trajectoire(vo=10, a=80, yo=2)
In [2]: ball1.affiche()
In [3]: ball1.a = 40
In [4]: ball1.vo = 15
In [5]: ball1.affiche()
In [6]: ball1.draw()

In [7]: ball2 = Trajectoire()
In [8]: ball2.draw()

"""

import numpy as np
import matplotlib.pyplot as plt
import IPython
from pylab import ion
class Trajectoire(object):
    """
        vo = vitesse initial en m/s
        a  = Angle de tir en degres
        g  = Acceleration de la pesanteur
        yo = Hauteur initial de tir en m

        t = Trajectoire()
        t.a =70



    """
    def __init__(self, vo=15, a=60, g=9.81, yo = 1):
        self.vo , self._a, self.g, self.yo = \
        float(vo), float(a), float(g), float(yo)
        self._a = np.radians(a)
        self.color = "r"
    
    

    # accessor pour a la mode python ( voir property au cas ou )
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = np.radians(value)
    

    
    def x_max(self):
        vo, a, g , yo = self.vo , self._a, self.g, self.yo
        x_max = ( vo**2. * np.sin(2.*a) ) / (2.*g)     \
                  + np.sqrt(   ( (vo**2. * np.sin(2.*a))**2.  )    /      (4.*g**2.)     \
                  + (  2.* yo * (vo * np.cos(a))**2.)  / g  )
        return x_max

    def y_max(self):
        vo, a, g , yo = self.vo , self._a, self.g, self.yo
        y_max = ( vo**2 * np.sin(a)**2 )   /   ( 2*g ) + yo
        return y_max

    def temps_de_vol(self):
        vo, a, g , yo = self.vo , self._a, self.g, self.yo
        temps_total = ((vo * np.sin(a) )   / g )  + ( np.sqrt(  (vo*np.sin(a))**2 + 2*g* yo) / g )
        return temps_total

    def equation(self, x):
        vo, a, g , yo = self.vo , self._a, self.g, self.yo
        y =  -( g / ( 2 * (vo * np.cos(a))**2) ) * x**2 + np.tan(a) * x + yo
        return y

    def config_axes_equation(self):
        size_x_max =  self.x_max() + 5./100. * self.x_max()
        size_y_max =  self.y_max() + 5./100. * self.y_max()
        return (size_x_max, size_y_max)

    def matrix_equation(self, precision = 0.1):
        x = np.arange( 0.0, self.x_max(), precision )
        y = self.equation(x)
        return (x, y)

    def draw_equation(self):
        x, y = self.matrix_equation()
        self.gui.draw(x,y)


    def draw(self, precision = 0.1 ):
        size_x_max =  self.x_max() + 5./100. * self.x_max()
        size_y_max =  self.y_max() + 5./100. * self.y_max()

        tab_xj = np.arange( 0.0, size_x_max, precision )
        plt.plot(tab_xj, self.equation(tab_xj), self.color, )

        plt.axis([0, size_x_max, 0, size_y_max])
        plt.figure(1)
        plt.title('Etude balistique du sctroumpfeur de balles')
        plt.grid(True)
        plt.ylabel('hauteur en m')
        plt.xlabel('distance en m')

        plt.show()

    def affiche(self):
        print (
        "**************************************\n" +
        "* Parametre                          *\n" +
        "**************************************\n" +
        "Velocite initial    : " + str(self.vo)+ "\n" +
        "Angle de projection : " + str(np.degrees(self.a)) + "\n" +
        "Gravitation         : " + str(self.g) + "\n" +
        "Hauteur initial     : " + str(self.yo)+ "\n" +
        "**************************************\n" +
        "Temps de vol : " + str(self.temps_de_vol())  + "\n"
        "Hauteur max  : " + str(self.y_max()) + "\n"
        "Portee       : " + str(self.x_max()) + "\n"
        "**************************************\n"
        )

ion()
IPython.embed()


