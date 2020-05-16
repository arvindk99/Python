import socket
import connectfour
from collections import namedtuple

ConnectfourConnection = namedtuple(
    'ConectfourConnection',
    ['socket', 'input', 'output'])

class I32CFSP_Error(Exception):
    pass

def hostname()-> str:
    '''This function will ask the user for a hostname.
    if it is an invalid host name, it will loop until the user inputs a valid hostname'''
    while True:
        hostname = input("Enter a hostname: ")
        if hostname == '':
            print("Enter a valid hostname.")
        else:
            return hostname.strip('')

def portnumber()->int:
    '''This function asks the user for a portnumber
    If the user enters an invalid portnumber it loops until the user
    inputs something valid and the reutrns in port number'''
    while True:
        try:
            portnumber = int(input("Enter a port number: "))
            if portnumber <= 0 or portnumber >= 65535:
                print("Enter a valid port number.")
            else:
                return portnumber
        except ValueError:
            print("Enter a valid portnumber.")

def connect(hostname,portnumber) -> 'connection':
    '''Connects to the connect four server, which is assumed to be
    running on the given host and listening on the given port. If successful,
    a connection  object is returned; if unsuccessful, an exception is raised.'''
    while True:
        try:
            cfour_socket = socket.socket()
            cfour_socket.connect((hostname, portnumber))
            cfour_input = cfour_socket.makefile('r')
            cfour_output = cfour_socket.makefile('w')

            return ConnectfourConnection(
                socket=cfour_socket,
                input=cfour_input,
                output=cfour_output)

        except socket.gaierror:
            raise I32CFSP_Error

        except ConnectionRefusedError:
            raise I32CFSP_Error

def close(connection)->None:
    '''Closes connection to the server.'''
    connection.input.close()
    connection.output.close()
    connection.socket.close()

def sendmessage(connection,input)-> None:
    '''Sends a message to the server.'''
    while True:
        try:
            connection.output.write(input + '\r\n')
            connection.output.flush()

        except ValueError:
            raise I32CFSP_Error

        else:
            break

def recvmessage(connection)->str:
    '''Receives a message from the server.'''
    message = connection.input.readline()[:-1]
    return message

def welcomelogin(connection,username:str)->'WELCOME':
    '''Function reads the message, and if it is a valid login,
    prints Welcome username, if invalid, raises an error.'''
    username = username.replace(' ', '')
    sendmessage(connection, 'I32CFSP_HELLO '+ username)
    print(username)
    welcome = recvmessage(connection)

    if welcome[:7] != 'WELCOME':
        raise I32CFSP_Error

    else:
        return welcome

def startaigame(connection)-> int:
    '''Function sends and receives message, if the
    message is valid, starts the AI game.'''
    sendmessage(connection,'AI_GAME')
    ready = recvmessage(connection)

    if  len(ready) !=5 or ready != 'READY':
        raise I32CFSP_Error

    else:
        ready = connectfour.RED
        return ready

def startconnection()->'connection':
    '''This function expects the user to connect to the connectfour server,
    if the host name is invalid, it will loop and check for the input until its valid.'''
    while True:
        host = hostname()
        port = portnumber()
        print("Connecting to connectfour server '{}' '{}'...".format(host, port))

        if host != 'woodhouse.ics.uci.edu':
            print(host)
            print("Could not connect... Try again.")

        elif port != 4444:
            print(port)
            print("Could not connect... Try again.")

        else:
            connection = connect(host, port)
            print("Connected!")
            return connection

def turncolor(connection)->int:
    '''This function uses a series of if and elif statements
    to check what the current turn is, and returns the turn as the turn color.'''
    response = recvmessage(connection)

    if response == 'READY':
        response = connectfour.RED
        return response

    elif response == 'OKAY':
        response = connectfour.YELLOW
        return response

    elif response[:4] == 'DROP':
        response = connectfour.YELLOW
        return response

    elif response[:3] == 'POP':
        return response

    elif response == 'INVALID':
        response = connectfour.RED
        return response

    elif response == 'WINNER_RED':
        response = int(11)
        return response

    elif response == 'WINNER_YELLOW':
        response = int(22)
        return response

    else:
        raise I32CFSP_Error

def servermove(connection)-> list:
    '''This function receives the server move and splits it into a list.'''
    turn = recvmessage(connection)
    while True:
        if turn[:4] == 'DROP' or turn[:3] == 'POP':
            movelist = []
            move = turn.split()
        else:
            break

        if move[0] == 'DROP' or move[0]== 'POP':
            movelist.append(move[0])
        else:
            print(move[0], move[1])
            raise I32CFSP_Error

        if int(move[1]) >= 0 and int(move[1]) <8:
            movelist.append(int(move[1]) - 1)
        else:
            print(move[0],move[1])
            raise I32CFSP_Error
        return movelist
