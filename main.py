import csv
import sys
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name','company','email','position']
clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_client_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name,mode='w') as f:
        writer = csv.DictWriter(f,fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('client already is in the client\'s list')


def list_clients():
    print('uid | name | company | email | position')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position'],
        ))


def update_client(client_id,updated_client):
    global clients
    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client is not in client\'s list.')
        


def delete_client(client_id):
    global clients
    for idx,client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name,message = "waht is the client{}? "):
    field = None

    while not field:
        field = input(f'What is the client {field_name}? ')
    
    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client


def _print_welcome():
    print('=' * 50)
    print('Welcome to Platzi Sales')
    print('=' * 50)
    print(f'What would you like to do today?')
    print(f'[C]reate client')
    print(f'[L]list client')
    print(f'[U]pdate client')
    print(f'[D]elete client')
    print(f'[S]earch client')


if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome()
    
    command = input().upper()


    if command == 'C':
       client = _get_client_from_user()

       create_client(client)
       
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id,updated_client)
        
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        if found:
            print(f'The client is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in client\'s list')
    else:
        print('Invalid command')

    _save_client_to_storage()