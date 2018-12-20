import web
urls=(
      '/(.*)','index'
)
render=web.template.render('templates/',base='layout')
app=web.application(urls,globals())
class index:
    def GET(self):
       return render.layout()
if __name__=="__main__":
    app.run()
