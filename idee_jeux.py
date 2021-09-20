# """ Deuxieme jeu : calcul mental"""
# """
# - optimiser le code avec une fonction pour afficher les messages succes et echec
# - 
# """

# # fonction menu
# def menu():
#     print("L'objectif du jeu ici est de donner le resultat correct ")
#     print("Avant la fin du decompte de chrono ")
#     print("Entrez '1' pour l'addition ")
#     print("Entrez '2' pour la soustraction ")
#     print("Entrez '3' pour la multiplication ")
#     print("Entrez '4' pour la division ")
#     return 0

# # fomction addition
# def addition(a, b):
#     return a + b

# # foction soustraction
# def soustraction(a, b):
#     return a - b

# # fonction multiplication
# def multiplication(a, b):
#     return a * b

# # fonction division
# def division(a, b):
#     return a / b


# def countdown(t):
#     import time

#     for i in range(t):
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1
        
#         return t

# def nouvelEssai():
#     choix = input("Voulez-vous contniuer ? 'O' ou 'N' ")
#     print()
#     if choix == 'O' or choix == 'o':
#         return True
#     else:
#         return False

# def permuterNbre(a, b):
#     # temp = a
#     # a = b
#     # b = temp
#     return b, a

# def compterNbreFois(liste, taille, numExercice):
#     """
#     l'idee est de pouvoir informer le joueur du nombre de fois 
#     qu'il a reussi ou echoue un type d'exercice
#     """
#     # sort the array
#     liste.sort()
#     # compteur a incrementer a chaque fois que le nombre est trouver
#     count = 0
#     for i in range(taille):
#         if(liste[i] == numExercice):
#             count += 1
#     return count

# def userAnswer(temps):
#     """ https://www.sololearn.com/Discuss/2701635/how-to-set-an-input-time-limit-in-python """    
#     t1 = time.time()
#     reponse = int(input("Votre reponse: "))
#     t2 = time.time()
#     t = t2 - t1
#     if t > temps:
#         print("Trop tard! Temps termine")
#         return reponse, t
#     return reponse, t


# if __name__ == '__main__':
#     menu()
#     count = 0
#     listChoix   = [] # pour stocker les choix fait 
#     listSuccess = [] # stocker les choix reussis
#     listEchec   = [] # stocker les choix echoue
#     while(True):
#         import random, time

#         if(count > 0):
#             print(listChoix, listSuccess, listEchec)
#         count += 1
#         choix = int(input("Choisissez l'operation sur laquelle vous voulez travailler "))
#         print()
#         listChoix.append(choix)
#         if(choix == 1):
#             nbre1 = random.randint(0,100)
#             nbre2 = random.randint(0,100)
#             result = addition(nbre1, nbre2)
#             print("{} + {} = ".format(nbre1, nbre2))
            
#             # verifier si premier fois de faire exercice
#             verif = compterNbreFois(listChoix, len(listChoix), choix)
#             if(verif <= 1):
#                 print("Plaisir de vous avoir pour la premiere fois :) ")
#             # insert here code to condition time of input
#             b = True # declare boolean so that code can be executed only if it is still True
          
#             # declencher le compteur + reponse user
#             reponse, temps = userAnswer(10)  
#             if(temps > 10)  :
#                 b = False
#                 listEchec.append(choix)
#                 quitter = nouvelEssai()
#                 if quitter == 1:
#                     continue
#                 else:
#                     break

#             if b == True:
            
#                 if (reponse == result):
#                     print("Felicitation! Reponse correct!!! \n")
#                     listSuccess.append(choix) # enregistrer les choix reussis
#                     print("Vous avez fait cet exercice {} fois et reussi {} fois \n".format(compterNbreFois(listChoix, len(listChoix), choix), \
#                         compterNbreFois(listSuccess, len(listSuccess), choix)))
#                     continue
#                 else:
#                     print("Le prochain essai sera le bon \n")
#                     listEchec.append(choix)   # enregistrer les choix echoues
#                     print("Vous avez fait cet exercice {} fois et echoue {} fois \n".format(compterNbreFois(listChoix, len(listChoix), choix), \
#                         compterNbreFois(listEchec, len(listEchec), choix)))
#                     quitter = nouvelEssai()
#                     if quitter == 1:
#                         continue
#                     else:
#                         break

#         if(choix == 2):
#             nbre1 = random.randint(0,100)
#             nbre2 = random.randint(0,100)
#             result = soustraction(nbre1, nbre2)

#             # verifier si premier fois de faire exercice
#             verif = compterNbreFois(listChoix, len(listChoix), choix)
#             if(verif <= 1):
#                 print("Plaisir de vous avoir pour la premiere fois :) ")

#             print("{} - {} = ".format(nbre1, nbre2))

#             # recuperer le choix du joueur
#             b = True # declare boolean so that code can be executed only if it is still True
          
