import web
urls=(
      '/(.*)','index'
)
app=web.application(urls,globals())
class index:
    def my_processor(handler): 
        print('before handling')
        print('after handling')
        handler='hi'
        result = handler
        print(result)
        return result
    app.add_processor(my_processor)
    def my_loadhook():
       web.header('Content-type', "text/html; charset=utf-8")
       input=web.input()
       print(input)
    def my_unloadhook():
        print ("my unload hook")
    app.add_processor(web.loadhook(my_loadhook))
    app.add_processor(web.unloadhook(my_unloadhook))
if __name__=="__main__":
       app.run()
