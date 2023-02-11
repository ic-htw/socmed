import duckdb
con = duckdb.connect(database='socmed.duckdb', read_only=False)

sql = """
xxx
"""
con.execute(sql)

print("ok")
