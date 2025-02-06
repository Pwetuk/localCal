import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dataConverter import *

class DataGetter:
    service = None
    SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

    def auth() -> None:
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", DataGetter.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", DataGetter.SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        with open("token.json", "w") as token:
            token.write(creds.to_json())
        

        try: 
            DataGetter.service = build("calendar", "v3", credentials=creds)
        except HttpError as error:
            print(f"An error occurred: {error}")
            raise "Failed to connect"
        
              

    def get_for_week(time: datetime.datetime) -> list:
        
        if DataGetter.service is None:
            raise "Error occured: something went wrong with auth"
        
        start_week, end_week = DataConverter.get_week_bounds(time)


        events = (DataGetter.service.events().list(
                calendarId="primary",
                timeMin=DataConverter.convert_datetime_to_google_format(start_week),
                timeMax=DataConverter.convert_datetime_to_google_format(end_week),
                singleEvents=True,
                orderBy="startTime",
            ).execute()
        )


        return events