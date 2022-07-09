# coding: utf8
"""
cd Documents/Main\ Desktop/Python/SI\ IA/
"""
import pygame as py
from random import randint
py.init()

ROUGE       = (255,0,0)
NOIR        = (0,0,0)
BLANC       = (255,255,255)
### def des variables :
# def couleur de fonc
C_FOND = NOIR

LARGUEUR = 600
HAUTEUR = 600
"""
# importation des sons :
son_gen = py.mixer.Sound("son_gen.ogg")
point =py.mixer.Sound("point.ogg")
"""
logo = py.image.load("petit_logo.png")
#logo.convert()

pion_h = py.image.load("PION_h.png")
pion_ia = py.image.load("PION_ia.png")

#nombre de pixel par coté de carré
speed = 1000
case = 200
#pion = py.image.load("pion.png")

## Définition des variables :
pn_h=[
[ 1 , 1 ]
,[ 1 , 2 ]
,[ 1 , 3 ]
]
pn_ia=[
[ 3 , 1 ]
,[ 3 , 2 ]
,[ 3 , 3 ]
]
pos_curseur = [1,1]
situation = ""
situation_h=""

"""
possibilite=[]
"""


possibilite=[
['A2 A3 C1 C2 ', ['A3', 'C1']] ,
['A2 A3 ', ['A2']] ,
['A2 B3 ', ['A2']] ,
['A2 B2 B3 ', ['B3']] ,
['A2 ', ['A2']] ,
['B1 B2 C2 ', ['B1']] ,
['A3 B1 ', ['A3']] ,
['A2 A3 B2 C1 ', ['A3', 'B2', 'C1']] ,
['A2 B3 C1 C2 ', ['A2', 'B3', 'C1', 'C2']] ,
['C2 ', ['C2']] ,
['C1 C2 ', ['C2']] ,
['A3 B2 C1 C2 ', ['A3', 'B2', 'C1']] ,
['A2 A3 B2 ', ['A3', 'B2']] ,
['A2 B2 ', ['A2', 'B2']] ,
['B1 C2 ', ['B1', 'C2']] ,
['B1 C2 C3 ', ['B1', 'C2', 'C3']] ,
['A2 A3 B1 C2 ', ['A2', 'A3', 'B1', 'C2']]
]



"""
 Explication de l'utilisation du cadrillage

[ 1 , 1 ]	[ 2 , 1 ]	[ 3 , 1 ]

[ 1 , 2 ]	[ 2 , 2 ]	[ 3 , 2 ]

[ 1 , 3 ]	[ 2 , 3 ]	[ 3 , 3 ]

1 <\-
2 <--
3 </-

[ "A12B3C2",[ A1,B3,C2 ]   ]
"""

def win_ia(window):
    arial_30 = py.font.SysFont("arial", 30)
    dimension_text = arial_30.render("{}".format(" l'IA a gagné !! ; - ) "), True, ROUGE)
    window.blit(dimension_text, [200,200] )
    py.display.flip()
    py.time.delay(10)


def loose_ia(window):
    arial_30 = py.font.SysFont("arial", 30)
    dimension_text = arial_30.render("{}".format(" l'IA a perdu !! ; - ) "), True, ROUGE)
    window.blit(dimension_text, [200,200] )
    py.display.flip()

def aff_curseur(window,curseur):
	window.blit(curseur,[pos_curseur[0]*50-50,pos_curseur[1]*50-50] )

def aff_pn(window, h, ia):
	window.fill(BLANC)
	for i in h:
		window.blit(pion_h,[i[0]*case-case,i[1]*case-case])
	for i in ia:
		window.blit(pion_ia,[i[0]*case-case,i[1]*case-case])
	py.display.flip()

def analyse_situation_droite(pn_ami,pn_enm):
    situation =""
    for i,j in zip(pn_ami,"ABC") :
        x,y=i[0],i[1]

        for k in pn_enm:
            if (y == 2 or y == 3) and [x-1,y-1] == k :
                situation+= j+"1"+" "

        test = True
        for k,l in zip(pn_enm,pn_ami ):
            if y==0 or [x-1,y]==k or [x-1,y]==l:
                test = False
        if test == True :
            situation+= j+"2"+" "

        for k in pn_enm :
            if (y == 1 or y == 2) and [x-1,y+1]== k :
                situation+= j+"3"+" "
    return(situation)

def analyse_situation_gauche(pn_ami,pn_enm):
    situation =""
    for i,j in zip(pn_ami,"ABC") :
        x,y=i[0],i[1]

        for k in pn_enm:
            if (y == 2 or y == 3) and [x-1,y+1] == k :
                situation+= j+"1"+" "

        test = True
        for k,l in zip(pn_enm,pn_ami) :
            if y==0 or [x+1,y]==k or [x+1,y]==l:
                test = False
        if test == True :
            situation+= j+"2"+" "

        for k in pn_enm :
            if (y == 1 or y == 2) and [x+1,y+1]== k :
                situation+= j+"3"+" "
    return(situation)

def reinit():
	h=[
	[ 1 , 1 ]
	,[ 1 , 2 ]
	,[ 1 , 3 ]
	]

	ia=[
	[ 3 , 1 ]
	,[ 3 , 2 ]
	,[ 3 , 3 ]
	]
	#pos_curseur = [1,1]
	situation = ""
	situation_h=""
	return(ia,h)

def aff_possibilite():
	for i in possibilite:
		print(i,",")
