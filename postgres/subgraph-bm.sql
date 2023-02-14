
--------------------------------------------------------------------------------------
-- Q1: 817.1M 18,47 / 2,27
--------------------------------------------------------------------------------------
SELECT count(*)
FROM Country
JOIN City ON City.PartOfCountryId = Country.id
JOIN Person ON Person.LocationCityId = City.id
JOIN Forum_hasMember_Person ON Forum_hasMember_Person.personid = Person.id
JOIN Forum ON Forum.id = Forum_hasMember_Person.forumid
JOIN Message Post ON Post.ContainerForumId = Forum.id
JOIN Message Comment ON Comment.ParentMessageId = Post.id
JOIN Message_hasTag_Tag ON Message_hasTag_Tag.id = Comment.id
JOIN Tag ON Tag.id = Message_hasTag_Tag.tagid
JOIN TagClass ON Tag.TypeTagClassId  = TagClass.id;

--------------------------------------------------------------------------------------
-- Q2 3.3M 1,32 / 0,09
--------------------------------------------------------------------------------------
SELECT count(*)
FROM Person_knows_Person pkp
     JOIN Message Comment ON pkp.Person1Id = Comment.creatorpersonid
     JOIN Message Post ON pkp.Person2Id = Post.creatorpersonid
AND Post.ParentMessageId is null and Comment.parentmessageid = Post.id;
--------------------------------------------------------------------------------------
-- Q3 3.2M 15,60 / 0,38
--------------------------------------------------------------------------------------
SELECT count(*)
FROM Country
JOIN City AS CityA ON CityA.PartOfCountryId  = Country.id
JOIN City AS CityB ON CityB.PartOfCountryId  = Country.id
JOIN City AS CityC ON CityC.PartOfCountryId  = Country.id
JOIN Person AS PersonA ON PersonA.LocationCityId  = CityA.id
JOIN Person AS PersonB ON PersonB.LocationCityId  = CityB.id
JOIN Person AS PersonC ON PersonC.LocationCityId  = CityC.id
JOIN Person_knows_Person AS pkp1 ON pkp1.Person1Id = personA.id AND pkp1.Person2Id = personB.id
JOIN Person_knows_Person AS pkp2 ON pkp2.Person1Id = personB.id AND pkp2.Person2Id = personC.id
JOIN Person_knows_person AS pkp3 ON pkp3.Person1Id = personC.id AND pkp3.Person2Id = personA.id;

--------------------------------------------------------------------------------------
-- Q4 50.0M 2,52 / 0,91
--------------------------------------------------------------------------------------
SELECT count(*)
FROM Message_hasTag_Tag
JOIN Message ON Message.Id = Message_hasTag_Tag.Id
JOIN Message Comment ON Comment.ParentMessageId = Message.Id
JOIN Person ON Person.Id = Message.creatorpersonid 
JOIN Person_likes_Message ON Person_likes_Message.Id = Message.Id;

--------------------------------------------------------------------------------------
-- Q5 41.6M 3,37 / 0,48
--------------------------------------------------------------------------------------
SELECT count(*)
FROM Message_hasTag_Tag as mht1
JOIN Message Comment ON Comment.Id = mht1.Id
JOIN Message ON Message.Id = Comment.ParentMessageId
JOIN Message_hasTag_Tag mht2 on mht2.id = Message.Id
WHERE mht1.tagid != mht2.tagid;

--------------------------------------------------------------------------------------
-- Q6 6.3B 6,50 / 4,76
--------------------------------------------------------------------------------------
SELECT count(*)
FROM Person_knows_Person pkp1
JOIN Person_knows_Person pkp2 ON pkp1.Person2Id = pkp2.Person1Id AND pkp1.Person1Id != pkp2.Person2Id
JOIN Person_hasInterest_Tag ON pkp2.Person2Id = Person_hasInterest_Tag.personid;

--------------------------------------------------------------------------------------
-- Q7 85.2M
--------------------------------------------------------------------------------------
SELECT count(*)
FROM Message_hasTag_Tag
JOIN Message_hasCreator_Person
ON Message_hasTag_Tag.MessageId =
Message_hasCreator_Person.MessageId
LEFT JOIN Comment_replyOf_Message
ON Comment_replyOf_Message.ParentMessageId =
Message_hasTag_Tag.MessageId
LEFT JOIN Person_likes_Message
ON Person_likes_Message.MessageId = Message_hasTag_Tag.
MessageId;

--------------------------------------------------------------------------------------
-- Q8 20.8M 
--------------------------------------------------------------------------------------
SELECT count(*)
FROM Message_hasTag_Tag as mht1
JOIN Message Comment ON Comment.Id = mht1.Id
JOIN Message ON Message.Id = Comment.ParentMessageId
JOIN Message_hasTag_Tag mht2 on mht2.id = Message.Id
LEFT JOIN mht1 
WHERE mht1.tagid != mht2.tagid;

SELECT count(*)
FROM Message_hasTag_Tag
JOIN Comment_replyOf_Message ON Message_hasTag_Tag.MessageId = Comment_replyOf_Message.ParentMessageId
JOIN Comment_hasTag_Tag AS cht1 ON Comment_replyOf_Message.CommentId = cht1.id
LEFT JOIN Comment_hasTag_Tag AS cht2 ON Message_hasTag_Tag.hasTag_Tag = cht2.hasTag_Tag AND Comment_replyOf_Message.CommentId = cht2.id
WHERE Message_hasTag_Tag.hasTag_Tag != cht1.hasTag_Tag
AND cht2.hasTag_Tag IS NULL;

--------------------------------------------------------------------------------------
-- Q9 6.0B 11,86 / 12,83
--------------------------------------------------------------------------------------
SELECT count(*)
FROM Person_knows_Person pkp1
JOIN Person_knows_Person pkp2 ON pkp1.Person2Id = pkp2.Person1Id AND pkp1.Person1Id != pkp2.Person2Id
JOIN Person_hasInterest_Tag ON pkp2.Person2Id = Person_hasInterest_Tag.personid
LEFT JOIN Person_knows_Person pkp3 ON pkp3.Person1Id = pkp1.Person1Id AND pkp3.Person2Id = pkp2.Person2Id
WHERE pkp3.Person1Id IS NULL;