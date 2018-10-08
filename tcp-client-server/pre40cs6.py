import socket
import sys
import argparse
import logging


ADDR = 'localhost'
PORT = 9999
BUFFER_MAX = 1400
CMDS = ['say', 'increment', 'bye', ]

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
    logic(scx)


def logic(sc):
    with sc as sc_conn:
        while True:
            data = sc_conn.recv(BUFFER_MAX).decode().split(' ', 1)
            if not data[0]:
                print("Client not available")
                break

            if data[0] in CMDS:
                data.append('')
                if data[0] == 'bye':
                    logger.debug('Incoming message: {}'.format(data[0]))
                    sc_conn.sendall(data[0].encode('utf-8'))
                    sc_conn.close()    # make sure connection is closed
                    print('Reply sent, socket closed')
                    sys.exit(0)

                elif data[0] == 'say' and data[1] == '' or \
                        data[0] == 'increment' and data[1] == '':
                    logger.debug('Incoming message invalid: {}'.format(data[0]))
                    sc_conn.sendall('Incomplete command - 1.'.encode("utf-8"))

                elif data[0] == 'say' and not data[1].isdigit():
                    logger.debug('Incoming message: {}, {}'.format(data[0], data[1]))
                    sc_conn.sendall(data[1].encode('utf-8'))

                elif data[0] == 'increment' and data[1].isdigit():
                    logger.debug('Incoming message: {}, {}'.format(data[0], data[1]))
                    sc_conn.sendall(str(int(data[1]) + 1).encode('utf-8'))

                else:
                    logger.debug('Incoming message invalid: {}'.format(data[0]))
                    sc_conn.sendall('Unknown command - 2 .'.encode("utf-8"))

            else:
                logger.debug('Incoming message invalid: {}'.format(data[0]))
                sc_conn.sendall('Unknown command.'.encode("utf-8"))


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
            send = input('SEND MESSAGE: ').strip()
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
