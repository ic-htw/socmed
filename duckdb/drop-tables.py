import duckdb
con = duckdb.connect(database='socmed.duckdb', read_only=False)

sql = """
DROP TABLE IF EXISTS Comment_hasTag_Tag;
DROP TABLE IF EXISTS Post_hasTag_Tag;
DROP TABLE IF EXISTS Forum_hasMember_Person;
DROP TABLE IF EXISTS Forum_hasTag_Tag;
DROP TABLE IF EXISTS Person_hasInterest_Tag;
DROP TABLE IF EXISTS Person_likes_Comment;
DROP TABLE IF EXISTS Person_likes_Post;
DROP TABLE IF EXISTS Person_studyAt_University;
DROP TABLE IF EXISTS Person_workAt_Company;
DROP TABLE IF EXISTS Person_knows_Person;
DROP TABLE IF EXISTS Message_hasTag_Tag;
DROP TABLE IF EXISTS Person_likes_Message;
DROP TABLE IF EXISTS Message;
DROP TABLE IF EXISTS Comment;
DROP TABLE IF EXISTS Forum;
DROP TABLE IF EXISTS Post;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS University;
DROP TABLE IF EXISTS Organisation;
DROP TABLE IF EXISTS Place;
DROP TABLE IF EXISTS City;
DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS Continent;
DROP TABLE IF EXISTS Tag;
DROP TABLE IF EXISTS TagClass;
"""
con.execute(sql)

print("ok")