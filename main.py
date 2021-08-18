import random

cartes = [""]*104

def carte():
        while True:
            alea = random.randint(0, 103)
            carte = cartes[alea]
            if carte != 0:
                cartes[alea] = 0
                break

        return carte

#distribution des cartes aux joueurs
def distribution(nbplayer):
    for x  in range (0, 104): #boucle de creation des cartes du jeux
        cartes[x] = str(x+1)

    player=nbplayer*[None]
    for carteplayer in range(len(player)):
        player[carteplayer]=11*[0]


    for p in range(nbplayer):
        for n in range(10): #don des cartes du jeux au joueur
            player[p][n] = carte()

    return player

def table():
    table = 4*[None]
    for jeuxmep in range(len(table)):
        table[jeuxmep]=6*[None]

    for cartedepart in range(4):

        table[cartedepart][0] = carte()

    return table



def demandeDepoDeCarte(qui, dataP):
    print("Vos cartes sont:")
    for nbcarte in range(10):
        if dataP[qui][nbcarte] == '0':
            break
        print(str(nbcarte + 1) +': '+ dataP[qui][nbcarte])

    quellecarte = input('joueur' + str(qui+1) + ' quelle carte joue tu? : \n--> ')
    quellecarte = int(quellecarte)
    quellecarte = quellecarte - 1



    return quellecarte






def loop(nbjoueur ):

    dataPlayers = distribution(nbjoueur)
    game = table()
    tourDepoCarte = 0
    carteSelectione = [0]*nbjoueur
    for tourDepoCarte in range(0, nbjoueur):
        for classified in range(30):
            print('.')
        thecarte = demandeDepoDeCarte(tourDepoCarte, dataPlayers)
        temp = dataPlayers[tourDepoCarte][thecarte]

        carteSelectione[tourDepoCarte] = temp
        dataPlayers[tourDepoCarte][thecarte] = None

        
        print(dataPlayers)
        print()
        print(game)













loop(2)
