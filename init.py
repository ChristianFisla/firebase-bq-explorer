from google.cloud import bigquery

client = bigquery.Client()

query = """
    SELECT name, SUM(number) as total
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    GROUP BY name
    ORDER BY total DESC
    LIMIT 10
"""

query_job = client.query(query)

for row in query_job:
    print(f"{row.name}: {row.total}")
