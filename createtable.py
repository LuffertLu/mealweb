#this is the script to create related table.
import MySQLdb
db=MySQLdb.connect("localhost", "root", "", "recommend")
cursor=db.cursor()
sqluser="create table user(id int, name varchar(20), primary key(id))"
cursor.execute(sqluser)
sqlanime="create table anime(id int, name varchar(20), brief varchar(100), primary key(id))"
cursor.execute(sqlanime)
sqlinsuser='insert into user values(1, "Tom")'
cursor.execute(sqlinsuser)

animevalue=[[279, "a", "A"],[3494, "b", "B"],[3377, "c", "C"],[3452, "d", "D"],[782, "e", "E"],[782, "f", "F"],[2730, "g", "G"]]

for x in range(7):
    sqlins anime='insert into anime values({},"{}","{}")'.format(animevalue[x][0],animevalue[x][1],animevalue[x][2])
    cursor.execute(sqlinsanime)

sqlastyle="create table anime_style(anime_id int, style_id int, foreign key(anime_id) references anime(id))"
cursor.execute(sqlastyle)
style_value=[[279,26],[279,30],[279,32],[279,8],[279,7],
            [3494,9],[3494,19],[3494,29],[3494,46],
            [3377,34],[3377,7],[3377,18],
            [3452,30],[3452,32],[3452,7],[3452,22],
            [782,30],[782,32],[782,7],
            [782,1],[782,50],
            [3421,30],[3421,32],[3421,7],[3421,22],
            [2370,11],[2370,30],[2370,22]]
