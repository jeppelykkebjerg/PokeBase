from dotenv import load_dotenv
import os
import pokemontcgsdk
import pandas as pd
import uuid

#Load environment variables
load_dotenv()

POKEMONTCG_IO_API_KEY=os.getenv("POKEMONTCG_IO_API_KEY")

# script variables
pokemontcgioapi_object = 'cards'

def get_object():
     #Get all cards
     pokemon_cards_list = pokemontcgsdk.Card.where(q='cardmarket.updatedAt:2024\/08\/02')
     pokemon_cards_df = pd.DataFrame(pokemon_cards_list)

     return pokemon_cards_df

def write_dataframe_to_json(data_frame, pokemontcgioapi_object, uuid):
     df = data_frame
     #Persist as json file
     write_path_parent = os.path.dirname(os.path.realpath(__file__))
     write_path = f'{write_path_parent}/datalake/pokemontcgioapi/{pokemontcgioapi_object}/incremental'

     # Check if the directory already exists
     if not os.path.exists(write_path):
          os.makedirs(write_path)
          print(f"{write_path} created successfully!")

     write_path_json = f'{write_path}/{pokemontcgioapi_object}_{uuid}.json'

     df.to_json(write_path_json, orient='index')

if __name__ == "__main__":
     pokemon_cards_df = get_object()
     # write_dataframe_to_json(pokemon_cards_df, pokemontcgioapi_object, uuid.uuid4())
     print(pokemon_cards_df.shape[0])