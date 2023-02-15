import kuzu
csvdir = "../../ldbc-snb/csv-kuzu"

db = kuzu.Database("socmed.kuzu")
con = kuzu.Connection(db)


# -------------------------------------------------
# xxx
# -------------------------------------------------
sql1 = """
drop table xxx;
"""

sql2 = """
create node table xxx (
    primary key (id)
);
"""

sql3 = f"""
copy xxx from '{csvdir}/xxx.csv' (HEADER=True, DELIM='|');
"""
# con.execute(sql1)
# con.execute(sql2)
# con.execute(sql3)