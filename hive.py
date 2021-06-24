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
            "n": 5,
        },
        "drone": {
            "hp": 50,
            "damage": 12,
            "n": 8,
        }
    }
    hive_state = []
    init_bees = 14
    n_bees = 14

    def     __intit__(self):
        pass

    def    add_bee(self, b_type):
        if b_type not in self.hive_info.keys():
            raise ValueError("This bee type does not exist")
        new_bee = Bee(self.hive_info[b_type]["hp"], self.hive_info[b_type]["damage"], b_type)
        self.hive_state.append(new_bee)

    def     get_n_bee(self, b_type):
        return self.hive_info[b_type]["n"]
