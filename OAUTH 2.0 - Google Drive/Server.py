from bottle import run,request,route,response,static_file

@route('/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static/')

run(host='localhost', port=8000)