#             # declencher le compteur + reponse user
#             reponse, temps = userAnswer(10)  
#             if(temps > 10)  :
#                 b = False
#                 listEchec.append(choix)
#                 quitter = nouvelEssai()
#                 if quitter == 1:
#                     continue
#                 else:
#                     break

#             if b == True:
        
#                 if(reponse == result):
#                     print("Felicitation! Reponse correct!!! \n")
#                     listSuccess.append(choix) # enregistrer les choix reussis
#                     print("Vous avez fait cet exercice {} fois et reussi {} fois \n".format(compterNbreFois(listChoix, len(listChoix), choix), \
#                         compterNbreFois(listSuccess, len(listSuccess), choix)))
#                     continue
#                 else:
#                     print("Le prochain essai sera le bon \n")
#                     listEchec.append(choix)   # enregistrer les choix echoues
#                     print("Vous avez fait cet exercice {} fois et echoue {} fois \n".format(compterNbreFois(listChoix, len(listChoix), choix), \
#                         compterNbreFois(listEchec, len(listEchec), choix)))
#                     quitter = nouvelEssai()
#                     if quitter == 1:
#                         continue
#                     else:
#                         break

#         if(choix == 3):
#             nbre1 = random.randint(0,20)
#             nbre2 = random.randint(0,20)
#             result = multiplication(nbre1, nbre2)

#             # verifier si premier fois de faire exercice
#             verif = compterNbreFois(listChoix, len(listChoix), choix)
#             if(verif <= 1):
#                 print("Plaisir de vous avoir pour la premiere fois :) ")

#             print("{} x {} = ".format(nbre1, nbre2))
            
#             # recuperer le choix du joueur
#             b = True # declare boolean so that code can be executed only if it is still True
          
#             # declencher le compteur + reponse user
#             reponse, temps = userAnswer(10)  
#             if(temps > 10)  :
#                 b = False
#                 listEchec.append(choix)
#                 quitter = nouvelEssai()
#                 if quitter == 1:
#                     continue
#                 else:
#                     break

#             if b == True:
            
#                 if (reponse == result):
#                     print("Felicitation! Reponse correct!!! \n")
#                     listSuccess.append(choix) # enregistrer les choix reussis
#                     print("Vous avez fait cet exercice {} fois et reussi {} fois \n".format(compterNbreFois(listChoix, len(listChoix), choix), \
#                         compterNbreFois(listSuccess, len(listSuccess), choix)))
#                     continue
#                 else:
#                     print("Le prochain essai sera le bon \n")
#                     listEchec.append(choix)   # enregistrer les choix echoues
#                     print("Vous avez fait cet exercice {} fois et echoue {} fois \n".format(compterNbreFois(listChoix, len(listChoix), choix), \
#                         compterNbreFois(listEchec, len(listEchec), choix)))
#                     quitter = nouvelEssai()
#                     if quitter == 1:
#                         continue
#                     else:
#                         break

#         if(choix == 4):
#             nbre1 = random.randint(1,30)
#             nbre2 = random.randint(1,30)

#             # verifier si premier fois de faire exercice
#             verif = compterNbreFois(listChoix, len(listChoix), choix)
#             if(verif <= 1):
#                 print("Plaisir de vous avoir pour la premiere fois :) ")

#             # verifier que le numerateur > au denominateur
#             if(nbre2 > nbre1):
#                 nbre1, nbre2 = permuterNbre(nbre1, nbre2)
#             print("{} / {} = ".format(nbre1, nbre2))
#             result = division(nbre1, nbre2)
#             result = round(result, 2)

#             # recuperer le choix du joueur
#             b = True # declare boolean so that code can be executed only if it is still True
#             # declencher le compteur + reponse user
#             t1 = time.time()
#             reponse = float(input("Votre reponse: "))
#             t2 = time.time()
#             t = t2 - t1
#             if t > 10:
#                 print("Trop tard! Temps termine")
#                 b = False
#                 listEchec.append(choix)
#                 quitter = nouvelEssai()
#                 if quitter == 1:
#                     continue
#                 else:
#                     break

#             if b == True:
#             # faire un arrondi a deux chiffre de la reponse
#                 reponse = round(reponse, 2)
                
#                 # print(reponse, result)

                
#                 if (reponse == result):
#                     print("Felicitation! Reponse correct!!! \n")
#                     listSuccess.append(choix) # enregistrer les choix reussis
#                     print("Vous avez fait cet exercice {} fois et reussi {} fois \n".format(compterNbreFois(listChoix, len(listChoix), choix), \
#                         compterNbreFois(listSuccess, len(listSuccess), choix)))
#                     continue
#                 else:
#                     print("Le prochain essai sera le bon \n")
#                     listEchec.append(choix)   # enregistrer les choix echoues
#                     print("Vous avez fait cet exercice {} fois et echoue {} fois \n".format(compterNbreFois(listChoix, len(listChoix), choix), \
#                         compterNbreFois(listEchec, len(listEchec), choix)))
#                     quitter = nouvelEssai()
#                     if quitter == 1:
#                         continue
#                     else:
#                         break

