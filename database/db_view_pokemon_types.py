import db_connection as dbcon

con = dbcon.PokeBaseConnection()

view_name = "types"

sql = f"""
    CREATE OR REPLACE VIEW prep_pokemon_{view_name} AS 
    WITH cte AS (
    	SELECT 
    		from_json(
    			json(
    				json_extract(characteristics , '$.types')
    			),'["JSON"]') AS json_col,
    	url
    	from pokebase.main.pokemon_characteristics pc
    )

    SELECT 
    	url, 
    	replace(types.type.name, '"', '') AS type_name,
        types.slot as type_slot,
    	replace(types.type.url, '"', '') as type_url
    FROM (
    SELECT 
    	unnest(json_col) AS types,
    	url
    FROM cte
    ) AS A;
"""

con.execute(sql)
con.close()