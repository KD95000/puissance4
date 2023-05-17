import pygame
import random

class Game:
    def __init__(self):

        self.screen = pygame.display.set_mode((674, 577))   
        self.running = True
        self.grille = pygame.image.load("grille.png")   
        self.pion_rouge = pygame.image.load("pionrouge.png")
        self.pion_jaune = pygame.image.load("pionjaune.png")

        # J'initialise le numéro de la colonne où le joueur va poser son pion
        # Je le met à -1 car 0 correspond bien à quelque chose dans une liste
        self.colonne = -1

        # Je crée des rectangles invisible pour chaque colonne de la grille, ça me servira par la suite pour savoir sur quelle colonne on a cliqué
        self.col1 = pygame.Rect(0,0,96,577)
        self.col2 = pygame.Rect(97,0,96,577)
        self.col3 = pygame.Rect(193,0,96,577)
        self.col4 = pygame.Rect(289,0,96,577)
        self.col5 = pygame.Rect(385,0,96,577)
        self.col6 = pygame.Rect(481,0,96,577)
        self.col7 = pygame.Rect(577,0,96,577)
        
        # Je tire au hasard le joueur qui va commencer la partie
        self.joueurs = ["jaune","rouge"]
        self.joueur = random.choice(self.joueurs)
        
        # Je crée la matrice qui représente ma grille de puissance 4
        # sans elle je ne pourrais pas faire de vérification pour voir qui a gagné
        self.matrice = [[0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        ]

    # Gestion des évenements 
    def gestion_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Si l'utilisateur clique sur la colonne 1
            if event.type == pygame.MOUSEBUTTONUP and self.col1.collidepoint(event.pos):
                # On stocke le numéro de la colonne où l'utilisateur veux jouer (on commence par 0 car l'index des listes commençent aussi par 0)
                self.colonne = 0
            
            # Si l'utilisateur clique sur la colonne 2
            if event.type == pygame.MOUSEBUTTONUP and self.col2.collidepoint(event.pos):
                self.colonne = 1

            # Si l'utilisateur clique sur...
            if event.type == pygame.MOUSEBUTTONUP and self.col3.collidepoint(event.pos):
                self.colonne = 2

            if event.type == pygame.MOUSEBUTTONUP and self.col4.collidepoint(event.pos):
                self.colonne = 3

            if event.type == pygame.MOUSEBUTTONUP and self.col5.collidepoint(event.pos):
                self.colonne = 4
                
            if event.type == pygame.MOUSEBUTTONUP and self.col6.collidepoint(event.pos):
                self.colonne = 5

            if event.type == pygame.MOUSEBUTTONUP and self.col7.collidepoint(event.pos):
                self.colonne = 6
                    
# Afficher la matrice sous forme de tableau en console (pour que je fasse des tests)
    def afficher_matrice(self):
        for liste in self.matrice:
            print(liste)
    
    def jouer(self):
        pass

    def jouer_grille(self):
        pass

    # Je crée une fonction qui va me servir a remettre chacun des pion joués dans la matrice
    def jouer_matrice(self):
        for i in range(len(self.matrice[0])):   # Je met une boucle for
            if i == self.colonne:               # Suivie de cette ligne pour éviter d'écrire 7 if d'affilé 
                for j in range(len(self.matrice)):
                    if self.joueur == "jaune":
                        
                        # Si il n'y a aucun pion tout en bas de la colonne jouée, on en pose un
                        if self.matrice[5][i] == 0:
                            self.matrice[5][i] = 1 # On joue (avec un 1, c'est le chiffre du pion jaune)
                            # C'est alors à l'autre de jouer
                            self.joueur = "rouge"
                            break
                        
                        # Si il y a un pion tout en haut de la colonne jouée, c'est plein, on ne peut rien poser
                        if self.matrice[0][i] == 1 or self.matrice[0][i] == 2:
                            print("Coup impossible !!! Veuillez rejouer")
                            # On ne met donc pas de "self.joueur = "rouge" car c'est encore au jaune de jouer
                            break
                        
                        # Sinon, on descend jusqu'à ce que l'on trouve un pion puis on pose le notre juste au dessus dans la matrice
                        if self.matrice[j][i] == 1 or self.matrice[j][i] == 2:
                            self.matrice[j-1][i] = 1
                            # C'est alors à l'autre de jouer
                            self.joueur = "rouge"
                            break

                    # Exactement le même morceau de code mais quand c'est au rouge de jouer
                    # On pose juste des 2 au lieu des 1
                    if self.joueur == "rouge":
                        if self.matrice[5][i] == 0:
                            self.matrice[5][i] = 2
                            self.joueur = "jaune"
                            break

                        if self.matrice[0][i] == 1 or self.matrice[0][i] == 2:
                            print("Coup impossible !!! Veuillez rejouer")
                            break
                        
                        if self.matrice[j][i] == 1 or self.matrice[j][i] == 2:
                            self.matrice[j-1][i] = 2
                            self.joueur = "jaune"
                            break
                print("---------------------")
                self.colonne = -1  
                self.afficher_matrice()
                break

    def verif_ligne(self):
        self.compteur = 0
        for i in range(1,3):
            for ligne in self.matrice:
                for chiffre in ligne:
                    if chiffre == i:
                        self.compteur += 1

                    if chiffre != i:
                        self.compteur = 0

                    if self.compteur >= 4:
                        print("Le joueur",i,"a gagné")
                        self.running = False
            self.compteur=0

    def verif_colonne(self):
        for joueur in range(1,3):
            chiffre = joueur
            for i in range(len(self.matrice[0])):
                for j in range(len(self.matrice)):
                    if self.matrice[j][i] == chiffre:
                        self.compteur += 1
                    
                    if self.matrice[j][i] != chiffre:
                        self.compteur = 0

                    if self.compteur >= 4:
                        print("Le joueur",joueur,"a gagné")
                        self.running = False
            self.compteur = 0

    def verif_diago_descendante(self):
        pass


    
    
    def verif_diago_montante(self):
        for joueur in range(1,3):
            chiffre = joueur
            for i in range(len(self.matrice)):
                for j in range(i+1):
                    for k in range(j):
                        
                        if self.matrice[i-k][k] == chiffre:
                            self.compteur += 1

                        if self.matrice[i-k][k] != chiffre:
                            self.compteur = 0

                        if self.compteur >= 4:
                            print("Le joueur",joueur,"a gagné")
                            self.running = False
            self.compteur = 0

                        
                            




    
    
    
    
    
    
    def verif(self):
        self.verif_ligne()
        self.verif_colonne()
        #self.verif_diago_descendante()
        self.verif_diago_montante()

                
                



    # Boucle du jeu
    
    def run(self):
        while self.running:
            self.gestion_events()
            self.screen.blit(self.grille, (0,0))
            self.screen.blit(self.pion_rouge, (0,0))
            
            self.jouer_matrice()
            self.verif()
            pygame.display.flip()
            
            
            
            
            
            
            
            
            
            
            
            
            


pygame.init()





game = Game()
game.run()



pygame.quit()

