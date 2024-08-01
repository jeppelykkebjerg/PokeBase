from dotenv import load_dotenv
import os
import pokemontcgsdk
import pandas as pd
import uuid

#Load environment variables
load_dotenv()

POKEMONTCG_IO_API_KEY=os.getenv("POKEMONTCG_IO_API_KEY")

# script variables
pokemontcgioapi_object = 'sets'


def get_object():
#Get all sets
    pokemon_sets_list = pokemontcgsdk.Set.all()
    pokemon_sets_df = pd.DataFrame(pokemon_sets_list)

    return pokemon_sets_df

def write_dataframe_to_json(data_frame, pokemontcgioapi_object, uuid):
#Persist as json file
    df = data_frame
    #Persist as json file
    write_path_parent = os.path.dirname(os.path.realpath(__file__))
    write_path = f'{write_path_parent}/datalake/pokemontcgioapi/{pokemontcgioapi_object}'
    
    # Check if the directory already exists
    if not os.path.exists(write_path):
         os.makedirs(write_path)
         print(f"{write_path} created successfully!")

    write_path_json = f'{write_path}/{pokemontcgioapi_object}_{uuid}.json'

    df.to_json(write_path_json, orient='records')

if __name__ == "__main__":
     pokemon_sets_df = get_object()
     write_dataframe_to_json(pokemon_sets_df, pokemontcgioapi_object, uuid.uuid4())