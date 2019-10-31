#!/usr/bin/env python3
# encoding: utf-8
#this is the script to create related table.
import MySQLdb
db=MySQLdb.connect("localhost", "root", "", "recommend")
cursor=db.cursor()
sqluser="create table user(id int, name varchar(20), primary key(id))"
try:
    cursor.execute(sqluser)
    db.commit()
except:
    db.rollback()

sqlinsuser="insert into user values(1, 'Tom')"
try:
    cursor.execute(sqlinsuser)
    db.commit()
except:
    db.rollback()

sqlanime="create table anime(id int, name varchar(20), brief varchar(100), primary key(id))"
try:
    cursor.execute(sqlanime)
    db.commit()
except:
    db.rollback()

animevalue=[[279, "a", "A"],[3494, "b", "B"],[3377, "c", "C"],[3452, "d", "D"],[782, "e", "E"],[782, "f", "F"],[2730, "g", "G"]]
for x in range(7):
    try:
        sqlinsanime='insert into anime values({},"{}","{}")'.format(animevalue[x][0],animevalue[x][1],animevalue[x][2])
        cursor.execute(sqlinsanime)
        db.commit()
    except:
        db.rollback()


sqlastyle="create table anime_style(anime_id int, style_id int, foreign key(anime_id) references anime(id))"
try:
    cursor.execute(sqlastyle)
    db.commit()
except:
    db.rollback()

style_value=[[279,26],[279,30],[279,32],[279,8],[279,7],
            [3494,9],[3494,19],[3494,29],[3494,46],
            [3377,34],[3377,7],[3377,18],
            [3452,30],[3452,32],[3452,7],[3452,22],
            [782,30],[782,32],[782,7],
            [782,1],[782,50],
            [3421,30],[3421,32],[3421,7],[3421,22],
            [2370,11],[2370,30],[2370,22]]

for i in range(len(style_value)):
    try:
        sqlinsastyle="insert into anime_style values({},{})".format(style_value[i][0],style_value[i][1])
        cursor.execute(sqlinsastyle)
        db.commit()
    except:
        db.rollback()

sqluseranime="create table user_anime(user_id int, anime_id int, foreign key(user_id) references user(id), foreign key(anime_id) references anime(id))"
try:
    cursor.execute(sqluseranime)
    db.commit()
except:
    db.rollback()
sqlinsua1="insert into user_anime values(1, 782)"
try:
    cursor.execute(sqlinsua1)
    db.commit()
except:
    db.rollback()
sqlinsua2="insert into user_anime values(1, 3421)"
try:
    cursor.execute(sqlinsua2)
    db.commit()
except:
    db.rollback()
sqlinsua3="insert into user_anime values(1, 2730)"
try:
    cursor.execute(sqlinsua3)
    db.commit()
except:
    db.rollback()

"""
animevalue=[[279, "a", "A"],[3494, "b", "B"],[3377, "c", "C"],[3452, "d", "D"],[782, "e", "E"],[782, "f", "F"],[2730, "g", "G"]]

for x in range(1):
    sqlinsanime='insert into anime values({},"{}","{}")'.format(animevalue[x][0],animevalue[x][1],animevalue[x][2])
    cursor.execute(sqlinsanime)
    sqlinsanime=""



"""
db.close()
