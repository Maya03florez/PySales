clients = 'Pablo,Ricardo'

def create_client(client_name):
    global clients
    _add_comma()
    clients += client_name

def list_clients():
    global clients
    print(clients)

def _add_comma():
    global clients
    if clients:
        clients += ','

if __name__ == '__main__':
    list_clients()
    create_client('David')
    list_clients()
