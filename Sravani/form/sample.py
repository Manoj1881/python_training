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


urls = (
    '/signup', 'signup',
    '/','index'
)
render=web.template.render('templates/')
class index:
    def GET(self):
        return render.index()
    
class signup:
    def POST(self):
        i = web.input()
        print(i)
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
                cursor.execute(sql, (i.email,i.password))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()

                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "SELECT id, password FROM users WHERE email=%s"
                    cursor.execute(sql, (i.email))
                    result = cursor.fetchone()
                    print(result)
        finally:
            connection.close()
            return "sucess"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

