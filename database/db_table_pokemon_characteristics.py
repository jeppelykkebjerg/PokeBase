import db_connection as dbcon

con = dbcon.PokeBaseConnection()

sql = """
    CREATE TABLE IF NOT EXISTS pokemon_characteristics
    (
    	url Text,
        characteristics JSON,
    	inserted_at Datetime DEFAULT current_timestamp
    )
"""

con.execute(sql)
con.close()