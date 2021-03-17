
from tkinter import *
import random
import time
#la face verte est considerer centrale
################################################################## VARIABLES ##############################################################################

(couleur)=['red','blue','yellow','white','orange','green']

# cr est l'abreviation de cube resolu.

# Definition des couleurs
red='red'
orange='orange'
white='white'
green='green'
yellow='yellow'
blue='blue'


# Definition des listes
CC=[]  # Cube en cours (non resolu)
cm1=[] # Cube apres le mouvement 1



# Partie graphique :


a = 800
b = 1900
i = int(a/12)
j = int(a/12)
x = int(a/22.5)
y = int(b/60)


fenetre = Tk()
fenetre.geometry(str(b)+"x"+str(a))
fond = Canvas(fenetre, width=b , heigh=a ,bg='#E4E4E4')
fond.pack(side=LEFT)

##################################################################### FONCTIONS ############################################################################

# Fonction du cube resolue

def CubeResolue() :
    global cr,red,orange,white,green,yellow,blue,CC
    cr=[[['red', 'red', 'red'], ['red', 'red', 'red'], ['red', 'red', 'red']], [['orange', 'orange', 'orange'], ['orange', 'orange', 'orange'], ['orange', 'orange', 'orange']], [['blue', 'blue', 'blue'], ['blue', 'blue', 'blue'], ['blue', 'blue', 'blue']], [['white', 'white', 'white'], ['white', 'white', 'white'], ['white', 'white', 'white']], [['green', 'green', 'green'], ['green', 'green', 'green'], ['green', 'green', 'green']], [['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow']]]
    CC=cr
    AfficheGraphique()
    AfficheGraphique3D ()




def AfficheGraphique ():
    global a,b,x,y

# Creation des faces avec des abreviation F pour face et C pour carre :

    F1C1=fond.create_rectangle(19*i , 1*j , 20*i , 2*j ,  outline='black' , fill=CC [0] [0] [0])
    F1C2=fond.create_rectangle(19*i , 2*j , 20*i , 3*j ,  outline='black' , fill=CC [0] [0] [1])
    F1C3=fond.create_rectangle(19*i , 3*j , 20*i , 4*j ,  outline='black' , fill=CC [0] [0] [2])
    F1C4=fond.create_rectangle(20*i , 1*j , 21*i , 2*j ,  outline='black' , fill=CC [0] [1] [0])
    F1C5=fond.create_rectangle(20*i , 2*j , 21*i , 3*j ,  outline='black' , fill=CC [0] [1] [1])
    F1C6=fond.create_rectangle(20*i , 3*j , 21*i , 4*j ,  outline='black' , fill=CC [0] [1] [2])
    F1C7=fond.create_rectangle(21*i , 1*j , 22*i , 2*j ,  outline='black' , fill=CC [0] [2] [0])
    F1C8=fond.create_rectangle(21*i , 2*j , 22*i , 3*j ,  outline='black' , fill=CC [0] [2] [1])
    F1C9=fond.create_rectangle(21*i , 3*j , 22*i , 4*j ,  outline='black' , fill=CC [0] [2] [2])

# Creation face 2 :
    
    F2C1=fond.create_rectangle(19*i , 7*j , 20*i , 8*j  , outline='black' , fill=CC [1] [0] [0])
    F2C2=fond.create_rectangle(19*i , 8*j , 20*i , 9*j  , outline='black' , fill=CC [1] [0] [1])
    F2C3=fond.create_rectangle(19*i , 9*j , 20*i , 10*j , outline='black' , fill=CC [1] [0] [2])
    F2C4=fond.create_rectangle(20*i , 7*j , 21*i , 8*j  , outline='black' , fill=CC [1] [1] [0])
    F2C5=fond.create_rectangle(20*i , 8*j , 21*i , 9*j  , outline='black' , fill=CC [1] [1] [1])
    F2C6=fond.create_rectangle(20*i , 9*j , 21*i , 10*j , outline='black' , fill=CC [1] [1] [2])
    F2C7=fond.create_rectangle(21*i , 7*j , 22*i , 8*j  , outline='black' , fill=CC [1] [2] [0])
    F2C8=fond.create_rectangle(21*i , 8*j , 22*i , 9*j  , outline='black' , fill=CC [1] [2] [1])
    F2C9=fond.create_rectangle(21*i , 9*j , 22*i , 10*j , outline='black' , fill=CC [1] [2] [2])

