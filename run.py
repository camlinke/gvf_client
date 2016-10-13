from socketIO_client import SocketIO

def on_response(*args):
    print('on_response', args)

baseurl = "http://138.68.16.188"
with SocketIO(baseurl, 80) as socketIO:
    socketIO.on('data', on_response)
    socketIO.wait()

