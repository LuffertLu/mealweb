#a simple script to test mysql db connected or not
import MySQLdb
db=MySQLdb.connect("localhost", "root", "", "recommend")
cursor=db.cursor()
sql="create table user_anime(user int, anime int)"
cursor.execute(sql)
db.close()

