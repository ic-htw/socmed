import duckdb
con = duckdb.connect(database='socmed.duckdb', read_only=True)

csvdir = '../../ldbc-snb/csv-kuzu'

# -------------------------------------------------
# Tag
# -------------------------------------------------
sql = f"""
copy tag to '{csvdir}/Tag.csv' (HEADER, DELIMITER '|');
"""
# con.execute(sql)

# -------------------------------------------------
# Person
# -------------------------------------------------
sql = f"""
copy person to '{csvdir}/Person.csv' (HEADER, DELIMITER '|');
"""
# con.execute(sql)

# -------------------------------------------------
# KNOWS
# -------------------------------------------------
sql = f"""
copy (select Person1Id, Person2Id, creationDate from Person_knows_Person) 
to '{csvdir}/KNOWS.csv' (HEADER, DELIMITER '|');
"""
# con.execute(sql)

# -------------------------------------------------
# HAS_INTEREST
# -------------------------------------------------
sql = f"""
copy (select PersonId, TagId, creationDate from Person_hasInterest_Tag) 
to '{csvdir}/HAS_INTEREST.csv' (HEADER, DELIMITER '|');
"""
# con.execute(sql)

# -------------------------------------------------
print('ok')
# -------------------------------------------------
