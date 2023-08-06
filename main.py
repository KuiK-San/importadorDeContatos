from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery 
from googleapiclient.errors import HttpError


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts', 'https://www.googleapis.com/auth/contacts.readonly']


def main():
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Get the Google API client
        client = googleapiclient.discovery.build('people', 'v1', credentials=creds)

        # Set the contact's name
        name = 'Guilherme Casagrande'

        # Set the contact's email address
        email = 'gui@casagrande.com'

        # Set the contact's phone number
        phone = '+55 11 9999-9999'

        # Create the contact
        contact = {
    'names': [{'givenName': 'Guilherme', 'familyName': 'Casagrande'}],
    'phoneNumbers': [{'value': phone}]
}

        # Call the People API to create the contact
        response = client.people().createContact(body=contact).execute()

        # Print the contact's ID
        print(response['resourceName'])
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()