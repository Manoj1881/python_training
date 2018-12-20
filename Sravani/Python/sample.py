import web
urls=(
      '/(.*)','index'
)
render=web.template.render("templates/")
app=web.application(urls,globals())

class index:
       
    def GET(self,name):
        return render.index("webpy is cool")
    def POST(self,name):
        return "post"
if __name__=="__main__":
    app.run()

