import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dataConverter import *
from getData import *

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def main():
  DataGetter.auth()

  events_result = DataGetter.get_for_week(datetime.datetime.now())

  events = events_result.get("items", [])

  print(f'Got {len(events)} upcoming events for you')
  
  if not events:
    print("No upcoming events found.")
    return
  # Prints the start and name of the next 10 events
  for event in events:
    start = event["start"].get("dateTime", event["start"].get("date"))
    try:
      print(start, event["summary"])
    except KeyError:
      print(event)


if __name__ == "__main__":
  main()