# Creation face 3 :

    F3C1=fond.create_rectangle(16*i , 4*j , 17*i , 5*j ,  outline='black' , fill=CC [2] [0] [0])
    F3C2=fond.create_rectangle(16*i , 5*j , 17*i , 6*j ,  outline='black' , fill=CC [2] [0] [1])
    F3C3=fond.create_rectangle(16*i , 6*j , 17*i , 7*j ,  outline='black' , fill=CC [2] [0] [2])
    F3C4=fond.create_rectangle(17*i , 4*j , 18*i , 5*j ,  outline='black' , fill=CC [2] [1] [0])
    F3C5=fond.create_rectangle(17*i , 5*j , 18*i , 6*j ,  outline='black' , fill=CC [2] [1] [1])
    F3C6=fond.create_rectangle(17*i , 6*j , 18*i , 7*j ,  outline='black' , fill=CC [2] [1] [2])
    F3C7=fond.create_rectangle(18*i , 4*j , 19*i , 5*j ,  outline='black' , fill=CC [2] [2] [0])
    F3C8=fond.create_rectangle(18*i , 5*j , 19*i , 6*j ,  outline='black' , fill=CC [2] [2] [1])
    F3C9=fond.create_rectangle(18*i , 6*j , 19*i , 7*j ,  outline='black' , fill=CC [2] [2] [2])

# Creation face 4 :

    F4C1=fond.create_rectangle(19*i , 4*j , 20*i , 5*j ,  outline='black' , fill=CC [3] [0] [0])
    F4C2=fond.create_rectangle(19*i , 5*j , 20*i , 6*j ,  outline='black' , fill=CC [3] [0] [1])
    F4C3=fond.create_rectangle(19*i , 6*j , 20*i , 7*j ,  outline='black' , fill=CC [3] [0] [2])
    F4C4=fond.create_rectangle(20*i , 4*j , 21*i , 5*j ,  outline='black' , fill=CC [3] [1] [0])
    F4C5=fond.create_rectangle(20*i , 5*j , 21*i , 6*j ,  outline='black' , fill=CC [3] [1] [1])
    F4C6=fond.create_rectangle(20*i , 6*j , 21*i , 7*j ,  outline='black' , fill=CC [3] [1] [2])
    F4C7=fond.create_rectangle(21*i , 4*j , 22*i , 5*j ,  outline='black' , fill=CC [3] [2] [0])
    F4C8=fond.create_rectangle(21*i , 5*j , 22*i , 6*j ,  outline='black' , fill=CC [3] [2] [1])
    F4C9=fond.create_rectangle(21*i , 6*j , 22*i , 7*j ,  outline='black' , fill=CC [3] [2] [2])

# Creation face 5 :

    F5C1=fond.create_rectangle(22*i , 4*j , 23*i , 5*j ,  outline='black' , fill=CC [4] [0] [0])
    F5C2=fond.create_rectangle(22*i , 5*j , 23*i , 6*j ,  outline='black' , fill=CC [4] [0] [1])
    F5C3=fond.create_rectangle(22*i , 6*j , 23*i , 7*j ,  outline='black' , fill=CC [4] [0] [2])
    F5C4=fond.create_rectangle(23*i , 4*j , 24*i , 5*j ,  outline='black' , fill=CC [4] [1] [0])
    F5C5=fond.create_rectangle(23*i , 5*j , 24*i , 6*j ,  outline='black' , fill=CC [4] [1] [1])
    F5C6=fond.create_rectangle(23*i , 6*j , 24*i , 7*j ,  outline='black' , fill=CC [4] [1] [2])
    F5C7=fond.create_rectangle(24*i , 4*j , 25*i , 5*j , outline='black' , fill=CC [4] [2] [0])
    F5C8=fond.create_rectangle(24*i , 5*j , 25*i , 6*j , outline='black' , fill=CC [4] [2] [1])
    F5C9=fond.create_rectangle(24*i , 6*j , 25*i , 7*j , outline='black' , fill=CC [4] [2] [2])
    
# Creation face 6 :

    F6C1=fond.create_rectangle(25*i , 4*j , 26*i , 5*j ,outline='black' , fill=CC [5] [0] [0])
    F6C2=fond.create_rectangle(25*i , 5*j , 26*i , 6*j ,outline='black' , fill=CC [5] [0] [1])
    F6C3=fond.create_rectangle(25*i , 6*j , 26*i , 7*j ,outline='black' , fill=CC [5] [0] [2])
    F6C4=fond.create_rectangle(26*i , 4*j , 27*i , 5*j ,outline='black' , fill=CC [5] [1] [0])
    F6C5=fond.create_rectangle(26*i , 5*j , 27*i , 6*j ,outline='black' , fill=CC [5] [1] [1])
    F6C6=fond.create_rectangle(26*i , 6*j , 27*i , 7*j ,outline='black' , fill=CC [5] [1] [2])
    F6C7=fond.create_rectangle(27*i , 4*j , 28*i , 5*j ,outline='black' , fill=CC [5] [2] [0])
    F6C8=fond.create_rectangle(27*i , 5*j , 28*i , 6*j ,outline='black' , fill=CC [5] [2] [1])
    F6C9=fond.create_rectangle(27*i , 6*j , 28*i , 7*j ,outline='black' , fill=CC [5] [2] [2])
