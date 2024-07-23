import os
import duckdb

def PokeBaseConnection():
    path = os.path.dirname(os.path.realpath(__file__))
    con = duckdb.connect(f"{path}/pokebase.db")

    return con



