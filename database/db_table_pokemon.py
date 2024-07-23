import db_connection as dbcon

con = dbcon.PokeBaseConnection()

sql = """
    CREATE TABLE IF NOT EXISTS pokemon
    (
    	name Text,
    	url Text,
    	inserted_at Datetime DEFAULT current_timestamp
    )
"""

con.execute(sql)
con.close()