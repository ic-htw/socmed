import duckdb
con = duckdb.connect(database='socmed.duckdb', read_only=True)
sql = """
select count(*) from Person_knows_Person;
"""
con.execute(sql)
print(con.fetchall())

sql = """
select * from Person_knows_Person limit 1;
"""
con.execute(sql)
print(con.fetchall())
