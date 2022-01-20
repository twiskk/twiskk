
"""
Created on Mon Nov  8 13:49:11 2021

@author: glmorin
"""

import os
"""
On importe le module os de Phyton qui permet d'effectuer des operations courantes liées au systeme d'exploitation, on l'utilisera ici
pour ouvrire un fichier a partier d'un terminal, et pour avoir un affichage plus fluide ( et pas un defilement ) des affichages du jeu

"""

import time

"""
On importe le module time de Phyton qui permet de ralentir l'affichage 

"""

from typing import Dict, List       #on importe du module typing les listes et les dictionnaires, pour pouvoir en cree
from random import randint, sample      #on importe du module random, randint et sample pour pouvoir
from saisiCar import SaisiCar        #on va prendre dans nos fichiers le programme saisiCar et on va importer la fonction SaisiCar


def affichagePlateau(lePlateau: Dict[str, int], leVaisseau: Dict[str, int], lesAliens: List[Dict[str, int]],aTire : bool,posy_aliensatteignable : int or None = None):
    
    """
    -----------
    Cette procedure va nous permettre tout au long du jeu d'afficher les differents elements de notre jeu comme les aliens, le vaiseau, les tires.
    -----------
    Parametre : On entre en Parametre le dictionnaire lePlateau, leVaisseau. On prend aussi la liste de dictionnaire lesAliens, aTire qui est un bouleen et la 
    posy_aliensatteignable qui est un entier et si aucune valeur n'est entrée alors on affectera None a cette variable.
    -----------
    
    """
    
    
    # affichage du Score
    """
    -----------
    Premierement on affichera le score, on va dire que le score prendra la place de 10 espaces, sur ces 10 espaces on comptera aussi la place que va
    prendre le mot  score et on l'enlever a ces 10 espaces comme ca l'affichage du score ne depassera jamais les 10 espaces qu'on lui a donné et l'affichage
    restera le meme. On fera la meme chose pour les vies et les niveaux et agalemnt pour leurs valeurs.
    -----------
    """
    
    longueur_score : int = len(str(lePlateau["score"]))
    espace_score : str = " "*(10-longueur_score)
    longueur_vie : int = len(str(lePlateau["vie"]))
    espace_vie : str = " "*(10-longueur_vie)
    longueur_level: int = len(str(lePlateau["level"]))
    espace_level : str  = " "*(10-longueur_level)
    espace1 : str = " "*5
    espace2 : str = " "*7
    espace3 : str  = " "*4
    print('-'*40)           #on affichera avant les informations sur notre jeux une ligne de trait et egalement apres
    print(espace1, 'Score', espace2, 'Vie', espace3, 'Niveau')
    print(espace_score, lePlateau["score"], espace_vie,lePlateau["vie"], espace_level, lePlateau["level"])
    print('-'*40)

    # couleur leVaisseau et aliens:
        
    """
    -----------
    On va ensuite choisir la couleur de nos aliens, du vaisseau et la couleur du reste du texte 
    -----------
    """
    
    alienC: str = "\033[0;32;40m"        # vert fond noir sans effet
    leVaisseauC: str = "\033[0;31;40m"   # rouge fond noir sans effet
    normalC : str = "\033[0;37;40m"      # blanc fond noir sans effet

    # affichage aliens et vaiseau
    """
    -----------
    Procedure: On va afficher les aliens lignes apres lignes puis lorque on aura atteint le bout du plateau on passera a la igne suivante etc... 
    Pour ca il faudra initialiser une variable affichage qui permetra d'afficher les aliens et lorques la position d'un alien corrrespondra on a 
    la position de la ligne ou de la colonne de la boucle alors on l'ajoutera a affichage, losrque on atteint la fin de la ligne on affichera la
    variable affichage et on la mettra de nouveau vide. A la dernier ligne on affichera la vaisseau qui est a la hauteur du plateau moins 1.
    -----------
    """
    
    
    affichage: str = ""
    for y in range(lePlateau['H']):             
        for x in range(lePlateau['L']):
            personnage : str = " "
            for aliens in lesAliens:
                if x == aliens['posx'] and y == aliens['posy']:
                    personnage = f'{alienC}@'
            if y == lePlateau["H"]-1 and x == leVaisseau["posx"]:
                personnage = f'{leVaisseauC}#'
            affichage += personnage
            
            #Affichage tir   
            
            """
            -----------
            Procedure: Pour afficher les tirs on va se servir de la boucle cree precedament comme ca lorque les coordonnées d'un tir correspondront on pourra
            les afficher sur le meme plateau que les aliens. Le vaisseau aillant plusieurs niveaux de tir il faut d'abord determine le niveau du tir.
            Les tirs du vaisseau seront cree entre le premier aliens se situant sur la meme colonne que le vaisseau et si le joueur appuye sur sa touche "o" sinon 
            on affichera pas de tire.
            *-----------
            """
            
            tir_affichage =" "
            niveau_tir : int = 2
            if posy_aliensatteignable != None:
                if niveau_tir == 1:
                    tir_affichage = ":"
                elif niveau_tir == 2:
                    tir_affichage = "§"
                elif niveau_tir == 3:
                    tir_affichage = "_"
                    
                if y <lePlateau['H']-1 and y > posy_aliensatteignable:
                    if x == leVaisseau['posx']-1 and aTire == True:
                        affichage +=tir_affichage
        print(affichage)
        affichage = ""
    print("\033[0;37;40m")
    print("-" * 40)



            
            