# Fonction permettant l'affichage du Rubik's Cube en 3D

def AfficheGraphique3D ():
    
    c = 2*x
    d = 2*y
    
# Creation des faces avec des abreviation F pour face et C pour carre :

    F1C1=fond.create_polygon(c+4.32*x ,  d+2*y ,     c+2.66*x ,  d+2.66*y , c+1*x ,    d+2*y ,    c+2.66*x ,    d+1.34*y  ,outline='black' ,  fill=CC [0] [0] [0])
    F1C2=fond.create_polygon(c+5.98*x ,  d+2.66*y ,  c+4.32*x ,  d+3.33*y , c+2.66*x , d+2.66*y , c+4.32*x ,    d+2*y     ,outline='black' ,  fill=CC [0] [0] [1])
    F1C3=fond.create_polygon(c+7.66*x ,  d+3.34*y ,  c+6*x ,     d+4*y ,    c+4.32*x , d+3.33*y , c+5.98*x ,    d+2.66*y  ,outline='black' ,  fill=CC [0] [0] [2])
    F1C4=fond.create_polygon(c+5.98*x ,  d+1.34*y ,  c+4.32*x ,  d+2*y ,    c+2.66*x , d+1.34*y , c+4.32*x ,    d+0.66*y  ,outline='black' ,  fill=CC [0] [1] [0])
    F1C5=fond.create_polygon(c+7.66*x ,  d+2*y ,     c+5.98*x ,  d+2.66*y , c+4.32*x , d+2*y ,    c+5.98*x ,    d+1.34*y  ,outline='black' ,  fill=CC [0] [1] [1])
    F1C6=fond.create_polygon(c+9.32*x ,  d+2.67*y ,  c+7.66*x ,  d+3.34*y , c+5.98*x , d+2.66*y , c+7.64*x ,    d+2*y     ,outline='black' ,  fill=CC [0] [1] [2])
    F1C7=fond.create_polygon(c+7.66*x ,  d+0.66*y ,  c+5.98*x ,  d+1.34*y , c+4.32*x , d+0.67*y , c+6*x ,       d+0*y     ,outline='black' ,  fill=CC [0] [2] [0])
    F1C8=fond.create_polygon(c+9.32*x ,  d+1.33*y ,  c+7.64*x ,  d+2*y ,    c+5.98*x , d+1.34*y , c+7.66*x ,    d+0.66*y  ,outline='black' ,  fill=CC [0] [2] [1])
    F1C9=fond.create_polygon(c+11*x ,    d+2*y ,     c+9.32*x ,  d+2.67*y , c+7.64*x , d+2*y ,    c+9.32*x ,    d+1.33*y  ,outline='black' ,  fill=CC [0] [2] [2])

# Creation face 2 :
    F2C1=fond.create_polygon(c+22*x ,    d+2*y ,     c+20.32*x , d+2.67*y , c+18.64*x , d+2*y ,    c+20.32*x ,  d+1.33*y  ,outline='black' ,  fill=CC [4] [2] [0])
    F2C2=fond.create_polygon(c+20.32*x , d+2.67*y ,  c+18.66*x , d+3.34*y , c+16.98*x , d+2.66*y , c+18.64*x ,  d+2*y     ,outline='black' ,  fill=CC [4] [2] [1])
    F2C3=fond.create_polygon(c+18.66*x , d+3.34*y ,  c+17*x ,    d+4*y ,    c+15.32*x , d+3.33*y , c+16.98*x ,  d+2.66*y  ,outline='black' ,  fill=CC [4] [2] [2])
    F2C4=fond.create_polygon(c+20.32*x , d+1.33*y ,  c+18.64*x , d+2*y ,    c+16.98*x , d+1.34*y , c+18.66*x ,  d+0.66*y  ,outline='black' ,  fill=CC [4] [1] [0])
    F2C5=fond.create_polygon(c+18.66*x , d+2*y ,     c+16.98*x , d+2.66*y , c+15.32*x , d+2*y ,    c+16.98*x ,  d+1.34*y  ,outline='black' ,  fill=CC [4] [1] [1])
    F2C6=fond.create_polygon(c+16.98*x , d+2.66*y ,  c+15.32*x , d+3.33*y , c+13.66*x , d+2.66*y , c+15.32*x ,  d+2*y     ,outline='black' ,  fill=CC [4] [1] [2])
    F2C7=fond.create_polygon(c+18.66*x , d+0.66*y ,  c+16.98*x , d+1.34*y , c+15.32*x , d+0.67*y , c+17*x ,     d+0*y     ,outline='black' ,  fill=CC [4] [0] [0])
    F2C8=fond.create_polygon(c+16.98*x , d+1.34*y ,  c+15.32*x , d+2*y ,    c+13.66*x , d+1.34*y , c+15.32*x ,  d+0.67*y  ,outline='black' ,  fill=CC [4] [0] [1])
    F2C9=fond.create_polygon(c+15.32*x , d+2*y ,     c+13.66*x , d+2.66*y , c+12*x ,    d+2*y ,    c+13.66*x ,  d+1.34*y  ,outline='black' ,  fill=CC [4] [0] [2])    


