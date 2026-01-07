from mcrcon import MCRcon
from plugins.common import *

def rcon(server, password):
    # validate server
    if checkserver(server) == False: logging.error('Please input a real domain or server'); return

    # parse host and port
    if ':' in server:
        host, port = server.split(':')
        port = int(port)
    else:
        host = server
        port = 25575  # default RCON port

    try:
        # connect to the server using rcon
        with MCRcon(host, password, port=port) as mcr:
            logging.info(f'Type "exit" to exit the rcon client')

            # command loop
            while True:
               rcmd = input(f'{yellow}/')
               if rcmd == 'exit': mcr.disconnect(); return False
               resp = mcr.command(f"{rcmd}")
               print(resp)

    except Exception as e:
        print(e)
