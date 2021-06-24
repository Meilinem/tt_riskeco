from hive import Hive
from random import randrange
from print_functions import print_bee_infos

def     print_hive(hive):
    print(f"BEES LEFT {hive.n_bees} -------------")
    for n, bee in enumerate(hive.hive_state):
        print(f"BEE {n} -- \
        TYPE : {bee.b_type} \
        HP : {bee.hp}")
        print()

def     end_game(hive):
    del hive
    print("GAME OVER")
    c = input("Play again ? [y/n]")
    if c == 'y':
        print("===================")
        print()
        start()
    exit(0)

def     bee_state(hive, bee, idx):
    if bee.hp <= 0:
        hive.n_bees -= 1
        print(f"------>  NUMBER OF BEES LEFT {hive.n_bees}<------")
        if bee.b_type == "queen":
            print("------> QUEEN DIES <------")
            end_game(hive)
        if hive.n_bees <= 0:
            print("------> NO MORE BEE LEFT <------")
            end_game(hive)
        del hive.hive_state[idx]

def     hit(hive):
    idx = randrange(hive.n_bees)
    for i, n in enumerate(hive.hive_state):
        if i == idx:
            bee = n
            break
    bee.hit()
    print_bee_infos(bee, idx)
    bee_state(hive, bee, idx)

def     start():
    hive = Hive()
    i = 0

    print_hive(hive)
    print("Let's start this little non ecologic game")
    while hive.n_bees > 0:
        print(i)
        i += 1
        #c = input("Hit a random bee ? [y/n]")
        #if (c == 'y'):
        #    print()
        hit(hive)

def     main():
    start()

if __name__ == "__main__":
    main()
