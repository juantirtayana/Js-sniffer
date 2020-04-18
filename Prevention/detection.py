from checksumdir import dirhash
from datetime import datetime
import mysql.connector

dir = '/var/www/'
newhash = dirhash(dir,'md5')

legithash = open("legitmd5.txt","r")

if newhash != legithash.read().rstrip():
	with open('/var/www/html/.htaccess') as htaccess:
		if 'Redirect /payment/ http://192.168.100.10/maintenance.html' not in htaccess.read():
     			file = open("/var/www/html/.htaccess","a")
     			file.write("\nRedirect /payment/ http://192.168.100.10/maintenance.html")
     			file.close()
			
			mydb = mysql.connector.connect(
				host = 'localhost',
				user = "root",
				password = "password",
				database = "hash_changes_date"
			)

			mycursor = mydb.cursor()

			sqlquery = "INSERT INTO hash (hashFile) VALUES (%s)"

			curr_date = [datetime.now().strftime('%d-%m-%Y %H:%M:%S')]

			mycursor.execute(sqlquery,curr_date)

			mydb.commit()

		htaccess.close()

legithash.close()
