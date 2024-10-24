import requests
import random

class PokemonService:
    BASE_URL = "https://pokeapi.co/api/v2"

    def get_pokemon_by_name(self, name):
        response = requests.get(f"{self.BASE_URL}/pokemon/{name}")
        if response.status_code == 200:
            pokemon_data = response.json()
            tipos = [tipo['type']['name'] for tipo in pokemon_data['types']]
            print(tipos)
            return {
                "data": [{
                    "name": pokemon_data["forms"][0]["name"],
                    "types": tipos
                }]
            }
        return {"error": "Pokemon not found"}
    
    def random_pokemon_type_filter(self, filter):
        if not filter:
            return {"error": "failed request"},400
        response = requests.get(f"{self.BASE_URL}/type/{filter}")
        if response.status_code == 200:
            type_info = response.json()
            pokemons = [poke['pokemon']['name'] for poke in type_info['pokemon']]
            pokemon = random.choice(pokemons)
            print('existe',pokemon)
            return self.get_pokemon_by_name(pokemon)
        return {"error": "Unable to fetch type Pokémon"}
    
    def long_name(self, filter):
        if not filter:
            return {"error": "failed request"},400
        response = requests.get(f"{self.BASE_URL}/type/{filter}")
        if response.status_code == 200:
            type_info = response.json()
            pokemon_mas_largo = ""
            for poke in type_info['pokemon']:
                nombre = poke['pokemon']['name']
                if len(nombre) > len(pokemon_mas_largo):
                    pokemon_mas_largo = nombre
            print(pokemon_mas_largo) 
            return self.get_pokemon_by_name(pokemon_mas_largo)
        return {"error": "Unable to fetch type Pokémon"}
        
    def filter_pokemon(self, filter_value):
        response = requests.get(f"{self.BASE_URL}/pokemon?limit=100000&offset=0")
        if response.status_code == 200:
            pokemon_list = response.json()["results"]
            filtered_pokemon = [pokemon for pokemon in pokemon_list if filter_value in pokemon["name"]]
            print(filtered_pokemon)
            random_pokemon = random.choice(filtered_pokemon)
            print("random",random_pokemon)
            pokemon_info = self.get_pokemon_by_name(random_pokemon["name"])
            return pokemon_info
        return {"error": "Unable to fetch Pokémon"}, 500
    
    def get_random_pokemon(self, filter, letras):
        if not filter:
            return {"error": "failed request"},400
        response = requests.get(f"{self.BASE_URL}/type/{filter}")
        if response.status_code == 200:
            type_info = response.json()
            pokemons = [poke['pokemon']['name'] for poke in type_info['pokemon']]
            filtrados = [p for p in pokemons if any(letra in p.upper() for letra in letras)]
            
            if filtrados:
                random_pokemon = random.choice(filtrados)
                return self.get_pokemon_by_name(random_pokemon)
            else:
                return {"error": "No Pokémon found with the specified letters"}
        
        return {"error": "Unable to fetch type Pokémon"}
