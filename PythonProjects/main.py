import requests
import json

token = 'e3d495ddbc6f15ce5aecd949aeefabe6'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'trainer_token': token}, json = {"name": "Пушок",
"photo": "https://purepng.com/public/uploads/large/purepng.com-pokemonpokemonpocket-monsterspokemon-franchisefictional-speciesone-pokemonmany-pokemonone-pikachu-1701527785665cjc7g.png"
})
print(response.text)

response = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'trainer_token': token}, json = {"pokemon_id": "5472",
"name": "Алекс", "photo": "https://purepng.com/public/uploads/large/purepng.com-pokemonpokemonpocket-monsterspokemon-franchisefictional-speciesone-pokemonmany-pokemonone-pikachu-1701527785665cjc7g.png"
})
print(response.text)

response = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'trainer_token': token}, json = {"pokemon_id": "5472"
})
print(response.text)