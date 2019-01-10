import web
import pymysql.cursors
import re
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
        i=web.input() 
        print("printing...!!!")
        print(i)
        match = re.search(r'[\w.-]+@[\w.-]+.\w+',str(i))
        if match:
           print( "valid email :::", match.group())
        else:
          print ("not valid:::")
          return "please enter correct email id"
        match_mob= re.search(r'((?:\(?\+?91\)?)?0?\d{10})', str(i))
        if match_mob:
            print(match_mob.group(0))
        else:
            print("not valid")
            return "please enter correct mobile no"
        print(i)
        if i.password==i.conformpassword:
            print("valid")
        else:
            print("not valid")
            return "enter password"
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO employe (firstname,email,gender,password,conformpassword,mobileno,bday,address) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (i.firstname,i.email,i.gender,i.password,i.conformpassword,i.mobileno,i.bday,i.address))
                connection.commit()
                with connection.cursor() as cursor:
                    sql = "SELECT id,firstname,gender,password,conformpassword,mobileno,bday,address FROM employe WHERE email=%s"
                    cursor.execute(sql, (i.email))
                    result = cursor.fetchone()
                    print(result)
        finally:
            connection.close()
            return "success"
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()