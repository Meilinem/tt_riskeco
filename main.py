from hive import Hive
from random import randrange
from print_functions import print_bee_infos

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
        if hive.n_bees <= 0:
            if bee.b_type == "queen":
                print("------> QUEEN DIES <------")
            else:
                print("------> NO MORE BEE LEFT <------")
            end_game(hive)
        del bee
        del hive.hive_state[idx]
        print("------>  NUMBER OF BEES LEFT <------", hive.n_bees)

def     hit(hive):
    idx = randrange(hive.n_bees)
    for i, n in enumerate(hive.hive_state):
        if i == idx:
            bee = n
            break
    bee.hit()
    bee_state(hive, bee, idx)
    print_bee_infos(bee, idx)

def     init(hive):
    lst = hive.hive_info.keys()

    for b_type in lst:
        n = hive.get_n_bee(b_type)
        for i in range(n):
            hive.add_bee(b_type)

def     start():
    auto = 1
    hive = Hive()
    init(hive)

    print("Let's start this little non ecologic game")
    mode = input("Choose your mode : manual [0] or auto [1]")
    if mode == 0:
        auto = 0

    while hive.n_bees > 0:
        if auto == 0:
            c = input("Hit a random bee ? [y/n]")
            if (c == 'y'):
                print()
                hit(hive)
        else:
            print()
            hit(hive)

def     main():
    start()

if __name__ == "__main__":
    main()
