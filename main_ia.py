# coding : utf8

"""
cd Documents/Main\ Desktop/Python/SI\ IA/
code principale de l'IA
Hexapawn Paul ADAM 
"""

# importation des modules 

import pygame as py
#import time
from random import randint
import module_ia as m

# initialisation de pygame
py.init()

# Initialisation de la fenetre graphique avec son nom
# | py.RESIZABLE
fenetre = py.display.set_mode((m.LARGUEUR,m.HAUTEUR), py.DOUBLEBUF | py.HWSURFACE )
py.display.set_caption("IA Hexapawn")

# vérif des paramètres d affichage dans le terminal :
print(py.display.Info())

#affichage logo et démarrage :
fenetre.blit(m.logo,[0,0])
py.display.flip()
A = True
# FIN = True
while A :
    for event in py.event.get() :
        if event.type == py.QUIT :
            A = False
            # FIN = False
            break
        if event.type == py.KEYDOWN :
            if event.key == py.K_SPACE :
                A = False
                break


# fond blanc
# m.pion_h.convert()
# m.pion_ia.convert()


fenetre.fill(m.BLANC)

# première image : affichage de tous les pions
m.aff_pn(fenetre,m.pn_h,m.pn_ia)
py.display.flip()

# importation des image et transparance 
selec_j = py.image.load("selection_jaune.png").convert()
selec_j.set_colorkey(m.BLANC)

selec_v = py.image.load("selection_verte.png").convert()
selec_v.set_colorkey(m.BLANC)


