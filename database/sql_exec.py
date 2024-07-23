import db_connection as dbcon

con = dbcon.PokeBaseConnection()

sql = """
    TRUNCATE table pokebase.main.pokemon_characteristics;

"""

con.execute(sql)
con.close()