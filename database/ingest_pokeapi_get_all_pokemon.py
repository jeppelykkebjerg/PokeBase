import requests
import db_connection as dbcon

def get_all_pokemon() -> list:
    """
        Consider persisting the raw json to avoid data loss. For a later iteration.
        DuckDB can also easily read from JSON files and import them.
    """

    #Create get request url
    pokeapi_base_url = "https://pokeapi.co/api/v2/"
    pokeapi_endpoint = "pokemon"
    pokeapi_parameters = "?limit=100000"
    pokeapi_get_url = pokeapi_base_url+pokeapi_endpoint+pokeapi_parameters

    #Fetch data
    response = requests.get(pokeapi_get_url)
    data = response.json()

    # Extract data
    pokemon_list = [
        (pokemon["name"], pokemon["url"]) for pokemon in data["results"]
    ]

    return pokemon_list


def insert_into_pokemon(data: list, table_name: str):
    sql = f"""
        INSERT INTO {table_name} (name, url)
        VALUES(?,?)
    """

    con = dbcon.PokeBaseConnection()
    con.executemany(sql, data)

    return

if __name__ == "__main__":
    pokemon_list = get_all_pokemon()
    insert_into_pokemon(pokemon_list, "pokemon")
    

