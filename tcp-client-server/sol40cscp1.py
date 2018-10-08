import socket
import sys
import argparse
import logging


ADDR = 'localhost'
PORT = 9999
BUFFER_MAX = 1024
CMDS = ['say', 'increment', 'bye', ]

actions = {
    'say': lambda word: word,
    'increment': lambda x: str(int(x) + 1),
    'bye': lambda bye: bye}

logger = logging.getLogger(__name__)
logging_file = 'tcp_server.log'


def run_logging():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(logging_file),
            logging.StreamHandler(sys.stdout)])


def start_server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)
    print(f'Listening at {sock.getsockname()}')

    scx, sock_addr = sock.accept()
    print(f'Accepted a connection from {sock_addr}')
    print('-> Socket host: ', scx.getsockname())
    print('-> Socket peer: ', scx.getpeername())
    logicnew(scx)


def logicnew(sc):
    with sc as clientsocket:
        while True:
            client_message = clientsocket.recv(BUFFER_MAX).decode()

            if not client_message:
                print("Client not available")
                break

            cmd, *sargs = client_message.split(' ', maxsplit=1)
            print(cmd)
            command = cmd.rstrip()
            print(command)

            if command in actions:

                if command == 'bye':
                    logger.debug("000 - Incoming message {}".format(client_message))
                    clientsocket.send(f"000 - See ya, {client_message}!".encode('utf-8'))
                    sys.exit(0)

                elif command == 'say' and not sargs or \
                        command == 'increment' and not sargs:
                    logger.debug('001 - Incoming message invalid or incomplete: {}'.format(client_message))
                    clientsocket.sendall('001 - Incomplete command'.encode("utf-8"))

                elif command == 'increment' and not sargs[0].isdigit():
                    logger.debug('002 - Incoming message: {}'.format(client_message))
                    clientsocket.sendall('002 - Invalid comment'.encode("utf-8"))

                elif command == 'increment' and sargs[0].isdigit():
                    logger.debug('003 - Incoming message: {}'.format(client_message))
                    clientsocket.send(actions[command](' '.join(sargs)).encode('utf-8'))

                else:
                    logger.debug("004 - Incoming message {}".format(client_message))
                    clientsocket.send(actions[command](' '.join(sargs)).encode('utf-8'))

            else:
                logger.debug("005 - Incoming message {}".format(client_message))
                clientsocket.send(f"005 - Invalid command: '{client_message}'".encode('utf-8'))


def start_client(host, prt):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with sock as cl_conn:
        try:
            cl_conn.connect((host, prt))
            print('Client has been assigned socket name', sock.getsockname())
        except ConnectionRefusedError:
            print("Oops! Can't connect to the TCP server.")
            cl_conn.close()
            sys.exit(0)

        while True:
            send = input('SEND MESSAGE: ').rstrip()
            if send == '':
                continue
            cl_conn.sendall(send.encode('utf-8'))
            print(f'\tRESPONSE: {cl_conn.recv(BUFFER_MAX).decode("utf-8")}')
            if send == 'bye':
                sys.exit(0)


def menu():
    print("\n*** TCP Server program ***")
    print("Please enter one of the following words/phrases:"
          "\n- say\n- increment (with an integer)\n- bye\n")


if __name__ == '__main__':
    choices = {'client': start_client, 'server': start_server}
    parser = argparse.ArgumentParser(description='TCP Server Exercise 40')
    parser.add_argument('role', choices=choices, help='which role to play.')
    parser.add_argument('-serverlog', required=False, default='off',
                        help='Enable logging, type: "-serverlog on", default is off',)
    args = parser.parse_args()
    run = choices[args.role]
    serv_log = args.serverlog
    if serv_log == 'on':
        run_logging()
    if args.role == 'client':
        menu()
        run(ADDR, PORT)
    else:
        run(ADDR, PORT)