def generationaliens(lePlateau: Dict, lesAliens: List[Dict[str, int]]):
    
    """
    -----------
    Cette focntion genere les aliens en fonction de leurs nombre et du nombre d'aliens par ligne, certain de ces aliens auront un tir 
    
    -----------
    Procedure: On devra pour cela initialiser un nombre d'aliens en fonction du niveau, le nombre d'aliens par ligne,
    la ligne courante et le nombre d'aliens par ligne. Puis on devra faire une boucle qui ira jusq'au nombre d'aliens,
    On definira la posx d'un alien de facon a ce que la ligne d'alien soit centrer au plus pres de la moitie de la longueur L du plateau,
    les aliens devront bien respecter le nombre aliens par ligne et parmit ces aliens certaint on a un tir .
    A chaque fois que on aura atteint le nombre d'alien par ligne on devra passer a la ligne suivant. La ligne definira la position y.
    AVant de recommencer la boucle on ajoute le dictionnaire a la fin de la liste.
    
    -----------
    Parametre: Le dictionnaire du Plateau de jeu et la liste des aliens
    
    -----------
    """
    nbAliens: int = lePlateau['level']*20+10
    nbAliensLigne: int = 10
    LigneCourante: int = 0
    nbAliensAvecTirs: int = 5
    i: int
    for i in range(nbAliens):                       # pour la creation du dictionnair aliens
        aliens: Dict[str, int] = dict()             # initialisation dictionnaire vide
        if i % nbAliensLigne == 0:                    # saut a la ligne des que on atteint 10 aliens sur une ligne
            LigneCourante = LigneCourante + 1
            
            
        # ajout des nouvelles données au dictionnaire aliens
        aliens['posx'] = i % nbAliensLigne + lePlateau["L"] // 2 - nbAliensLigne // 2
        aliens['posy'] = LigneCourante
        aliens["sens"] = 0
        aliens["tir"] = 0
        
        # ajout du dictionnaire aliens dans la liste lesAliens
        lesAliens.append(aliens)

    # utilisation de sample de la bibliotheque random qui permet de prendre un sous effectif d'un effectif
    
    AliensAvecTirs: List[int] = sample(lesAliens, nbAliensAvecTirs)
    for aliens in AliensAvecTirs:
        
        # utilisation de randint qui permet de choisir aleatoirement des chiffres entre 2 et 3
        aliens['tir'] = randint(2, 3)

    # affichage claire de la liste des Aliens
    
    """
    print('Les Aliens: \n')
    for car in lesAliens:
        print('-en position (', car['posx'], ',',car['posy'], ') -tir', car['tir'])
    """

   