# Creation face 3 :

    F3C1=fond.create_polygon(c+2.66*x ,  d+5.03*y ,  c+1*x ,     d+4.36*y ,  c+1*x ,    d+2*y ,    c+2.66*x ,   d+2.66*y  ,outline='black' ,  fill=CC [2] [0] [0])
    F3C2=fond.create_polygon(c+2.66*x ,  d+7.36*y ,  c+1*x ,     d+6.66*y ,  c+1*x ,    d+4.36*y , c+2.66*x ,   d+5.03*y  ,outline='black' ,  fill=CC [2] [0] [1])
    F3C3=fond.create_polygon(c+2.66*x ,  d+9.66*y ,  c+1*x ,     d+9*y ,     c+1*x ,    d+6.66*y , c+2.66*x ,   d+7.32*y  ,outline='black' ,  fill=CC [2] [0] [2])
    F3C4=fond.create_polygon(c+4.32*x ,  d+5.69*y ,  c+2.66*x ,  d+5.03*y ,  c+2.66*x , d+2.66*y , c+4.32*x ,   d+3.33*y  ,outline='black' ,  fill=CC [2] [1] [0])
    F3C5=fond.create_polygon(c+4.32*x ,  d+8.02*y ,  c+2.66*x ,  d+7.36*y ,  c+2.66*x , d+5.03*y , c+4.32*x ,   d+5.69*y  ,outline='black' ,  fill=CC [2] [1] [1])
    F3C6=fond.create_polygon(c+4.32*x ,  d+10.33*y , c+2.66*x ,  d+9.66*y ,  c+2.66*x , d+7.36*y , c+4.32*x ,   d+8.02*y  ,outline='black' ,  fill=CC [2] [1] [2])
    F3C7=fond.create_polygon(c+6*x ,     d+6.33*y ,  c+4.32*x ,  d+5.69*y ,  c+4.32*x , d+3.33*y , c+6*x ,      d+4*y     ,outline='black' ,  fill=CC [2] [2] [0])
    F3C8=fond.create_polygon(c+6*x ,     d+8.66*y ,  c+4.32*x ,  d+8.02*y ,  c+4.32*x , d+5.69*y , c+6*x ,      d+6.33*y  ,outline='black' ,  fill=CC [2] [2] [1])
    F3C9=fond.create_polygon(c+6*x ,     d+11*y ,    c+4.32*x ,  d+10.33*y , c+4.32*x , d+8.02*y , c+6*x ,      d+8.66*y  ,outline='black' ,  fill=CC [2] [2] [2])      

# Creation face 4 :

    F4C1=fond.create_polygon(c+7.66*x ,  d+5.69*y ,  c+6*x ,     d+6.33*y ,   c+6*x ,    d+4*y ,    c+7.66*x ,  d+3.33*y  ,outline='black' ,  fill=CC [3] [0] [0])
    F4C2=fond.create_polygon(c+7.66*x ,  d+8.02*y ,  c+6*x ,     d+8.66*y ,   c+6*x,     d+6.33*y , c+7.66*x,   d+5.69*y  ,outline='black' ,  fill=CC [3] [0] [1])
    F4C3=fond.create_polygon(c+7.66*x ,  d+10.33*y , c+6*x ,     d+11*y ,     c+6*x ,    d+8.66*y , c+7.66*x ,  d+8.02*y  ,outline='black' ,  fill=CC [3] [0] [2])
    F4C4=fond.create_polygon(c+9.32*x ,  d+5.04*y ,  c+7.66*x ,  d+5.7*y ,    c+7.66*x , d+3.34*y , c+9.32*x ,  d+2.67*y  ,outline='black' ,  fill=CC [3] [1] [0])
    F4C5=fond.create_polygon(c+9.32*x ,  d+7.34*y ,  c+7.66*x ,  d+8*y ,      c+7.66*x , d+5.7*y ,  c+9.32*x ,  d+5.04*y  ,outline='black' ,  fill=CC [3] [1] [1])
    F4C6=fond.create_polygon(c+9.32*x ,  d+9.67*y ,  c+7.66*x ,  d+10.33*y ,  c+7.66*x , d+8*y ,    c+9.32*x ,  d+7.33*y  ,outline='black' ,  fill=CC [3] [1] [2])
    F4C7=fond.create_polygon(c+11*x ,    d+4.36*y ,  c+9.32*x ,  d+5.04*y ,   c+9.32*x , d+2.67*y , c+11*x ,    d+2*y     ,outline='black' ,  fill=CC [3] [2] [0])
    F4C8=fond.create_polygon(c+11*x ,    d+6.67*y ,  c+9.32*x ,  d+7.34*y ,   c+9.32*x , d+5.04*y , c+11*x ,    d+4.36*y  ,outline='black' ,  fill=CC [3] [2] [1])
    F4C9=fond.create_polygon(c+11*x ,    d+9*y ,     c+9.32*x ,  d+9.67*y ,   c+9.32*x , d+7.33*y , c+11*x ,    d+6.66*y  ,outline='black' ,  fill=CC [3] [2] [2])
  
