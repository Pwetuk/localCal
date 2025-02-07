import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dataConverter import *
import calExceptions as ce

class DataGetter:
    service = None
    SCOPES = ["https://www.googleapis.com/auth/calendar"]

    @classmethod
    def auth(cls) -> None:
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", cls.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", cls.SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        with open("token.json", "w") as token:
            token.write(creds.to_json())
        

        try: 
            cls.service = build("calendar", "v3", credentials=creds)
        except HttpError as error:
            print(f"An error occurred: {error}")
            raise ce.ServiceAuthFailedError
        
    @classmethod
    def _get_by_time(cls, start: datetime.datetime, end: datetime.datetime) -> list:

        events = (cls.service.events().list(
                calendarId="primary",
                timeMin=DataConverter.convert_datetime_to_google_format(start),
                timeMax=DataConverter.convert_datetime_to_google_format(end),
                singleEvents=True,
                orderBy="startTime",
            ).execute()
        )
        return events

    @classmethod
    def _check_if_none(cls) -> None:
        if cls.service is None:
            raise ce.ServiceIsNoneError

    @classmethod
    def get_for_week(cls, time: datetime.datetime) -> list:
        cls._check_if_none()
        
        start_week, end_week = DataConverter.get_week_bounds(time)
        
        events = cls._get_by_time(start_week, end_week)

        return events
    
    @classmethod
    def get_for_month(cls, time: datetime.datetime) -> list:
        cls._check_if_none()

        start_month, end_month = DataConverter.get_month_bounds(time)

        events = cls._get_by_time(start_month, end_month)

        return events
    
    @classmethod
    def add_event(cls, name: str, event_start: datetime.datetime, event_end: datetime.datetime, loc="") -> bool:
        cls._check_if_none()
        
        request_body = {
            "end": {
                "dateTime": DataConverter.convert_datetime_to_google_format(event_end),
            },
            "start": {
                "dateTime": DataConverter.convert_datetime_to_google_format(event_start)
            },
            "summary": name,
            "location": loc,
        }

        try: 
            cls.service.events().insert(
                calendarId="primary",
                body=request_body,
                
            ).execute()
        except Exception as exp:
            print(exp)
            return False
        
        return True