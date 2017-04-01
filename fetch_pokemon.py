import requests
import json
import pprint


def get_pokemon(index):
    output = requests.get("http://pokeapi.co/api/v2/pokemon/" + str(index))
    return json.loads(output.content.decode('utf-8'))


def get_name(pokemon):
    name = pokemon["name"]
    return name


def get_pokemon_abilities(pokemon):
    abilities = pokemon['abilities']
    return abilities


def get_first_ability(pokemon):
    ability = pokemon[0]['ability']['name']
    return ability


def get_ability_from_ability_name(pokemon, ability_name):
    pokemon_abilities = get_pokemon_abilities(pokemon)
    abilities_length = len(pokemon_abilities)
    i = 0
    while i < abilities_length:
        if pokemon_abilities[i]['ability']['name'] == ability_name:
            return pokemon_abilities[i]
        i += 1
    return 'not found'


def main():
    pprint.pprint(get_ability_from_ability_name(get_pokemon(150), 'pressure'))


if __name__ == '__main__':
    main()