#     design = "=========="
#     espa = " "

#     print("==================== Statistiques de votre passage ==================== \n")
#     print("==================== Partie Jouee  : {} ====================".format(len(listChoix)))
#     print("==================== Partie Gagnee : {} ====================".format(len(listSuccess)))
#     print("==================== Partie Perdue : {} ====================".format(len(listEchec)))
#     print("========== Historique partie jouee  : {} ====================".format((listChoix)))
#     print("========== Historique partie gagnee : {} {} {} ".format((listSuccess), 2*(len(listChoix)-len(listSuccess))*espa, design))
#     print("========== Historique partie perdue : {} {} {} ".format((listEchec), 2*(len(listChoix)-len(listEchec))*espa, design ))
    


""" Petit jeu tirage aleatoire """

# from typing import Counter


# def tirage(maxPlage):
    
#     # faire le tirage aleatoire 
#     aleatNbre = random.randint(0,maxPlage)
#     print(aleatNbre)
#     choix = int(input("Entrez votre choix ! "))
#     if (choix == aleatNbre):
#         print("Bravo! Vous avez gagnez!!! \n")
#         return True
#     else:
#         print("Vous avez perdu! \n")
#         return False
        


# count = 0
# if __name__ == '__main__':
#     import random
#     maxPlage = 10
#     # afficher un message a l'utilisateur definissant la plage de nombre possible a choisir
#     print("Bienvenue dans le jeu de tirage aleatoire ")
#     print("Si votre choix correspond au nombre aleatoire tirer vous gagnez! ")
#     print("Chaque fois que vous decidez de continuer la plage augmente")
#     print("afin de rendre le tirage plus complexe ")
#     print("Max plage de depart = ", maxPlage)
#     print()
#     tirage(maxPlage)
#     quitter = 'O'
#     while(quitter != 'N'):
#         quitter = input("Voulez-vous rejouer? 'O' ou 'N' ")
#         if(quitter == "O"):
#             maxPlage += 5
#             print("max plage = ", maxPlage)
#             result = tirage(maxPlage)
#         else:
#             print("Merci! A Bientot!!!\n")
#         if (result == 1):
#             count += 1
#         if (count == 3):
#             print("Et trois bonne predictions! Vous etes fait pour predire!!!\n")
#             count = 0


""" Jeu pour completer les lettre manquante """
"""
l'idee c'est d'avoir un repertoire de mots dans une liste qui peut etre completee
puis choisir au hasard un mot, puis supprimer de ce mots un ou deux caractere 
et demander au jouer de completer les lettres manquantes pour faire le mot correct
*** le joueur pourra retaper completement le mot en completant les lettres 
manquantes pour faire simple au debut
"""
import random

print("L'objectif de ce jeu est de trouver le(s) caractere(s) manquant(s) \
       et former le mot correct ")
print("Note: Un mot commence par une lettre 'majuscule' ")

# optimiser le code en recuperant les mots depuis un fichier de mots
# optimiser aussi avec la possibilite de choisir la langue pour jouer
listMots = ["Bonjour", "Merci", "Aurevoir", "Pardon", "Amour", "Bien"]

quitter = True
while(quitter == True):

    # generer un nombre aleatoire compris entre 0 et longueur listMots
    idx = random.randint(0, len(listMots) - 1)
    # recuperer le mot correspondant a l'index generer 
    mots = listMots[idx]
    # trouver un moyen de modifier un caractere du mots
    motsMod = list(mots) # liste4 = "".join(liste2) si besoin de reconstituer le mots en string
    # index pour tirer au hasard la lettre a modifier
    if(len(motsMod) >= 5):
        for i in range(2):
            idxMod = random.randint(0, len(motsMod) - 1)
            motsMod[idxMod] = " "
    else:
        idxMod = random.randint(0, len(motsMod) - 1)
        motsMod[idxMod] = " "
    #  afficher le mot incomplet 
    print("\nMots a completer: {} ".format(motsMod))
    cond = True
    while(cond == True): 
        # demander a l'utilisateur de saisir sa proposition du mot complet 
        userAnswer = input("Saisissez votre reponse en completant la/les lettre(s)\
                            \nmanquantes ou entrez 'Q' pour ne pas repondre ")

        # comparer la reponse utilisateur avec le mots de depart tirer pour savoir si user correct
        if(userAnswer == mots):
            print("\nBravo! Le mot correct est bien: {} ".format(mots))
            cond = False
        elif(userAnswer == 'Q' or userAnswer == 'q'):
            cond = False
        else:
            print("\nDomage votre reponse est incorrect :( ! Essayez a nouveau ")
            cond = True

    quit = input("\nVoulez-vous jouer a nouveau ? 'O' ou 'N' ")
    if(quit == "O" or quit == "o"):
        quitter = True
    else:
        quitter = False

