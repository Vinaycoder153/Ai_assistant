from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import pytz

def get_today_events(creds_path="token.json", timezone="Asia/Kolkata"):
    try:
        creds = Credentials.from_authorized_user_file(creds_path)
        service = build('calendar', 'v3', credentials=creds)

        now = datetime.now(pytz.timezone(timezone))
        start = now.isoformat()
        end = (now + timedelta(days=1)).isoformat()

        events_result = service.events().list(
            calendarId='primary', timeMin=start, timeMax=end,
            singleEvents=True, orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])
        return [f"{e.get('summary', 'Unnamed Event')} at {e['start'].get('dateTime', e['start'].get('date'))}" for e in events]

    except Exception as e:
        return [f"Error fetching calendar events: {str(e)}"] 