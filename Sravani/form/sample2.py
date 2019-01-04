import web
import pymysql.cursors

#f=codecs.open("task1.html", 'r')
#print(f.read())
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='test1',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
urls=(
      '/signup','signup',
      '/','main1'
)
render=web.template.render('templates/')
class main1:
    def GET(self):
        return render.main1()
class signup:
    def POST(self):
        i = web.input()
        print(i)
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO employe (firstname,email,gender,password,conformpassword,mobileno,bday,address) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (i.firstname,i.email,i.gender,i.password,i.conformpassword,i.mobileno,i.bday,i.address))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()

                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "SELECT id,firstname,gender,password,conformpassword,mobileno,bday,address FROM employe WHERE email=%s"
                    cursor.execute(sql, (i.email))
                    result = cursor.fetchone()
                    print(result)
        finally:
            connection.close()
            return "sucess"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()