# Creation face 5   :

    F5C1=fond.create_polygon(c+18.66*x , d+5.66*y ,  c+17*x ,    d+6.33*y ,  c+17*x ,    d+4*y ,    c+18.66*x , d+3.33*y  ,outline='black' ,  fill=CC [5] [0] [2])
    F5C2=fond.create_polygon(c+18.66*x , d+8*y ,     c+17*x ,    d+8.66*y ,  c+17*x ,    d+6.33*y , c+18.66*x , d+5.66*y  ,outline='black' ,  fill=CC [5] [1] [2])
    F5C3=fond.create_polygon(c+18.66*x , d+10.33*y , c+17*x ,    d+11*y ,    c+17*x ,    d+8.66*y , c+18.66*x , d+8*y     ,outline='black' ,  fill=CC [5] [2] [2])
    F5C4=fond.create_polygon(c+20.32*x , d+5*y ,     c+18.66*x , d+5.66*y ,  c+18.66*x , d+3.33*y , c+20.32*x , d+2.66*y  ,outline='black' ,  fill=CC [5] [0] [1])
    F5C5=fond.create_polygon(c+20.32*x , d+7.33*y ,  c+18.66*x , d+8*y ,     c+18.66*x , d+5.66*y , c+20.32*x , d+5*y     ,outline='black' ,  fill=CC [5] [1] [1])
    F5C6=fond.create_polygon(c+20.32*x , d+9.66*y ,  c+18.66*x , d+10.33*y , c+18.66*x , d+8*y ,    c+20.32*x , d+7.33*y  ,outline='black' ,  fill=CC [5] [2] [1])
    F5C7=fond.create_polygon(c+22*x ,    d+4.36*y ,  c+20.32*x , d+5*y ,     c+20.32*x , d+2.66*y , c+22*x ,    d+2*y     ,outline='black' ,  fill=CC [5] [0] [0])
    F5C8=fond.create_polygon(c+22*x ,    d+6.66*y ,  c+20.32*x , d+7.33*y ,  c+20.32*x , d+5*y ,    c+22*x ,    d+4.36*y  ,outline='black' ,  fill=CC [5] [1] [0])
    F5C9=fond.create_polygon(c+22*x ,    d+9*y ,     c+20.32*x , d+9.66*y ,  c+20.32*x , d+7.33*y , c+22*x ,    d+6.66*y  ,outline='black' ,  fill=CC [5] [2] [0])
# Creation face 6 :

    F6C1=fond.create_polygon(c+13.66*x , d+5*y ,     c+12*x ,    d+4.36*y ,  c+12*x ,    d+2*y ,    c+13.66*x , d+2.66*y  ,outline='black' ,  fill=CC [1] [2] [0])
    F6C2=fond.create_polygon(c+13.66*x , d+7.32*y ,  c+12*x ,    d+6.66*y ,  c+12*x ,    d+4.36*y , c+13.66*x , d+5*y     ,outline='black' ,  fill=CC [1] [1] [0]) 
    F6C3=fond.create_polygon(c+13.66*x , d+9.66*y ,  c+12*x ,    d+9*y ,     c+12*x ,    d+6.66*y , c+13.66*x , d+7.32*y  ,outline='black' ,  fill=CC [1] [0] [0])
    F6C4=fond.create_polygon(c+15.32*x , d+5.66*y ,  c+13.66*x , d+5*y ,     c+13.66*x , d+2.66*y , c+15.32*x , d+3.33*y  ,outline='black' ,  fill=CC [1] [2] [1])
    F6C5=fond.create_polygon(c+15.32*x , d+8*y ,     c+13.66*x , d+7.32*y ,  c+13.66*x , d+5*y ,    c+15.32*x , d+5.66*y  ,outline='black' ,  fill=CC [1] [1] [1])  
    F6C6=fond.create_polygon(c+15.32*x , d+10.33*y , c+13.66*x , d+9.66*y ,  c+13.66*x , d+7.32*y , c+15.32*x , d+8*y     ,outline='black' ,  fill=CC [1] [0] [1])
    F6C7=fond.create_polygon(c+17*x ,    d+6.33*y ,  c+15.32*x , d+5.66*y ,  c+15.32*x , d+3.33*y , c+17*x ,    d+4*y     ,outline='black' ,  fill=CC [1] [2] [2])
    F6C8=fond.create_polygon(c+17*x ,    d+8.66*y ,  c+15.32*x , d+8*y ,     c+15.32*x , d+5.66*y , c+17*x ,    d+6.33*y  ,outline='black' ,  fill=CC [1] [1] [2])
    F6C9=fond.create_polygon(c+17*x ,    d+11*y ,    c+15.32*x , d+10.33*y , c+15.32*x , d+8*y ,    c+17*x ,    d+8.66*y  ,outline='black' ,  fill=CC [1] [0] [2])

    
