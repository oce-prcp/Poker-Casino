import random

#------------------PREMIER TIRAGE---------------

def premier_tirage(deck):   
    tirage = random.sample(deck,5)

    for i in tirage:
        deck.remove(i)
    
    print("\n\nVoici votre premier tirage",tirage)
    return tirage, deck

#------------------CHOIX DES CARTES---------------

def choix_carte(tirage1):
    jeu = []

    for carte in tirage1:
        choix1 = input("\nGarder la carte "+carte+"? (y/n)\n")
        
        if choix1 == "y":
            jeu.append(carte)
    
    return jeu

#-----------------2e TIRAGE------------------

def deuxieme_tirage(jeu,deck2):
    carteATirer = 5 - len(jeu)
    print("\n------------------------------------------------------\n\nVoici votre jeu:",jeu,"\n")
    tirage2 = random.sample(deck2,carteATirer)

    if len(tirage2) != 0:
        print("Voici les cartes que vous venez de tirer ",tirage2,"\n")
    
    tirageFinal = jeu + tirage2
    
    if len(tirage2) != 0:
        print("Voici votre nouvelle main:",tirageFinal,"\n")
    
    return tirageFinal

#-----------------MACHINE------------------

def machine():
    deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
    #deck = ['3-d','3-h','3-s','3-c','6-h']
    tirage1,deck2 = premier_tirage(deck)
    jeu = choix_carte(tirage1)
    tirageFinal = deuxieme_tirage(jeu,deck2)
    return tirageFinal


#tirageFinal = machine()

#---------------------------DECOMPOSER LA MAIN-----------------------

def decomp(tirageFinal):
    valeur = []
    couleur = []

    for carte in tirageFinal:
        valeur.append(carte.split("-")[0])
        couleur.append(carte.split("-")[1])

    for e,i in zip(valeur, range(0,5)):

        try:
            valeur[i] = int(e)

        except:
            if e == "J":
                valeur[i] = 11
            elif e == "Q":
                valeur[i] = 12
            elif e == "K":
                valeur[i] = 13
            elif e == "A":
                valeur[i] = 14
            else:
                continue
    return valeur,couleur

#---------------------------PAIRE-----------------------

def Paire(tirageFinal):
        valeur,couleur = decomp(tirageFinal)
        valeurDistinctes = set(valeur)
        compte = []

        for i in valeurDistinctes:
            compte.append(valeur.count(i))

        compte.sort()

        if len(valeurDistinctes) == 4 and compte == [1,1,1,2]:
            return True
        
        else:
            return False

#---------------------------DOUBLE PAIRE-----------------------

def DoublePaire(tirageFinal):
        valeur,couleur = decomp(tirageFinal)
        valeurDistinctes = set(valeur)
        compte = []

        for i in valeurDistinctes:
            compte.append(valeur.count(i))

        compte.sort()

        if len(valeurDistinctes) ==3 and compte == [1,2,2]:
            return True
        
        else:
            return False

#---------------------------BRELAN-----------------------

def brelan(tirageFinal):
        valeur,couleur = decomp(tirageFinal)
        valeurDistinctes = set(valeur)
        compte = []

        for i in valeurDistinctes:
            compte.append(valeur.count(i))
        
        compte.sort()
        
        if len(valeurDistinctes) == 3 and compte == [1,1,3]:
            return True
        
        else:
            return False

#---------------------------CARRÉ-----------------------

def carre(tirageFinal):
        valeur,couleur = decomp(tirageFinal)
        valeurDistinctes = set(valeur)
        compte = []

        for i in valeurDistinctes:
            compte.append(valeur.count(i))
        
        compte.sort()
        
        if len(valeurDistinctes) == 2 and compte == [1,4]:
            return True
        
        else:
            return False

#---------------------------QUINTE-----------------------

def Quinte(tirageFinal):
    valeur,couleur = decomp(tirageFinal)
    valeur.sort()
    int_valeur = []

    for i in valeur:
        int_valeur.append(int(i))

    if int_valeur[0] + 4 == int_valeur[1] + 3 == int_valeur[2] + 2 == int_valeur[3] + 1 == int_valeur[4]:
        return True
    else: 
        return False

#---------------------------FLUSH-----------------------

