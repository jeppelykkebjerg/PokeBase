from airflow.decorators import dag, task
from dotenv import load_dotenv
import os
import pokemontcgsdk
import pandas as pd
import uuid
from datetime import datetime

# Define the basic parameters of the DAG, like schedule and start_date
@dag(
    start_date=datetime(2024, 8, 1),
    schedule="@daily",
    catchup=False,
    default_args={"owner": "Jeppe Lykkebjerg Jensen", "retries": 3},
    tags=["ingestion"],
)
def ingest_pokemontcgioapi_get_all_cards():
    # Load environment variables
    load_dotenv()
    POKEMONTCG_IO_API_KEY = os.getenv("POKEMONTCG_IO_API_KEY")
    
    # script variables
    pokemontcgioapi_object = 'cards'

    @task
    def get_cards():
        pokemon_cards_list = pokemontcgsdk.Card.all()
        pokemon_cards_df = pd.DataFrame(pokemon_cards_list)

        return pokemon_cards_df
    
    @task
    def write_cards_dataframe_to_json(data_frame, pokemontcgioapi_object, uuid):
        #Persist as json file
        df = data_frame
        #Persist as json file
        write_path = f'/usr/local/airflow/data/pokemontcgioapi/{pokemontcgioapi_object}'

        # Check if the directory already exists
        if not os.path.exists(write_path):
            os.makedirs(write_path)
            print(f"{write_path} created successfully!")

        write_path_json = f'{write_path}/{pokemontcgioapi_object}_{uuid}.json'
        df.to_json(write_path_json, orient='records')

    # Invoke functions to create tasks and define dependencies
    pokemon_cards_df = get_cards()
    write_cards_dataframe_to_json(pokemon_cards_df, pokemontcgioapi_object, uuid.uuid4())

# Instantiate the DAG
ingest_pokemontcgioapi_get_all_cards()