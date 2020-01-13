# reduce, range
import requests

rick_morty_api = requests.get('https://rickandmortyapi.com/api/')


def rick_morty(*args):
    apis = [values for key, values in args[0].json().items()]

    # using map
    character_api, locations_api, episodes_api = map(lambda api: requests.get(api).json(), apis)
    return character_api, locations_api, episodes_api


def consumer():
    from functools import reduce
    characters, locations, episodes = rick_morty(rick_morty_api)
    is_alive = filter(lambda x: x['status'].lower() == 'alive', characters['results'])

    # seasons
    seasons = {value['episode'][:3]: [x['episode'] for x in episodes['results'] if x['episode'][:3] == value['episode'][:3]] for value in episodes['results']}

    # all characters
    all_characters = []
    for val, char in enumerate(characters['results'], 1):
        all_characters.append((val, char['name']))

    # characters still alive
    characters_alive = []
    for val, char in enumerate(list(is_alive), 1):
        characters_alive.append((val, char['name']))

    # zip illustration
    zipped = []
    for all_content in zip(characters['results'], locations['results'], episodes['results']):
        zipped.append(all_content)


consumer()
