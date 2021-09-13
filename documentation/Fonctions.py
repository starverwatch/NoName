"""
Les fonctions sont des blocs de commandes qui permettent de rendre plus efficace le code
Ils seront là dés qu'il y a lieu de répétition dans les codes
"""

# On crée la fonction chat qui va permettre de savoir qui à dit quoi
def chat(name,message): # Il y a ici deux paramettre: le nom et le message de la personne
    print("[{}] : {}".format(name,message)) # On va récupérer les deux variables introduitent et les travailler dans la fonciton

# Ici on appelle la fonction créer ci-dessus et on lui donne des valeurs pour ces variables
chat("Alexis","Bonjour à tous") # L'affichage sera donc : [Alexis] : Bonjour à tous

# Voici quelques autres exemples :

def auto_goodbye(): # ici aucun paramettre n'es à ajouter, donc il n'y aura pas de variables à travailler
    print("Au revoir les amis :)")

auto_goodbye() # appelle de la fonction auto_goodbye

def addition(*nbre, tot=0): # ici on peut ajouter un nombre infini de nombre et on déclare une variable tot
    for a in nbre: # on créer ensuite une boucle qui se répète autant de fois qu'il y a de nombres
        tot = tot+a # par la suite on additionne tout les nombre entre eux grâce à la variable tot
    print("Voici le résultat : "+tot) # on affiche ensuite le résultat

addition(1,2,3,4) # appelle de la fonction addition et attribution de variables