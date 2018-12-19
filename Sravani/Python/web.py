import web

urls = (
    '/(.*)', 'index'
)


class index:
    def GET(self,name):
        print("Hello",name, '. How are you today')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    