def deplacerAliens(lesAliens : List[Dict[str,int]],lePlateau : Dict[str,int]):
    """
    ----------
    Cette fonction deplace les aliens
    
    ----------
    Pocedure: On va d'abord regarder qu'il y a des aliens a deplacer pour cela on verifie que la liste des aliens et differentes de 0. On va ensuite 
    determiner l'aliens qui a la position x minimale et maximale. Si les aliens avancent vers la droite alors la position de toute la liste des aliens avancera
    sa posx augmente de 1 jusqu'a atteindre le la longueur du plateau et invercement si ils vont vers la gauche, on enlevera 1 a toute les position x des aliens 
    jusqu'a atteindre le bout du plateau. Lorsque les aliens atteignent le bout d'un des cote du plateau il faudra evidamment que il passe a la ligne suivant pour cela on 
    a ajoutera 1 a la posy. Il faudra aussi que les aliens reste a la meme posx pendant 2 generations comme ca lorsqu'il descend d'un etage il reste a la meme posx ca les
    aliens   cree une variable etage qui lorque la position x a atteint a bout est egale a vrai. Alors si etage est vrai en fonction du sens des aliens on enlevera ou ajoutera un 
    a tout les pour qu'ils puissent rester a la meme place et remetra etage comme false.
    
    ---------
    Parametre: Les paramtres seront la listes de dictionnaire des Aliens qu'on devra deplacer et le Plateau du jeu qui nous pemet d'avoir les information sur le plateau
        
    ----------

    """
    if len(lesAliens) != 0:
        
        #initialisation maxi et mini
        
        maxi : int = lesAliens[0]['posx']           
        mini : int = lesAliens[-1]['posx']
        etage : bool = False
        for aliens in lesAliens:
            if maxi < aliens['posx']:
                maxi = aliens['posx']
            if mini >aliens['posx'] :
                mini = aliens['posx']
            
        if etage == True:
            if lesAliens[0]["sens"] == 1:
                for aliens in lesAliens:
                    aliens['posx'] +=1
                etage = False
                
                
      
            elif lesAliens[0]['sens'] == 0:
                for aliens in lesAliens:
                    aliens['posx'] -=1
                etage = False
               
                
            
        elif lesAliens[0]["sens"] == 0 :
            for aliens in lesAliens:
                if maxi >= lePlateau['L']-1:
                        aliens["sens"] = 1 
                        aliens['posy'] += 1
                        etage = True
                else:
                    aliens['posx'] += 1
                
            
        elif lesAliens[0]['sens'] ==1 :
            for aliens in lesAliens:
                if  mini < 1:
                        aliens['sens'] = 0
                        aliens['posy'] += 1
                        etage = True
                else:
                    aliens['posx'] -= 1



def actionSurVaisseau(leVaisseau : Dict[str,int],action : str,lePlateau : Dict[str,int])-> bool :
    """
    ----------
    Cette fonction va en fonction de la variable action deplacer le vaisseau ou retourner vrai siaction est agale a "o" 
    
    ----------
    Procedure: On va initialiser une vraible res qui sera fausse, si action est agale a "k" alors on se deplacera vers la droite si action est agale a m alors vers la gauche
    lorsqu on deplace le vaisseau il faut rajouter la condition que si on est au bord du plateau alors on n'avance pas. Si action est egale a "o" alors on dire que res est 
    vrai c'est a dire que le joueur a tire
        
    ----------
    Parametre: Les parametres de cette fonction sont le dictionnaire du Vaisseau et du Plateau
    
    ----------
    Retourn: La fonction retourne vrai si action est agale a "o" c'est a dire que le joueur a tire sinon faux
    
    ----------
    """
    
    res  : bool = False
    if action == 'k':
        if leVaisseau['posx']<lePlateau['L']-1:
            leVaisseau['posx'] += 1 
    elif action == 'm':
        if leVaisseau['posx']> 0:
            leVaisseau['posx'] -= 1
    elif action == 'o':
        res = True
    return res

