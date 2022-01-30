import numpy
import random
# il topo evita i gatti, e in caso di necessità spara(anche diagonalmente)
# i gatti si muovono in direzione del topo con movimenti alternatini(verticali e orizzontali)
# se i gatti raggiungono il topo, esso viene ucciso e l'episodio termina

# Effetti delle azioni:
# ad ogni azione risulterà il movimento dell'agente topo

#Reward: -1 per ogni azione movimento
         #+100 per formaggio mangiato
         #-1000 per topo ucciso
         #spara ha un reward di -10 se non viene ucciso nessun gatto, e +10 per ogni gatto ucciso


# Stop condition: topo mangia formaggio, massimo numero di azioni, o topo ucciso


def generate_grid(m, n, num_gatti):
    #set a seed for the random number generator
    random.seed(1)


    # 5 possibili azioni per l'agente topo, su, giù, destra, sinistra, e spara
    q_values = numpy.zeros((m, n, 5))
    #inizializzo una seconda matrice con reward di -1
    reward = numpy.full((m, n), -1)
    #generate random integer between 0 and 4
    intervallo = m*n
    for elem in range(num_gatti):
        #generate random integer between 0 and intervallo-1
        x = random.randint(0, intervallo-1)
        #calculate the row and column of the gatto
        row = x // n
        column = x % n
        #in questa posizione c'è un gatto
        reward[row, column] = -1000
    reward[m-3, n-1] = 100
    return q_values, reward



# create main function
def main():
    q_values, reward = generate_grid(10, 10, 2)
    print(reward)



if(__name__ == "__main__"):
    main()