def jeu(window):
    FIN = True
    test3 = False
    nb = 0 
    # Coeur du programme
    #window.fill(m.NOIR)
    while  FIN :

        for event in py.event.get() :
            if event.type == py.QUIT :
                FIN = False
                break

        # affichage des pions
        m.aff_pn(window,m.pn_h,m.pn_ia)
        #py.time.delay(1000)


        ###### TOUR JOUEUR :
        # choisir son pion
        pion_choisi = 5
        m.pos_curseur= [1,1] 
        test1 = True
        while test1 ==True :
            for event in py.event.get() :
                if event.type == py.KEYDOWN :
                    if event.key == py.K_UP :
                        m.pos_curseur[1]-=1
                    elif event.key == py.K_DOWN :
                        m.pos_curseur[1]+=1
                    elif  event.key == py.K_LEFT :
                        m.pos_curseur[0]-=1
                    elif event.key == py.K_RIGHT :
                        m.pos_curseur[0]+=1
                    elif event.key == py.K_SPACE :
                        test1 = False
                window.fill(m.BLANC)
                m.aff_pn(window,m.pn_h,m.pn_ia)
                window.blit(selec_j,[m.pos_curseur[0]*m.case-m.case,m.pos_curseur[1]*m.case-m.case])
                ##
                py.display.flip()
        pion_choisi = m.pn_h.index(m.pos_curseur)
        # choisir son déplacement de pion :
        test2 = True
        while test2 == True :
            for event in py.event.get() :
                if event.type == py.KEYDOWN :
                    if event.key == py.K_UP :
                        m.pos_curseur[1]-=1
                    elif event.key == py.K_DOWN :
                        m.pos_curseur[1]+=1
                    elif  event.key == py.K_LEFT :
                        m.pos_curseur[0]-=1
                    elif event.key == py.K_RIGHT :
                        m.pos_curseur[0]+=1
                    elif event.key == py.K_SPACE :
                        test2 = False
                window.fill(m.BLANC)
                m.aff_pn(window,m.pn_h,m.pn_ia)
                window.blit(selec_v,[m.pos_curseur[0]*m.case-m.case,m.pos_curseur[1]*m.case-m.case])
                py.display.flip()


        m.pn_h[pion_choisi]=m.pos_curseur
        window.fill(m.BLANC)
        m.aff_pn(window,m.pn_h,m.pn_ia)
        window.blit(selec_v,[m.pos_curseur[0]*m.case-m.case,m.pos_curseur[1]*m.case-m.case])

        # py.time.delay(1000)
        py.display.flip()


        ###### TEST DE VISTOIRE OU DEFAITE
        ### test de pion humain qui mange un pion IA :
        for ia in m.pn_ia:
            for h in m.pn_h:
                if ia == h :
                    m.pn_ia[m.pn_ia.index(ia)]= [0,0]

        m.aff_pn(window,m.pn_h,m.pn_ia)
        # tous les pions ia morts :
        compteur = 0
        for ia in m.pn_ia :
            if ia == [0,0] :
                compteur += 1
        if compteur == 3 :
            # IA a perdu
            m.loose_ia(window)
            m.possibilite[nb][1].remove(tirage)
            print("Tous les pions IA sont morts")
            break

        # arrivée ligne humain
        compteur = 0 
        for h in m.pn_h :
            if h[0] ==  3 :
                # IA a perdu
                m.loose_ia(window)
                m.possibilite[nb][1].remove(tirage)
                compteur +=1
        if compteur == 1:
            print("Humain de l'autre coté du plateau")
            break

        # ia peut plus bouger
        m.situation=m.analyse_situation_droite(m.pn_ia,m.pn_h)

        if m.situation == "" :
            m.loose_ia(window)
            m.possibilite[nb][1].remove(tirage)
            #print(m.possibilite)
            print("IA ne peut plus bouger")
            break

        m.aff_pn(window,m.pn_h,m.pn_ia)
        py.time.delay(1000)

        
        ###### TOUR IA
        # analyse de la situation pour IA
        m.situation = m.analyse_situation_droite(m.pn_ia,m.pn_h)
        
        # analyse si la situation est deja été expérimenté : 
        # si test3 == True alors la situation a déjà été analysé  
        # on tire au hasard dans les possibilités
        # si test3 == False alors on ajoute la situation en dernier

        test3=False
        for i in m.possibilite :
            if m.situation == i[0]:
                test3 = True
                nb = m.possibilite.index(i)
                         
        if test3 == False :
            m.possibilite.append( [m.situation , m.situation.split()] )
            nb = -1


        # on tire au hasard dans la liste des possibilités :
        tirage = m.possibilite[nb][1][randint(0,len(m.possibilite[nb][1])-1) ]
        if tirage[0] == "A" :
            x=0
        elif tirage[0] == "B" :
            x=1
        elif tirage[0] == "C" :
            x=2
        
        if tirage[1] == "1" :
            m.pn_ia[x][0]-=1
            m.pn_ia[x][1]-=1
        elif tirage[1] == "2" :
            m.pn_ia[x][0]-=1
            m.pn_ia[x][1]+=0
        elif tirage[1] == "3" :
            m.pn_ia[x][0]-=1
            m.pn_ia[x][1]+=1


        m.aff_pn(window,m.pn_h,m.pn_ia)
        # py.time.delay(1000)


        ###### TEST DE VISTOIRE OU DEFAITE

        # [1.] test de pion IA qui mange un pion Humain :
        for ia in m.pn_ia:
            for h in m.pn_h:
                if ia == h :
                    m.pn_h[m.pn_h.index(h)]= [0,0]

        # différente vérification de victoire ou défaite qui mette fin au jeu :

        # [2.] tous les pions humain morts :
        compteur = 0
        for h in m.pn_h :
            if h == [0,0] :
                compteur += 1
        if compteur == 3 :
            m.win_ia(window)
            # if len(m.possibilite[nb][1])>1 :
            #    m.possibilite[nb][1].append(tirage)
            print("ts les pions joueurs st morts")
            break
        

        # [3.] plus de mouvement possible humain :

        m.situation_h=m.analyse_situation_gauche(m.pn_h,m.pn_ia)

        if m.situation_h == "" :
            m.win_ia(window)
            #if len(m.possibilite[nb][1])>1 :
            #    m.possibilite[nb][1].append(tirage)
            print("Plus de mouvement pour le joueur")
            break

        # [4.] arrivée IA territoire ennemie :

        compteur = 0
        for ia in m.pn_ia :
            if ia[0] ==  1 :
                m.win_ia(window)
                #if len(m.possibilite[nb][1])>1 :
                #    m.possibilite[nb][1].append(tirage)
                print("IA de l'autre coté du plateau")
                compteur+=1
        if compteur == 1 :    
            break


        # actualisation de l'écran
        py.display.flip()


# boucle de jeu
# cette boucle fait tourner les tours de jeu à l'infini

a = "O"
while a == "O" :
    m.pn_ia,m.pn_h=m.reinit()
    m.aff_pn(fenetre,m.pn_h,m.pn_ia)

    jeu(fenetre)
    A = True
    while A :
        for event in py.event.get() :
            if event.type == py.KEYDOWN :
                if event.key == py.K_SPACE :
                    A = False
                    break
                if event.key == py.K_DELETE :
                    a = "N"
                    A = False
                    break
    if a == "N" :
        m.aff_possibilite()