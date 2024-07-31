import db_connection as dbcon

con = dbcon.PokeBaseConnection()

view_name = "stats"

sql = f"""
    CREATE OR REPLACE VIEW prep_pokemon_{view_name} AS 
    WITH cte AS (
    	SELECT 
    		from_json(
    			json(
    				json_extract(characteristics , '$.stats')
    			),'["JSON"]') AS json_col,
    	url
    	from pokebase.main.pokemon_characteristics pc
    )

    SELECT 
    	url, 
    	replace(stats.stat.name, '"', '') AS stat_name,
    	stats.base_stat as stat_base_stat,
    	stats.effort as stat_effort,
    	replace(stats.stat.url, '"', '') as stat_url
    FROM (
    SELECT 
    	unnest(json_col) AS stats,
    	url
    FROM cte
    ) AS A;
"""

con.execute(sql)
con.close()