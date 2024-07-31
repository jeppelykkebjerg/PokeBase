import db_connection as dbcon

con = dbcon.PokeBaseConnection()

view_name = "sprites"

sql = f"""
    CREATE OR REPLACE VIEW prep_pokemon_{view_name} AS 
    SELECT 
		url,
        json_extract(characteristics , '$.sprites.back_default') as sprites_back_default, 
		json_extract(characteristics , '$.sprites.back_female') as sprites_back_female, 
		json_extract(characteristics , '$.sprites.back_shiny') as sprites_back_shiny, 
		json_extract(characteristics , '$.sprites.back_shiny_female') as sprites_back_shiny_female, 
		json_extract(characteristics , '$.sprites.front_default') as sprites_front_default, 
		json_extract(characteristics , '$.sprites.front_female') as sprites_front_female, 
		json_extract(characteristics , '$.sprites.front_shiny') as sprites_front_shiny, 
		json_extract(characteristics , '$.sprites.front_shiny_female') as sprites_front_shiny_female
	FROM pokebase.main.pokemon_characteristics pc;
"""

con.execute(sql)
con.close()
 