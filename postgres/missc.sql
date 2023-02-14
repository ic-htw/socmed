select
  relname as table_name,
  n_live_tup as row_count
from pg_stat_user_tables
where schemaname = 'usocmed'
order by schemaname, relname;

table_name               |row_count|
-------------------------+---------+
city                     |     1343|
company                  |     1575|
country                  |      111|
forum                    |   100827|
forum_hasmember_person   |  2909768|
forum_hastag_tag         |   328584|
message                  |  2861276|
message_hastag_tag       |  2928064|
organisation             |     7955|
pathq19                  |   311328|
pathq20                  |     6866|
person                   |    10295|
person_hasinterest_tag   |   238052|
person_knows_person      |   173014|
person_likes_message     |  1870268|
person_studyat_university|     8309|
person_workat_company    |    22044|
place                    |     1460|
popularityscoreq06       |     8989|
tag                      |    16080|
tagclass                 |       71|
top100popularforumsq04   |    92436|
university               |     6380|