from __future__ import print_function
from take_credentials import *
import httplib2

from apiclient import discovery

def take_table():
    credentials_table = get_credentials('Roman_tables.json')
    http_table = credentials_table.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    service_table = discovery.build('sheets', 'v4', http=http_table, discoveryServiceUrl=discoveryUrl)
    return service_table


def take_calendar():
    credentials_calendar = get_credentials('Roman_calendar.json')
    http_calendar = credentials_calendar.authorize(httplib2.Http())
    service_calendar = discovery.build('calendar', 'v3', http=http_calendar)
    return service_calendar
