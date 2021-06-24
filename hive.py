from bee import Bee

class   Hive:
    hive_info = {
        "queen": {
            "hp": 100,
            "damage": 8,
            "n": 1,
        },
         "worker": {
            "hp": 70,
            "damage": 10,
            "n": 2,
        },
        "drone": {
            "hp": 50,
            "damage": 12,
            "n": 3,
        }
    }
    hive_state = []
    init_bees = 0
    n_bees = 0

    def     __init__(self):
        self.init_bees = 14
        self.n_bees = 5
        self.hive_state = []
        lst = self.hive_info.keys()

        for b_type in lst:
            n = self.get_n_bee(b_type)
            for i in range(n):
                self.add_bee(b_type)

    def    add_bee(self, b_type):
        if b_type not in self.hive_info.keys():
            raise ValueError("This bee type does not exist")
        new_bee = Bee(self.hive_info[b_type]["hp"], self.hive_info[b_type]["damage"], b_type)
        self.hive_state.append(new_bee)

    def     get_n_bee(self, b_type):
        return self.hive_info[b_type]["n"]
