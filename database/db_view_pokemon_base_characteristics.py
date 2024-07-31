import db_connection as dbcon

con = dbcon.PokeBaseConnection()

view_name = "base_characteristics"

sql = f"""
    CREATE OR REPLACE VIEW prep_pokemon_{view_name} AS 
    SELECT 
		url,
        json_extract(characteristics , '$.base_experience') as base_characteristic_base_experience,
		json_extract(characteristics , '$.height') as base_characteristic_height,
		json_extract(characteristics , '$.id') as base_characteristic_id,
		json_extract(characteristics , '$.is_default') as base_characteristic_is_default,
		replace(json_extract(characteristics , '$.name'), '"','') as base_characteristic_name,
		json_extract(characteristics , '$.order') as base_characteristic_order,
		json_extract(characteristics , '$.weight') as base_characteristic_weight
	FROM pokebase.main.pokemon_characteristics pc;
"""

con.execute(sql)
con.close()
 