def findelapartie(leVaisseau : Dict[str,int],lesAliens : List[Dict[str,int]],lePlateau : Dict[str,int])->bool:
    """
    ----------
    Cette fonction retourne vrai si la partie est finie c'est a dire si on a tué tout les aliens ou si un alien a atteint la ligne du vaisseau
    
    ----------
    Procedure: On va verifier si la liste des aliens est egale a zero ou si un alien est sur le meme ligne que le vaisseau
    
    ----------
    Parametre: Les dictionnaire du Vaisseau et du Plateau et la liste des dictionnaire les Aliens
        
    ----------
    Retourne: Cette fonction retourne vrai quand l'une de ces 2 cinitions est respecté
    ----------
    """
    
    res : bool = False
    if len(lesAliens)==0:
        res = True
    else:
        for aliens in lesAliens:
            if aliens["posy"]== lePlateau['H']-1:
                res = True

    return res

def AlienAtteignable(lesAliens : List[Dict[str,int]],posx : int)-> int or None:
    """
    ----------
    Cette fonction determine si un alien est attiignable par le tire du vaisseau c'est a dire qu'il est sur la meme colonne que lui
    
    ----------
    Pocedure: Cette fonction retourne none si aucun alien et sur la meme posx que le vaisseau et sinon retourne la posy de l'alien le 
    plus bas sur la meme ligne que le Vaisseau.  Pour cela on initialisera res comme etant egale a Non. Puis cela on cree une boucle de 
    la liste des dictionnaire des aliens, dans laquelle on va metre la condition que si un alien a la meme posx que le Vaisseau, on afffectera
    la posy a la variable res.
    
    ----------
    Parametre: Cette fonction prend en parametre la liste de dictionnaire des aliens et la posx du Vaiseau
    
    ----------
    Retourne: Cette fonction retourne none si aucun alien est sur le meme colone que le Vaisseau sinon la position y du premiere alien atteignable
    
    ----------
    """
    
    res : int = None
    for aliens in lesAliens:
        if aliens['posx'] == posx:
            res = aliens['posy']
    return res


def gestion_tir(leVaisseau : Dict,lesAliens : Dict,alienAtteignable : int)-> int:
    """
    ----------
    Cette fonction tuera les aliens lorsque le vaisseau tirera
    
    ----------
    Procedure: Pour cela on va cree une boucle qui va faire l'ensemble de la liste des dictionnaire des aliens verier que la position y de l'alien
    est la meme que c'elle de l'alien atteignable,si c'est le cas on vas ensuite verifier que l'alien est sur la meme colonne que le vaisseau.
    Si c'est le cas on supprime l'alien de la liste et on ajoute un on nombre d'alien tues
        
    ----------
    Parametre: La fonction prend en parametre le dictionnaire du Vaisseau et l'alienAtteignable qui est un entier
    
    ----------
    Retourne: La fonction retourne le nombre d'aliens tuees
    
    ----------
    """
    
    nbAliens_tues : int = 0
    for aliens in lesAliens:
        if aliens['posy']== alienAtteignable:
            if aliens['posx'] == leVaisseau['posx']:
                lesAliens.remove(aliens)
                nbAliens_tues +=1
    return nbAliens_tues
    

