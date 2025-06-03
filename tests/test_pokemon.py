import requests
import pytest


Host = 'https://api.pokemonbattle.ru'
Token = '13040790da5c36e29fb982c7d7b03c96'
Header = {
    'Content-Type' : 'application/json', 
    'trainer_token' : Token
}



def test_status_code():
    response = requests.get(url = f'{Host}/v2/trainers')
    assert response.status_code == 200

Trainer_id = '33813'

def test_trainer_name():
    response_name = requests.get(url = f'{Host}/v2/trainers', params = {'trainer_id': Trainer_id})
    assert response_name.json()["data"][0]["trainer_name"] == 'Андроник Цефалон'