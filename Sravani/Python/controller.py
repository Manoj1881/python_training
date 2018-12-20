import web

urls=(
     
      '/','register',
      '/home','home',
      '/postregistration','postregistration'
      
)
render=web.template.render("views/templates",base="mainlayout")
app=web.application(urls,globals())



class home:
    def GET(self):
        return render.home()


class register:
    def GET(self):
        return render.register()
class postregistration:
    def POST(self):
        data=web.input()
       
        
        return data.username

if __name__=="__main__":
    app.run()