import kuzu
csvdir = "../../ldbc-snb/csv-kuzu"

db = kuzu.Database("socmed.kuzu")
con = kuzu.Connection(db)

# -------------------------------------------------
# Tag
# -------------------------------------------------
sql1 = """
drop table Tag;
"""

sql2 = """
create node table Tag (
    id int64,
    name string,
    url string,
    TypeTagClassId int64,
    primary key (id)
);
"""

sql3 = f"""
copy Tag from '{csvdir}/Tag.csv' (HEADER=True, DELIM='|');
"""
# con.execute(sql1)
# con.execute(sql2)
# con.execute(sql3)

# -------------------------------------------------
# person
# -------------------------------------------------
sql1 = """
drop table Person;
"""

sql2 = """
create node table Person (
    creationDate timestamp,
    id int64,
    firstName string,
    lastName string,
    gender string,
    birthday date,
    locationIP string,
    browserUsed string,
    LocationCityId int64,
    speaks string,
    email string,
    primary key (id)
);
"""

sql3 = f"""
copy Person from '{csvdir}/Person.csv' (HEADER=True, DELIM='|');
"""
# con.execute(sql1)
# con.execute(sql2)
# con.execute(sql3)


# -------------------------------------------------
# KNOWS
# -------------------------------------------------
sql1 = """
drop table KNOWS;
"""

sql2 = """
create rel table KNOWS (
    from Person to Person, creationdate timestamp
);
"""

sql3 = f"""
copy KNOWS from '{csvdir}/KNOWS.csv' (HEADER=True, DELIM='|');
"""
# con.execute(sql1)
# con.execute(sql2)
# con.execute(sql3)

# -------------------------------------------------
# HAS_INTEREST
# -------------------------------------------------
sql1 = """
drop table HAS_INTEREST;
"""

sql2 = """
create rel table HAS_INTEREST (
    from Person to Tag, creationdate timestamp
);
"""

sql3 = f"""
copy HAS_INTEREST from '{csvdir}/HAS_INTEREST.csv' (HEADER=True, DELIM='|');
"""
con.execute(sql1)
con.execute(sql2)
con.execute(sql3)

# -------------------------------------------------
print('ok')
# -------------------------------------------------
