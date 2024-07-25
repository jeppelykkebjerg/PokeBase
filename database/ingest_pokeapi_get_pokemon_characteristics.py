import db_connection as dbcon
import requests
import json

def get_pokemon_characteristics_url(connection):
    sql = """
        SELECT 
        	ROW_NUMBER() OVER(PARTITION BY name ORDER BY inserted_at DESC) as row_num,
        	* 
        FROM Pokemon 
        QUALIFY row_num = 1
        ORDER BY inserted_at
    """
    #return result as pandas dataframe
    df = con.execute(sql).fetch_df()

    return df

def get_pokemon_characteristics(url) -> list:
    url = url

    response = requests.get(url)
    data = json.dumps(response.json())

    pokemon_characteristics_list = [
        url,
        data
    ]

    return pokemon_characteristics_list

def insert_pokemon_characteristics(con, data: str, table_name: str):
    url = data[0]
    characteristics = data[1]
    
    sql = f"""
        INSERT INTO {table_name} (url, characteristics)
        VALUES('{url}','{characteristics}')
    """

    con = dbcon.PokeBaseConnection()
    con.execute(sql)
    
    return



if __name__ == "__main__":
    con = dbcon.PokeBaseConnection()

    df_pokemon_url = get_pokemon_characteristics_url(con)

    for row in df_pokemon_url.itertuples(index=True, name='Pandas'):
        print(f'Fetching data from: {row.url} ')
        pokemon_char_data = get_pokemon_characteristics(row.url)

        insert_pokemon_characteristics(con, pokemon_char_data, "pokemon_characteristics")




    
