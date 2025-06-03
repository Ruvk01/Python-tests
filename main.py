import requests

Host = 'https://api.pokemonbattle.ru'
Token = '13040790da5c36e29fb982c7d7b03c96'
Header = {
    'Content-Type' : 'application/json', 
    'trainer_token' : Token
}

BodyCreation = {
    "name": "generate",
    "photo_id": -1
}

ResponseCreation = requests.post(url = f'{Host}/v2/pokemons', headers = Header, json = BodyCreation)
print(ResponseCreation.text)

Pokemon_id = ResponseCreation.json()['id']
print(Pokemon_id)




BodyChange = {
    "pokemon_id": Pokemon_id,
    "name": "generate",
    "photo_id": -1
}

ResponseChange = requests.put(url= f'{Host}/v2/pokemons', headers = Header, json = BodyChange)
print(ResponseChange.text)


BodyCatch = {
    "pokemon_id": Pokemon_id,
}

ResponseCatch = requests.post(url= f'{Host}/v2/trainers/add_pokeball', headers = Header, json = BodyCatch)
print(ResponseCatch.text)