# Fonctions definissant les mouvements.

def Opt_Affichage () :
    
    AfficheGraphique ()
    AfficheGraphique3D ()

# Cette fonction effectue un mouvement vers l'avant de la premiere colonne.


def left_prime():
    global CC,cm1
    cm1=[[[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]], 
         [[CC[5][2][2],CC[5][2][1],CC[5][2][0]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][2][0],CC[2][1][0],CC[2][0][0]],[CC[2][2][1],CC[2][1][1],CC[2][0][1]],[CC[2][2][2],CC[2][1][2],CC[2][0][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[0][0][2],CC[0][0][1],CC[0][0][0]]]]

    CC=cm1

    Opt_Affichage ()
    

# Cette fonction effectue un mouvement vers l'arriere de la premiere colonne.
def left():
    global CC,cm2
    
    cm2=[[[CC[5][2][0],CC[5][2][1],CC[5][2][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][2],CC[2][1][2],CC[2][2][2]],[CC[2][0][1],CC[2][1][1],CC[2][2][1]],[CC[2][0][0],CC[2][1][0],CC[2][2][0]]],
         [[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][2][0],CC[4][1][0],CC[4][0][0]],[CC[4][2][1],CC[4][1][1],CC[4][0][1]],[CC[4][2][2],CC[4][1][2],CC[4][0][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[1][0][0],CC[1][0][1],CC[1][0][2]]]]
    CC=cm2

    Opt_Affichage ()
        



# Mvt5 correspond au mouvement vers l'avant de la 3eme colonne.