def flush(tirageFinal):
    valeur,couleur = decomp(tirageFinal)
    couleur.sort()
    n = 5
    prev = -10
    count = 0
    flag = 0

    for item in couleur:
        if item == prev:
            count = count+1
        else:
            count = 1
        prev = item

        if count == n:
            flag = 10
            return True
    
    if flag == 0:
        return False

#---------------------------FULL-----------------------

def full(tirageFinal):
        valeur,couleur = decomp(tirageFinal)
        valeurDistinctes = set(valeur)
        compte = []
        for i in valeurDistinctes:
            compte.append(valeur.count(i))
        compte.sort()
        if len(valeurDistinctes) == 2 and compte == [2,3]:
            return True
        else:
            return False

#---------------------------QUINTE FLUSH-----------------------

def quinteFlush(tirageFinal):

    if Quinte(tirageFinal) == True and flush(tirageFinal) == True:
        return True

    else:
        return False

#---------------------------QUINTE FLUSH ROYAL-----------------------

def QuinteFlushRoyale(tirageFinal):
    valeur,couleur = decomp(tirageFinal)
    valeur.sort()

    if valeur == [10,11,12,13,14] and flush(tirageFinal) == True:
        return True

    else:
        return False

#---------------------------CHECK COMBINAISONS-----------------------

def combinaisons(tirageFinal,mise):

    if QuinteFlushRoyale(tirageFinal) == True:
        gain = mise * 250
        result = "Vous avez un quinte flush royale, vous gagnez {} euros".format(gain)  
        return gain,result

    elif quinteFlush(tirageFinal) == True:
        gain = mise * 50
        result = "Vous avez un quinte flush, vous gagnez {} euros".format(gain)
        return gain,result

    elif carre(tirageFinal) == True:
        gain = mise * 25
        result = "Vous avez un carre, vous gagnez {} euros".format(gain)
        return gain,result

    elif full(tirageFinal) == True:
        gain = mise * 9
        result = "Vous avez un full, vous gagnez {} euros".format(gain)
        return gain,result

    elif flush(tirageFinal) == True:
        gain = mise * 6
        result = "Vous avez un flush, vous gagnez : {} euros".format(gain)
        return gain,result

    elif Quinte(tirageFinal) == True:
        gain = mise * 4
        result = "Vous avez un quinte, vous gagnez {} euros".format(gain)
        return gain,result
    
    elif brelan(tirageFinal) == True:
        gain = mise * 3
        result = "Vous avez un brelan avez, vous gagnez: {} euros".format(gain)
        return gain,result

    elif DoublePaire(tirageFinal) == True:
        gain = mise * 2
        result = "Vous avez une double paire, vous gagnez: {} euros".format(gain)
        return gain,result

    elif Paire(tirageFinal) == True:
        gain = mise * 1
        result = "Vous avez une paire, vous gagnez: {} euros".format(gain)
        return gain,result
    
    else:
        gain = 0
        result = "Perdu"
        return gain, result

#---------------------------JEU-----------------------

def video_poker():

        #---------reccueil des renseignements---------

    sexe = input("Bonjour, veuillez renseigner votre sexe.(Homme/Femme)").lower()
    age = int(input("Veuillez saisir votre âge s'il vous plaît."))
    
        #--------traitement des renseignements--------

    if age < 18:
        print("Désolé, vous ne pouvez pas jouer avant d'avoir 18 ans.")
        return
    
    elif age > 110 and sexe == "homme":
        print("Vous êtes mort monsieur, que faites-vous ici ?")
        return

    elif age > 110 and sexe == "femme":
        print("Vous êtes morte madame, que faites-vous ici ?")
        return

    else:
        print("Bienvenue au Video Poker 2000")


    bankroll = int(input("Veuillez saisir une branroll :"))

        #---------mise en route de la machine---------

    while bankroll > 0:
        mise = int(input("\nVeuillez saisir votre mise: "))

        if mise <= bankroll:
            tirageFinal = machine()
            gain,result = combinaisons(tirageFinal,mise)
            print(result,"\n")
            bankroll = bankroll - mise + gain
            print("Votre bankroll est de {} euros".format(bankroll),"\n")

        else:
            print("Votre mise est inccorrecte, veuillez resaisir une mise")
        
        #---------partie terminée, demande de relancement---------

        print("Voulez vous rejouer ?")
        rejouer = str(input()).lower()

        if rejouer == "non" or "nan" or "nope" or "non merci":
            print("Voici votre bankroll:",bankroll,"euros merci de votre visite et à bientôt !")
            break
video_poker()