class Char:
    def __init__(self, name, hp, mp, atk):
        self._name = name
        self._hp = hp
        self._mp = mp
        self._atk = atk

    def get_name(self):
        return self._name

    def get_hp(self):
        return self._hp

    def get_mp(self):
        return self._mp

    def get_atk(self):
        return self._atk

    def update_hp(self, hp_change):
        self._hp += hp_change

    def update_mp(self, mp_change):
        self._mp += mp_change

    def __str__(self):
        return f"name: {self._name}, hp: {self._hp}, mp:{self._mp}, atk: {self._atk}."


class Pokemon(Char):
    def __init__(self, name, hp, mp, atk, p_type):
        super().__init__(name, hp, mp, atk)
        self._p_type = p_type

    def get_type(self):
        return self._p_type

    def __str__(self):
        return super().__str__()[:-1] + f", type: {self._p_type}."


class Player(Char):
    def __init__(self, name, hp, mp, atk):
        super().__init__(name, hp, mp, atk)
        self._pokemons = []

    def display_pokemons(self):
        if len(self._pokemons) == 0:
            print("You have not caught any pokemons yet.")
        else:
            print("Here are the pokemons in your team:")
            for pokemon in self._pokemons:
                print(pokemon)
        print()

    def catch_pokemon(self, new_pokemon):
        for pokemon in self._pokemons:
            if pokemon.get_type() == new_pokemon.get_type():
                print("You already have:\n" + str(pokemon))
                print("Now you meet:\n" + str(new_pokemon))
                choice = input(
                    "Would you like to replace the pokemon of the same type? [Y/N]")
                if choice in "yY":
                    self._pokemons.remove(pokemon)
                    self._pokemons.append(new_pokemon)
                    print(
                        f"You have released {pokemon.get_name()}, and caught {new_pokemon.get_name()}.")
                else:
                    print(f"You choose not to catch {new_pokemon.get_name()}.")
                return

        self._pokemons.append(new_pokemon)
        print(f"You have caught {new_pokemon.get_name()}.")


def test_01():
    player = Player("Ash Ketchum", 100, 100, 20)
    pokemon_01 = Pokemon("Charmander", 50, 60, 18, "Fire")
    pokemon_02 = Pokemon("Squirtle", 55, 60, 15, "Water")
    pokemon_03 = Pokemon("Bulbasaur", 80, 60, 12, "Grass")
    pokemon_04 = Pokemon("Pikachu", 60, 60, 15, "Electric")
    pokemon_05 = Pokemon("Ponyta", 60, 60, 18, "Fire")

    print(player)

    player.display_pokemons()
    player.catch_pokemon(pokemon_01)
    player.catch_pokemon(pokemon_02)
    player.catch_pokemon(pokemon_03)
    player.catch_pokemon(pokemon_04)
    player.display_pokemons()
    player.catch_pokemon(pokemon_05)
    player.display_pokemons()


test_01()
