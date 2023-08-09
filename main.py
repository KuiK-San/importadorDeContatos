from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery 
from googleapiclient.errors import HttpError
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from time import sleep

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts', 'https://www.googleapis.com/auth/contacts.readonly']

def pathCsv():
    janela_padrao = Tk().withdraw()
    caminho_do_arquivo = askopenfilename(filetypes = (("Arquivos de texto", "*.csv"), ("Arquivos csv", "*.csv")))

    if caminho_do_arquivo:
        with open(caminho_do_arquivo, encoding='latin_1') as arquivo:
            return arquivo
    else:
        return None

def salvarContato(firstName, phone, creds, email = ''):
    

    try:
        # Get the Google API client
        client = googleapiclient.discovery.build('people', 'v1', credentials=creds)

        contact = {
            'names': [{'givenName': firstName}],
            'phoneNumbers': [{'value': phone}],
            'emailAddresses':[{'value': email}]
        }

        # Call the People API to create the contact
        response = client.people().createContact(body=contact).execute()

        # Print the contact's ID
        print(f'Contato de {name} salvo!')
    except HttpError as err:
        print(err)

def csv_to_dict(csv_file_path):
    data_dict = []
    with open(csv_file_path, 'r', newline='', encoding="UTF-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data_dict.append(row)
    return data_dict

def DesenharRiscos(qtd):
    for i in range(qtd):
        print("-", end="")
    


if __name__ == '__main__':
    creds = None
    
    DesenharRiscos(60)
    print("\nCriado e desenvolvido por: Guilherme Casagrande")
    DesenharRiscos(60)


    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        print('\nLogue sua conta google no Navegador')
        sleep(0.5)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    nome = input("\nInsira aqui o nome da coluna de nome no CSV: ")
    telefone = input("Insira aqui o nome da coluna de telefone no CSV: ")
    print(f'Agora você irá escolher onde está salvo o arquivo')
    sleep(0.5)
    path = pathCsv()
    if path == None:
        print('\nArquivo não encontrado!')
        sleep(3)
        exit()
    peoples = csv_to_dict(path.name)

    for people in peoples:
        name = people[nome]
        phone = people[telefone]
        phone = f'+55 {phone}'
        salvarContato(name, phone, creds)

    sleep(5)