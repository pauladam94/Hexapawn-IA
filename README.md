Le jeu Hexapawn est comme les échecs mais avec les 3 pions de chaque camp de cette manière :

X_________X

X_________X

X_________X
le joueur qui n'a pas plus de pions || qui laisse passer un pion adverse || n'a plus de coup à jouer a perdu.

Ce projet très simple est un outils pour expliquer le fonctionnement d'une IA aux plus jeunes.
Je l'ai utiliser pour expliquer cette notion complexe à mes petits cousins.

Le principe est de jouer contre un ordinateur à une version très simplifié des échecs (3 pions
contre 3 pions), à chaque partie l'ordinateur apprend à mieux jouer.
Même si l'exemple est ici assez simple, il faut quand même coder chaque position pour pouvoir
retrouver facilement en temps constant les positions jouer précédemment. Le plus efficace est 
d'utiliser des structures d'arbres.
L'adversaire(IA) construit un graphe des positions et retient quand une position est gagnant ou 
perdante. Lors d'une partie, l'adversaire parcourt son graphe de partie déjà joué, si il atteint
un nœud sans fils du graphe, il joue aléatoirement sinon il joue un coup considéré gagnant.

Cela m'a aussi permis de travailler sur la sauvegarde de données qui doivent être conserver et
facilement accessible d'un run à l'autre du programme.
