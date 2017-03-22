

def todo(request):
    html = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body = '<h1>hello bbq</h1>'

    return html + '\r\n' + body

route_todo = {
    '/todo': todo
}