if __name__ == "__main__":
    os.system('cls')
    
    # information jeu creation dictionnaire
    lePlateau: Dict[str, int]  # declaration variable
    lePlateau = {'L': 25, 'H': 20, 'score': 0, 'vie': 3,'level': 1}  # initialisation variable

    #assert verifiant que la variable lePlateau est un doctionnaire et que il a comme clée L,H,vie,score,level
    assert type(lePlateau) == dict
    assert set(lePlateau.keys()) == {"L", "H", "vie", "score","level"}
    
    
    # Liste de dictionnaire les aliens
    lesAliens: List[Dict[str, int]] = []  # declaration de la liste des aliens vide
    
    #assert lesAliens
    assert type(lesAliens) == list     #les aliens sont une liste
    assert len(lesAliens) == 0      #les aliens est une liste vide
    
    # information lePlateau
    leVaisseau: Dict = {str, int}  # declaration dictionnaire
    
    # initialisation du dictionnaire leVaisseau
    leVaisseau = {'posx': lePlateau['L'] // 2, 'tir': 1}    

    #assert de la bonne creation du dictionnaire leVaisseau et des cleés du dictionnaire
    assert type(leVaisseau) == dict #la variable est un dictionnaire
    assert set(leVaisseau.keys()) == {'posx','tir'}
    
    #assert sur le deplacement du leVaisseau
    assert actionSurVaisseau(leVaisseau, 'o',lePlateau) == True
    assert actionSurVaisseau(leVaisseau, 'k' or 'm',lePlateau) == False
    
    #assert sur la fonction AlienAtteignable si on prend la liste des aliens au debut du jeu et la position x du vaisseau au debut aussi
    #pour cela il faut generer les aliens
    generationaliens(lePlateau, lesAliens)
    
    assert AlienAtteignable(lesAliens,leVaisseau['posx']) == 3

    
    partieFinie : bool = False
    action : str = "x"
    score : int =0
    kb = SaisiCar()
    res : bool= False
    
    
    #Boucle principale du jeu
    while res != True:                                                          #on ne quitte pas cette boucle tant que le jeu n'est aps finit
        while partieFinie == False and action != "q":                           #boucle pour les manches
            action = kb.recupCar(['m','o','k','q'])                             
            aTire = actionSurVaisseau(leVaisseau, action,lePlateau)
            alienAtteignable = AlienAtteignable(lesAliens,leVaisseau['posx'])
            affichagePlateau(lePlateau, leVaisseau, lesAliens,aTire,alienAtteignable)
            if aTire == True:
                
                #si le joueur tire alors si des ou un alien(s) est sur la mem colonne que le vaisseau, on tuera le premiere alien atteignable
                nbAliens_tues=gestion_tir(leVaisseau, lesAliens, alienAtteignable)
                
                #haque aliens tues valent 5 points, on ajoutera ces points au score au niveau des informations du jeu
                score += nbAliens_tues      
                lePlateau['score'] = score *5
                
            deplacerAliens(lesAliens, lePlateau)
            partieFinie = findelapartie(leVaisseau, lesAliens, lePlateau)
            time.sleep(0.005)
            #os.system('clear')
            os.system('cls')
            
        #si la manche est finie on verifie si la manche c est finie car tout les aliens ont ete tuer
        if len(lesAliens) ==0 and partieFinie == True :
            #si oui on ajoute un niveau a la partie et on reinitialise les aliens avec un plus grand effecif proportionel au niveau et on reinitialise le vaisseau 
            partieFinie : bool = False
            lePlateau['level'] +=1
            generationaliens(lePlateau, lesAliens)
            leVaisseau = {'posx': lePlateau['L'] // 2, 'tir': 1}
            
        #sinon on verifie si la manche c'est finie car un aliens a atteint la ligne du vaisseau
        elif len(lesAliens) != 0 and partieFinie == True:
            #si oui on redemarre une autre manche en reinitilisant le vaisseau, les aliens et on enleve une vie au joueur
            partieFinie : bool = False
            lePlateau['vie'] -=1
            lesAliens: List[Dict[str,int]]=list()
            generationaliens(lePlateau, lesAliens)
            leVaisseau = {'posx': lePlateau['L'] // 2, 'tir': 1}
        
        #on verifie si le joueur a encore des vies ou si le joueur veut quitter le jeu
        if action == "q" or lePlateau['vie'] < 0:
            res =True