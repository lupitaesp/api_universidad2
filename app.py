import web

from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

urls = (
    '/alumnos?', 'application.controllers.alumnos.Alumnos' #el simbolo ? inidca que recibira variables en la URL
)
app = web.application(urls, globals())

#render = web.template.render('templates/')  #dice que la carpeta de las paginas web sera templates

if __name__ == "__main__":
    web.config.debug = True
    app.run()