-- bi / read / 4
DROP TABLE IF EXISTS Top100PopularForumsQ04;

CREATE TABLE Top100PopularForumsQ04(
    id bigint not null,
    creationDate timestamp with time zone NOT NULL,
    maxNumberOfMembers bigint not null
);

INSERT INTO Top100PopularForumsQ04(id, creationDate, maxNumberOfMembers)
SELECT T.id, Forum.creationdate, T.maxNumberOfMembers
FROM (SELECT ForumId AS id, max(numberOfMembers) AS maxNumberOfMembers
FROM (
SELECT Forum_hasMember_Person.ForumId AS ForumId, count(Person.id) AS numberOfMembers, City.PartOfCountryId AS CountryId
    FROM Forum_hasMember_Person
    JOIN Person
    ON Person.id = Forum_hasMember_Person.PersonId
    JOIN City
    ON City.id = Person.LocationCityId
    GROUP BY City.PartOfCountryId, Forum_hasMember_Person.ForumId
) ForumMembershipPerCountry
GROUP BY ForumId) T, Forum
WHERE T.id = Forum.id;

ALTER TABLE Top100PopularForumsQ04 ADD PRIMARY KEY (id);


-- bi / read / 6
DROP TABLE IF EXISTS PopularityScoreQ06;

CREATE TABLE PopularityScoreQ06 (
    person2id bigint not null,
    popularityScore bigint not null
);

INSERT INTO PopularityScoreQ06(person2id, popularityScore)
SELECT
    message2.CreatorPersonId AS person2id,
    count(*) AS popularityScore
FROM Message message2
JOIN Person_likes_Message like2
    ON like2.Id = message2.Id
GROUP BY message2.CreatorPersonId;

ALTER TABLE PopularityScoreQ06 ADD PRIMARY KEY (person2id);

-- bi /read / 19
DROP TABLE IF EXISTS PathQ19;
CREATE TABLE PathQ19 (
    src bigint not null,
    dst bigint not null,
    w double precision not null
);
INSERT INTO PathQ19(src, dst, w)
WITH
weights(src, dst, w) AS (
    SELECT
        person1id AS src,
        person2id AS dst,
        greatest(round(40 - sqrt(count(*)))::bigint, 1) AS w
    FROM (SELECT person1id, person2id FROM Person_knows_person WHERE person1id < person2id) pp, Message m1, Message m2
    WHERE pp.person1id = least(m1.creatorpersonid, m2.creatorpersonid) and pp.person2id = greatest(m1.creatorpersonid, m2.creatorpersonid) and m1.parentmessageid = m2.id and m1.creatorpersonid <> m2.creatorpersonid
    GROUP BY src, dst
)
SELECT src, dst, w FROM weights
UNION ALL
SELECT dst, src, w FROM weights;
ALTER TABLE PathQ19 ADD PRIMARY KEY (src, dst);

-- bi / read / 20

DROP TABLE IF EXISTS PathQ20;
CREATE TABLE PathQ20 (
    src bigint not null,
    dst bigint not null,
    w int not null
) with (storage = paged);
INSERT INTO PathQ20(src, dst, w)
select p1.personid, p2.personid, min(abs(p1.classYear - p2.classYear)) + 1
from Person_knows_person pp, Person_studyAt_University p1, Person_studyAt_University p2
where pp.person1id = p1.personid and pp.person2id = p2.personid and p1.universityid = p2.universityid
group by p1.personid, p2.personid;
ALTER TABLE PathQ20 ADD PRIMARY KEY (src, dst);
