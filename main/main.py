from __future__ import print_function
from upload_obj import *
import datetime

def main():

    # Таблица
    service_table = take_table()

    spreadsheetId = '1tnrBzbUkW1kEggxSopRGZL8dlID2gQejz7E_MP7MnmY'
    rangeName = 'A1:D5'
    result = service_table.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    for raw in values:
        print(raw)

    # Календарь
    service_calendar = take_calendar()

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    eventsResult = service_calendar.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event ['end'].get('dateTime',event['end'].get('date'))
        print(start, end, event['summary'])

if __name__ == '__main__':
    main()