def right():
    global CC ,cm5
    cm5=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[5][0][2],CC[5][0][1],CC[5][0][0]]],
         [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[4][0][2],CC[4][1][2],CC[4][2][2]],[CC[4][0][1],CC[4][1][1],CC[4][2][1]],[CC[4][0][0],CC[4][1][0],CC[4][2][0]]],
         [[CC[0][2][2],CC[0][2][1],CC[0][2][0]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm5

    Opt_Affichage ()
        

# Mvt6 correspond au mouvement vers l'arriere de la 3eme colonne.
def right_prime():
   global CC,cm6
   cm6=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[5][0][2],CC[5][0][1],CC[5][0][0]]],
        [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
        [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
        [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
        [[CC[4][2][0],CC[4][1][0],CC[4][0][0]],[CC[4][2][1],CC[4][1][1],CC[4][0][1]],[CC[4][2][2],CC[4][1][2],CC[4][0][2]]],
        [[CC[1][2][2],CC[1][2][1],CC[1][2][0]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
   CC=cm6

   Opt_Affichage ()
    
# Mvt7 correspond au mouvement vers la gauche de la 1ere ligne.
def up():
    global CC ,cm7
    cm7=[[[CC[0][0][2],CC[0][1][2],CC[0][2][2]],[CC[0][0][1],CC[0][1][1],CC[0][2][1]],[CC[0][0][0],CC[0][1][0],CC[0][2][0]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[3][0][0],CC[2][0][1],CC[2][0][2]],[CC[3][1][0],CC[2][1][1],CC[2][1][2]],[CC[3][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[4][0][0],CC[3][0][1],CC[3][0][2]],[CC[4][1][0],CC[3][1][1],CC[3][1][2]],[CC[4][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[5][0][0],CC[4][0][1],CC[4][0][2]],[CC[5][1][0],CC[4][1][1],CC[4][1][2]],[CC[5][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[2][0][0],CC[5][0][1],CC[5][0][2]],[CC[2][1][0],CC[5][1][1],CC[5][1][2]],[CC[2][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm7

    Opt_Affichage ()


# Mvt8 correspond au mouvement vers la droite de la 1ere ligne.
def up_prime():
    global CC ,cm8
    cm8=[[[CC[0][2][0],CC[0][1][0],CC[0][0][0]],[CC[0][2][1],CC[0][1][1],CC[0][0][1]],[CC[0][2][2],CC[0][1][2],CC[0][0][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[5][0][0],CC[2][0][1],CC[2][0][2]],[CC[5][1][0],CC[2][1][1],CC[2][1][2]],[CC[5][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[2][0][0],CC[3][0][1],CC[3][0][2]],[CC[2][1][0],CC[3][1][1],CC[3][1][2]],[CC[2][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[3][0][0],CC[4][0][1],CC[4][0][2]],[CC[3][1][0],CC[4][1][1],CC[4][1][2]],[CC[3][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[4][0][0],CC[5][0][1],CC[5][0][2]],[CC[4][1][0],CC[5][1][1],CC[5][1][2]],[CC[4][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm8

    Opt_Affichage ()
        

 

# Mvt 11 correspond au mouvement vers la gauche de la 3eme ligne.
def down_prime():
    global CC ,cm11
    cm11=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][2][0],CC[1][1][0],CC[1][0][0]],[CC[1][2][1],CC[1][1][1],CC[1][0][1]],[CC[1][2][2],CC[1][1][2],CC[1][0][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[3][0][2]],[CC[2][1][0],CC[2][1][1],CC[3][1][2]],[CC[2][2][0],CC[2][2][1],CC[3][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[4][0][2]],[CC[3][1][0],CC[3][1][1],CC[4][1][2]],[CC[3][2][0],CC[3][2][1],CC[4][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[5][0][2]],[CC[4][1][0],CC[4][1][1],CC[5][1][2]],[CC[4][2][0],CC[4][2][1],CC[5][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[2][0][2]],[CC[5][1][0],CC[5][1][1],CC[2][1][2]],[CC[5][2][0],CC[5][2][1],CC[2][2][2]]]]
    CC=cm11

    Opt_Affichage ()
      

# Mvt 12 correspond au mouvement vers la droite de la 3eme ligne.
def down():
    global CC ,cm12
    cm12=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][2],CC[1][1][2],CC[1][2][2]],[CC[1][0][1],CC[1][1][1],CC[1][2][1]],[CC[1][0][0],CC[1][1][0],CC[1][2][0]]],
          [[CC[2][0][0],CC[2][0][1],CC[5][0][2]],[CC[2][1][0],CC[2][1][1],CC[5][1][2]],[CC[2][2][0],CC[2][2][1],CC[5][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[2][0][2]],[CC[3][1][0],CC[3][1][1],CC[2][1][2]],[CC[3][2][0],CC[3][2][1],CC[2][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[3][0][2]],[CC[4][1][0],CC[4][1][1],CC[3][1][2]],[CC[4][2][0],CC[4][2][1],CC[3][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[4][0][2]],[CC[5][1][0],CC[5][1][1],CC[4][1][2]],[CC[5][2][0],CC[5][2][1],CC[4][2][2]]]]
    CC=cm12

    Opt_Affichage ()
     

def back():
    global CC,cm13
    cm13=[[[CC[4][2][0],CC[0][0][1],CC[0][0][2]],[CC[4][2][1],CC[0][1][1],CC[0][1][2]],[CC[4][2][2],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][0],CC[1][0][1],CC[2][0][0]],[CC[1][1][0],CC[1][1][1],CC[2][0][1]],[CC[1][2][0],CC[1][2][1],CC[2][0][2]]],
          [[CC[0][2][0],CC[0][1][0],CC[0][0][0]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[1][2][2],CC[1][1][2],CC[1][0][2]]],
          [[CC[5][0][2],CC[5][1][2],CC[5][2][2]],[CC[5][0][1],CC[5][1][1],CC[5][2][1]],[CC[5][0][0],CC[5][1][0],CC[5][2][0]]]]
    CC=cm13

    Opt_Affichage ()     
        
def back_prime():
    global CC,cm14
    cm14=[[[CC[2][0][2],CC[0][0][1],CC[0][0][2]],[CC[2][0][1],CC[0][1][1],CC[0][1][2]],[CC[2][0][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][0],CC[1][0][1],CC[4][2][2]],[CC[1][1][0],CC[1][1][1],CC[4][2][1]],[CC[1][2][0],CC[1][2][1],CC[4][2][0]]],
          [[CC[1][0][2],CC[1][1][2],CC[1][2][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[0][0][0],CC[0][1][0],CC[0][2][0]]],
          [[CC[5][2][0],CC[5][1][0],CC[5][0][0]],[CC[5][2][1],CC[5][1][1],CC[5][0][1]],[CC[5][2][2],CC[5][1][2],CC[5][0][2]]]]
    CC=cm14

    Opt_Affichage ()
  
        


def front_prime():
    global CC,cm17
    cm17=[[[CC[0][0][0],CC[0][0][1],CC[4][0][0]],[CC[0][1][0],CC[0][1][1],CC[4][0][1]],[CC[0][2][0],CC[0][2][1],CC[4][0][2]]],
          [[CC[2][2][0],CC[1][0][1],CC[1][0][2]],[CC[2][2][1],CC[1][1][1],CC[1][1][2]],[CC[2][2][2],CC[1][2][1],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[0][2][2],CC[0][1][2],CC[0][0][2]]],
          [[CC[3][2][0],CC[3][1][0],CC[3][0][0]],[CC[3][2][1],CC[3][1][1],CC[3][0][1]],[CC[3][2][2],CC[3][1][2],CC[3][0][2]]],
          [[CC[1][2][0],CC[1][1][0],CC[1][0][0]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm17

    Opt_Affichage ()


def front():
    global CC,cm18
    cm18=[[[CC[0][0][0],CC[0][0][1],CC[2][2][2]],[CC[0][1][0],CC[0][1][1],CC[2][2][1]],[CC[0][2][0],CC[0][2][1],CC[2][2][0]]],
          [[CC[4][0][2],CC[1][0][1],CC[1][0][2]],[CC[4][0][1],CC[1][1][1],CC[1][1][2]],[CC[4][0][0],CC[1][2][1],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[1][0][0],CC[1][1][0],CC[1][2][0]]],
          [[CC[3][0][2],CC[3][1][2],CC[3][2][2]],[CC[3][0][1],CC[3][1][1],CC[3][2][1]],[CC[3][0][0],CC[3][1][0],CC[3][2][0]]],
          [[CC[0][0][2],CC[0][1][2],CC[0][2][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm18

    Opt_Affichage ()



def scrambler():

    for x in range(random.randint(10,30)):

        random.choice(liste)()
        #Tk.after(10000, Opt_Affichage)
        

def design ():
    
    print CC 
    

#BOUTONS 




def Boutons():
     
    Bmvt1 = Button(fenetre, text="left_prime", bg= 'red' , font= "Helvetica 12 bold" , command=left_prime )
    Bmvt1_fenetre = fond.create_window(x+1620, 700, window=Bmvt1)

    Bmvt2 = Button(fenetre, text="left", bg= 'red' , font= "Helvetica 12 bold" , command=left )
    Bmvt2_fenetre = fond.create_window(x+1755, 700, window=Bmvt2)



    Bmvt5 = Button(fenetre, text="right", bg= 'red', font= "Helvetica 12 bold"  , command=right )
    Bmvt5_fenetre = fond.create_window(x+270, 700 , window=Bmvt5)
    
    Bmvt6 = Button(fenetre, text="right_prime", bg= 'red', font= "Helvetica 12 bold"  , command=right_prime )
    Bmvt6_fenetre = fond.create_window(x+405, 700 , window=Bmvt6)

    Bmvt7 = Button(fenetre, text="up", bg= 'red', font= "Helvetica 12 bold"  , command=up )
    Bmvt7_fenetre = fond.create_window(x+540, 700, window=Bmvt7)

    Bmvt8 = Button(fenetre, text="up_prime", bg= 'red', font= "Helvetica 12 bold"  , command=up_prime )
    Bmvt8_fenetre = fond.create_window(x+675, 700 , window=Bmvt8)



    Bmvt11 = Button(fenetre, text="down_prime", bg= 'red' , font= "Helvetica 12 bold" , command=down_prime )
    Bmvt11_fenetre = fond.create_window(x+810, 700, window=Bmvt11)

    Bmvt12 = Button(fenetre, text="down", bg= 'red', font= "Helvetica 12 bold"  , command=down )
    Bmvt12_fenetre = fond.create_window(x+945 , 700, window=Bmvt12)

    Bmvt13 = Button(fenetre, text="back", bg= 'red', font= "Helvetica 12 bold"  , command=back )
    Bmvt13_fenetre = fond.create_window(x+1080 , 700, window=Bmvt13)

    Bmvt14 = Button(fenetre, text="back_prime", bg= 'red', font= "Helvetica 12 bold"  , command=back_prime )
    Bmvt14_fenetre = fond.create_window(x+1215, 700, window=Bmvt14)



    Bmvt17 = Button(fenetre, text="front_prime", bg= 'red', font= "Helvetica 12 bold"  , command=front_prime )
    Bmvt17_fenetre = fond.create_window(x+1350 , 700, window=Bmvt17)

    Bmvt18 = Button(fenetre, text="front", bg= 'red', font= "Helvetica 12 bold"  , command=front )
    Bmvt18_fenetre = fond.create_window(x+1485 , 700, window=Bmvt18) 

        




# Creation du bouton permettant de fermer la fenetre.
restart = Button(fenetre, text="restart", bg='SlateGray1' , bd= 10 , activebackground ='red',command=CubeResolue)
restart_fenetre = fond.create_window(40, 20, window=restart)
scrambl = Button(fenetre, text="scrambl", bg='SlateGray1' , bd= 10 , activebackground ='red',command=scrambler)
scrambl_fenetre = fond.create_window(40, 100, window=scrambl)
design = Button(fenetre, text="design", bg='SlateGray1' , bd= 10 , activebackground ='red',command=design)
design_fenetre = fond.create_window(40, 150, window=design)




######################################################################### MAIN #############################################################################

CubeResolue ()
Boutons()
liste =[left_prime,left,right_prime,right,up_prime,up,down_prime,down,back_prime,back,front_prime,front]

fenetre.mainloop()



    





