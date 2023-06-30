clients = 'Pablo,Ricardo'

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += ',' + client_name
        _add_comma()
    else:
        print('client already is in the client\'s list')


def list_clients():
    global clients
    print(clients)


def update_client(client_name,updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name + ',')
    else:
        print('Client is not in clients list')


def _add_comma():
    global clients
    if clients:
        clients += ','


def _print_welcome():
    print('=' * 50)
    print('Welcome to Platzi Sales')
    print('=' * 50)
    print(f'What would you like to do today?')
    print(f'[C]reate client')
    print(f'[U]pdate client')
    print(f'[D]elete client')


def _get_client_name():
    return input('What is your client name? ')


if __name__ == '__main__':
    _print_welcome()
    
    command = input().upper()


    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name ')
        update_client(client_name, updated_client_name)
        list_clients()
    else:
        print('Invalid command')