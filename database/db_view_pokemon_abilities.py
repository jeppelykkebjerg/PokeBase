import db_connection as dbcon

con = dbcon.PokeBaseConnection()


sql = """
    CREATE OR REPLACE VIEW prep_pokemon_abilities AS 
    WITH cte AS (
    	SELECT 
    		from_json(
    			json(
    				json_extract(characteristics , '$.abilities')
    			),'["JSON"]') AS json_col,
    	url
    	from pokebase.main.pokemon_characteristics pc
    )

    SELECT 
    	url, 
    	replace(abilities.ability.name, '"', '') AS ability_name,
    	abilities.is_hidden AS ability_is_hidden,
    	abilities.slot AS ability_slot
    FROM (
    SELECT 
    	unnest(json_col) AS abilities,
    	url
    FROM cte
    ) AS A;
"""

con.execute(sql)
con.close()