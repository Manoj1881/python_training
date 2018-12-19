import web

urls = (
    '/(.*)/(.*)', 'index'
)
 
class index:
    def GET(self,name,age):
        return render.main(name,age)

if __name__ == "__main__":
    render=web.template.render("resources/")
    app = web.application(urls, globals())
    app.run()
    


