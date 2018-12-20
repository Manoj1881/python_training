import web
urls=(
      '/(.*)','SomePage'
)
app=web.application(urls,globals())
class SomePage:
    def POST(self):
        raise web.seeother('/someotherpage')
if __name__=="__main__":
    app.run()


