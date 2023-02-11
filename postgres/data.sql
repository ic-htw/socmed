copy TagClass from '/var/lib/postgresql/csv/socmed/TagClass.csv' delimiter '|' csv header;
copy Tag from '/var/lib/postgresql/csv/socmed/Tag.csv' delimiter '|' csv header;
copy Place from '/var/lib/postgresql/csv/socmed/Place.csv' delimiter '|' csv header;
copy Organisation from '/var/lib/postgresql/csv/socmed/Organisation.csv' delimiter '|' csv header;
copy Person from '/var/lib/postgresql/csv/socmed/Person1.csv' delimiter '|' csv header;
copy Person from '/var/lib/postgresql/csv/socmed/Person2.csv' delimiter '|' csv header;
copy Post from '/var/lib/postgresql/csv/socmed/Post2.csv' delimiter '|' csv header;
copy Post from '/var/lib/postgresql/csv/socmed/Post3.csv' delimiter '|' csv header;
copy Comment from '/var/lib/postgresql/csv/socmed/Comment2.csv' delimiter '|' csv header;
copy Comment from '/var/lib/postgresql/csv/socmed/Comment3.csv' delimiter '|' csv header;
copy Forum from '/var/lib/postgresql/csv/socmed/Forum1.csv' delimiter '|' csv header;
copy Forum from '/var/lib/postgresql/csv/socmed/Forum2.csv' delimiter '|' csv header;
copy Comment_hasTag_Tag from '/var/lib/postgresql/csv/socmed/Comment_hasTag_Tag2.csv' delimiter '|' csv header;
copy Comment_hasTag_Tag from '/var/lib/postgresql/csv/socmed/Comment_hasTag_Tag3.csv' delimiter '|' csv header;
copy Post_hasTag_Tag from '/var/lib/postgresql/csv/socmed/Post_hasTag_Tag1.csv' delimiter '|' csv header;
copy Post_hasTag_Tag from '/var/lib/postgresql/csv/socmed/Post_hasTag_Tag2.csv' delimiter '|' csv header;
copy Forum_hasMember_Person from '/var/lib/postgresql/csv/socmed/Forum_hasMember_Person2.csv' delimiter '|' csv header;
copy Forum_hasMember_Person from '/var/lib/postgresql/csv/socmed/Forum_hasMember_Person3.csv' delimiter '|' csv header;
copy Forum_hasTag_Tag from '/var/lib/postgresql/csv/socmed/Forum_hasTag_Tag1.csv' delimiter '|' csv header;
copy Forum_hasTag_Tag from '/var/lib/postgresql/csv/socmed/Forum_hasTag_Tag2.csv' delimiter '|' csv header;
copy Person_hasInterest_Tag from '/var/lib/postgresql/csv/socmed/Person_hasInterest_Tag1.csv' delimiter '|' csv header;
copy Person_hasInterest_Tag from '/var/lib/postgresql/csv/socmed/Person_hasInterest_Tag2.csv' delimiter '|' csv header;
copy Person_likes_Comment from '/var/lib/postgresql/csv/socmed/Person_likes_Comment2.csv' delimiter '|' csv header;
copy Person_likes_Comment from '/var/lib/postgresql/csv/socmed/Person_likes_Comment3.csv' delimiter '|' csv header;
copy Person_likes_Post from '/var/lib/postgresql/csv/socmed/Person_likes_Post1.csv' delimiter '|' csv header;
copy Person_likes_Post from '/var/lib/postgresql/csv/socmed/Person_likes_Post2.csv' delimiter '|' csv header;
copy Person_studyAt_University from '/var/lib/postgresql/csv/socmed/Person_studyAt_University1.csv' delimiter '|' csv header;
copy Person_studyAt_University from '/var/lib/postgresql/csv/socmed/Person_studyAt_University2.csv' delimiter '|' csv header;
copy Person_workAt_Company from '/var/lib/postgresql/csv/socmed/Person_workAt_Company1.csv' delimiter '|' csv header;
copy Person_workAt_Company from '/var/lib/postgresql/csv/socmed/Person_workAt_Company2.csv' delimiter '|' csv header;
copy Person_knows_Person from '/var/lib/postgresql/csv/socmed/Person_knows_Person1.csv' delimiter '|' csv header;
copy Person_knows_Person from '/var/lib/postgresql/csv/socmed/Person_knows_Person2.csv' delimiter '|' csv header;

INSERT INTO Country
    SELECT id, name, url, PartOfPlaceId AS PartOfContinentId
    FROM Place
    WHERE type = 'Country';

INSERT INTO City
    SELECT id, name, url, PartOfPlaceId AS PartOfCountryId
    FROM Place
    WHERE type = 'City';

INSERT INTO Company
    SELECT id, name, url, LocationPlaceId AS LocatedInCountryId
    FROM Organisation
    WHERE type = 'Company';

INSERT INTO University
    SELECT id, name, url, LocationPlaceId AS LocatedInCityId
    FROM Organisation
    WHERE type = 'University';

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

INSERT INTO Person_likes_Message
    SELECT creationDate, PersonId, PostId AS id FROM Person_likes_Post;

INSERT INTO Person_likes_Message
    SELECT creationDate, PersonId, CommentId AS id FROM Person_likes_Comment;

INSERT INTO Message_hasTag_Tag
    SELECT creationDate, PostId AS id, TagId FROM Post_hasTag_Tag;

INSERT INTO Message_hasTag_Tag
    SELECT creationDate, CommentId AS id, TagId FROM Comment_hasTag_Tag;

DROP TABLE IF EXISTS Post;
DROP TABLE IF EXISTS Comment;

DROP TABLE IF EXISTS Person_likes_Post;
DROP TABLE IF EXISTS Person_likes_Comment;

DROP TABLE IF EXISTS Post_hasTag_Tag;
DROP TABLE IF EXISTS Comment_hasTag_Tag;
