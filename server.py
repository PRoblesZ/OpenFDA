#PROGRAMA PRINCIPAL
import socketserver
import web

##
#WEB SERVER
##

PORT=8000


#Handler=http.server.SimpleHTTPRequestHandler
Handler=web.testHTTPRequestHandler

#Para poder utilizar el puerto 8000 sin limite

socketserver.TCPServer.allow_reuse_address = True

httpd=socketserver.TCPServer(('',PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
