import db_connection as dbcon

con = dbcon.PokeBaseConnection()

sql = """
    SELECT * FROM 'D:/DataEngineering/PokeBase/database/testdata/pokemon_characteristics.json';

"""

print(con.execute(sql).fetchall())
con.close()