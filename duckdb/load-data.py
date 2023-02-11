import duckdb
con = duckdb.connect(database='socmed.duckdb', read_only=False)

csvdir = '../../ldbc-snb/csv/'

# -------------------------------------------------
# TagClass
# -------------------------------------------------
sql = f"""
insert into TagClass
  select * from read_csv('{csvdir}TagClass.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""
# print(sql)
con.execute(sql)


# -------------------------------------------------
# Tag
# -------------------------------------------------
sql = f"""
insert into Tag
  select * from read_csv('{csvdir}Tag.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""
con.execute(sql)

# -------------------------------------------------
# place
# -------------------------------------------------
sql = f"""
insert into place
  select * from read_csv('{csvdir}Place.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)

# -------------------------------------------------
# Organisation
# -------------------------------------------------
sql = f"""
insert into Organisation
  select * from read_csv('{csvdir}Organisation.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)



# -------------------------------------------------
# Person
# -------------------------------------------------
sql = f"""
insert into Person
  select * from read_csv('{csvdir}Person1.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Person
  select * from read_csv('{csvdir}Person2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)

# -------------------------------------------------
# Post
# -------------------------------------------------
sql = f"""
insert into Post
  select * from read_csv('{csvdir}Post2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Post
  select * from read_csv('{csvdir}Post3.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)


# -------------------------------------------------
# Comment
# -------------------------------------------------
sql = f"""
insert into Comment
  select * from read_csv('{csvdir}Comment2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Comment
  select * from read_csv('{csvdir}Comment3.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)


# -------------------------------------------------
# Forum
# -------------------------------------------------
sql = f"""
insert into Forum
  select * from read_csv('{csvdir}Forum1.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Forum
  select * from read_csv('{csvdir}Forum2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)


# -------------------------------------------------
# Comment_hasTag_Tag
# -------------------------------------------------
sql = f"""
insert into Comment_hasTag_Tag
  select * from read_csv('{csvdir}Comment_hasTag_Tag2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Comment_hasTag_Tag
  select * from read_csv('{csvdir}Comment_hasTag_Tag3.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)


# -------------------------------------------------
# Post_hasTag_Tag
# -------------------------------------------------
sql = f"""
insert into Post_hasTag_Tag
  select * from read_csv('{csvdir}Post_hasTag_Tag1.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Post_hasTag_Tag
  select * from read_csv('{csvdir}Post_hasTag_Tag2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)


# -------------------------------------------------
# Forum_hasMember_Person
# -------------------------------------------------
sql = f"""
insert into Forum_hasMember_Person
  select * from read_csv('{csvdir}Forum_hasMember_Person2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Forum_hasMember_Person
  select * from read_csv('{csvdir}Forum_hasMember_Person3.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)


# -------------------------------------------------
# Forum_hasTag_Tag
# -------------------------------------------------
sql = f"""
insert into Forum_hasTag_Tag
  select * from read_csv('{csvdir}Forum_hasTag_Tag1.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Forum_hasTag_Tag
  select * from read_csv('{csvdir}Forum_hasTag_Tag2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)



# -------------------------------------------------
# Person_hasInterest_Tag
# -------------------------------------------------
sql = f"""
insert into Person_hasInterest_Tag
  select * from read_csv('{csvdir}Person_hasInterest_Tag1.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Person_hasInterest_Tag
  select * from read_csv('{csvdir}Person_hasInterest_Tag2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)


# -------------------------------------------------
# Person_likes_Comment
# -------------------------------------------------
sql = f"""
insert into Person_likes_Comment
  select * from read_csv('{csvdir}Person_likes_Comment2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Person_likes_Comment
  select * from read_csv('{csvdir}Person_likes_Comment3.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)


# -------------------------------------------------
# Person_likes_Post
# -------------------------------------------------
sql = f"""
insert into Person_likes_Post
  select * from read_csv('{csvdir}Person_likes_Post1.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Person_likes_Post
  select * from read_csv('{csvdir}Person_likes_Post2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)


# -------------------------------------------------
# Person_studyAt_University
# -------------------------------------------------
sql = f"""
insert into Person_studyAt_University
  select * from read_csv('{csvdir}Person_studyAt_University1.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Person_studyAt_University
  select * from read_csv('{csvdir}Person_studyAt_University2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)


# -------------------------------------------------
# Person_workAt_Company
# -------------------------------------------------
sql = f"""
insert into Person_workAt_Company
  select * from read_csv('{csvdir}Person_workAt_Company1.csv', delim='|', header=True, AUTO_DETECT=TRUE);
insert into Person_workAt_Company
  select * from read_csv('{csvdir}Person_workAt_Company2.csv', delim='|', header=True, AUTO_DETECT=TRUE);
"""



con.execute(sql)


# -------------------------------------------------
# Person_knows_Person
# -------------------------------------------------
sql = f"""
insert into Person_knows_Person
  select * from read_csv('{csvdir}Person_knows_Person1.csv', delim='|', header=True, AUTO_DETECT=TRUE, SAMPLE_SIZE=-1);
insert into Person_knows_Person
  select * from read_csv('{csvdir}Person_knows_Person2.csv', delim='|', header=True, AUTO_DETECT=TRUE, SAMPLE_SIZE=-1);
"""
con.execute(sql)



# -------------------------------------------------
# Country
# -------------------------------------------------
sql = f"""
INSERT INTO Country
    SELECT id, name, url, PartOfPlaceId AS PartOfContinentId
    FROM Place
    WHERE type = 'Country';
"""
con.execute(sql)


# -------------------------------------------------
# City
# -------------------------------------------------
sql = f"""
INSERT INTO City
    SELECT id, name, url, PartOfPlaceId AS PartOfCountryId
    FROM Place
    WHERE type = 'City'
"""
con.execute(sql)


# -------------------------------------------------
# Company
# -------------------------------------------------
sql = f"""
INSERT INTO Company
    SELECT id, name, url, LocationPlaceId AS LocatedInCountryId
    FROM Organisation
    WHERE type = 'Company';
"""
con.execute(sql)


# -------------------------------------------------
# University
# -------------------------------------------------
sql = f"""
INSERT INTO University
    SELECT id, name, url, LocationPlaceId AS LocatedInCityId
    FROM Organisation
    WHERE type = 'University';
"""
con.execute(sql)


# -------------------------------------------------
# Message 1
# -------------------------------------------------
sql = f"""
INSERT INTO Message
    SELECT
        creationDate,
        id AS id,
        language,
        content,
        imageFile,
        locationIP,
        browserUsed,
        length,
        CreatorPersonId,
        ContainerForumId,
        LocationCountryId,
        NULL::bigint AS ParentMessageId
    FROM Post;
"""
con.execute(sql)

# -------------------------------------------------
# Message 2
# -------------------------------------------------
sql = f"""
INSERT INTO Message
    SELECT
        Comment.creationDate AS creationDate,
        Comment.id AS id,
        NULL,
        Comment.content AS content,
        NULL AS imageFile,
        Comment.locationIP AS locationIP,
        Comment.browserUsed AS browserUsed,
        Comment.length AS length,
        Comment.CreatorPersonId AS CreatorPersonId,
        NULL AS ContainerForumId,
        Comment.LocationCountryId AS LocationCityId,
        coalesce(Comment.ParentPostId, Comment.ParentCommentId) AS ParentMessageId
    FROM Comment;
"""
con.execute(sql)


# -------------------------------------------------
# Person_likes_Message 1
# -------------------------------------------------
sql = f"""
INSERT INTO Person_likes_Message
    SELECT creationDate, PersonId, PostId AS id FROM Person_likes_Post;
"""
con.execute(sql)


# -------------------------------------------------
# Person_likes_Message 2
# -------------------------------------------------
sql = f"""
INSERT INTO Person_likes_Message
    SELECT creationDate, PersonId, CommentId AS id FROM Person_likes_Comment;
"""
con.execute(sql)


# -------------------------------------------------
# Message_hasTag_Tag 1
# -------------------------------------------------
sql = f"""
INSERT INTO Message_hasTag_Tag
    SELECT creationDate, PostId AS id, TagId FROM Post_hasTag_Tag;
"""
con.execute(sql)


# -------------------------------------------------
# Message_hasTag_Tag 2
# -------------------------------------------------
sql = f"""
INSERT INTO Message_hasTag_Tag
    SELECT creationDate, CommentId AS id, TagId FROM Comment_hasTag_Tag;
"""
con.execute(sql)

# -------------------------------------------------
# Drop tables
# -------------------------------------------------
sql = f"""
DROP TABLE IF EXISTS Post;
DROP TABLE IF EXISTS Comment;

DROP TABLE IF EXISTS Person_likes_Post;
DROP TABLE IF EXISTS Person_likes_Comment;

DROP TABLE IF EXISTS Post_hasTag_Tag;
DROP TABLE IF EXISTS Comment_hasTag_Tag;
"""
con.execute(sql)



# -------------------------------------------------
print("ok")
# -------------------------------------------------


