import db_connection as dbcon

con = dbcon.PokeBaseConnection()

view_name = "moves"

sql = f"""
    CREATE OR REPLACE VIEW prep_pokemon_{view_name} AS 
    WITH cte AS (
    	SELECT 
    		from_json(
    			json(
    				json_extract(characteristics , '$.moves')
    			),'["JSON"]') AS json_col,
    	url
    	from pokebase.main.pokemon_characteristics pc
    )

    SELECT 
    	url, 
    	replace(moves.move.name, '"', '') AS move_name,
    	replace(moves.move.url, '"', '') as move_url,
    	moves.version_group_details as move_version_group_details
    FROM (
    SELECT 
    	unnest(json_col) AS moves,
    	url
    FROM cte
    ) AS A;
"""

con.execute(sql)
con.close()