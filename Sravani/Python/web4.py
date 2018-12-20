import web
urls=(
        '/', 'Index',
)
app = web.application(urls, globals())
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app,store,initializer={'count': 0})
    web.config._session = session
else:
    session = web.config._session
render = web.template.render('templates', base='base')
class Index:
    def GET(self):
        print(session.count)
        print(session.get('count'))
        #print session['count']
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()