import datetime
import os.path
import re

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


from partiful_data_extraction import extract_event_data

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly","https://www.googleapis.com/auth/calendar.events.readonly"]


def calendar_event_extraction():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=3000)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Pull all events from the Partiful calendar
    calendar_list = service.calendarList().list().execute()
    calendars = calendar_list.get("items")
    calendar_id = partiful_calender_extraction(calendars)
    print("partiful calendar id is",calendar_id)
    #events_result = service.events().list(calendarId=calendar_id).execute()

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId=calendar_id,
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    partiful_event_ids = []
    for event in events:
      description = event.get('description')
      if description is not None and 'partiful' in description:
        print("found partiful event")
        partiful_id = link_parser(description)
        if partiful_id is not None:
          partiful_event_ids.append(partiful_id)
      start = event["start"].get("dateTime", event["start"].get("date"))
    print("all partiful event ids found", partiful_event_ids)
    for events in partiful_event_ids:
      extract_event_data(events)
      # print(start, event["summary"])

  except HttpError as error:
    print(f"An error occurred: {error}")


def partiful_calender_extraction(calendars):
  for calendar in calendars:
    summary = calendar.get("summary")
    if summary == 'Partiful':
      print("calendar id found")
      calendar_id =  calendar.get("id")
      return calendar_id
  print("no calendar present")
  return None

def link_parser(text):
  pattern = r'^.*RSVP at.*$'
  matches = re.findall(pattern, text, re.MULTILINE)
  for match in matches:
      # extract id
      parse = match.split("/e/")
      print(parse)
      partiful_event_id = parse[1]
      return partiful_event_id
  return None