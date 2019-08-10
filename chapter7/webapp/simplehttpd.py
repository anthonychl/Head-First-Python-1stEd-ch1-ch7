from http.server import HTTPServer, CGIHTTPRequestHandler  #import the HTTP and CGI modules

port = 8080 #specify a port

httpd = HTTPServer(('',port),CGIHTTPRequestHandler) #Create a server

print("Starting simple_httpd on port: "+ str(httpd.server_port)) #display a friendly message

httpd.serve_forever() #start the server
