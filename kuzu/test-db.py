import kuzu
csvdir = "../../ldbc-snb/csv-kuzu"

db = kuzu.Database("socmed.kuzu")
con = kuzu.Connection(db)

# -------------------------------------------------
# person
# -------------------------------------------------
q = """
MATCH (x:Tag) RETURN x limit 2;
"""
rs = con.execute(q)

while rs.has_next():
    print(rs.get_next())

# -------------------------------------------------
print('ok')
# -------------------------------------------------
