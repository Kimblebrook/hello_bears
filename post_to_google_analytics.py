from google_measurement_protocol import Event, report
import os
import pandas as pd

os.environ['HTTPS_PROXY'] = 'http://proxy01aws.int.xbridge.com:3128'
os.environ['HTTP_PROXY'] = 'http://proxy01aws.int.xbridge.com:3128'

v = 1                           # Measurement Protocol version.
tid = 'UA-8804762-6'            # The Tracking ID for the property. This is Simply Business - Universal.
cid = '2094329444.1440323430'   # The user's Google Analytics cid.
t = 'event'                     # The measurement protocol hit type.
category = 'Lead Scoring'       # An arbitrary event category, any value can be used.
action = 'Set Score'            # An event action, any value can be used.
custom1 = 1                     # Custom dimension index 1 value, your first CRM user attribute.
ni = '1'                        # This sets the hit as a non interaction hit.


df = pd.read_csv('/Users/sduncan/Temp/ga_cookies.csv',
                 dtype={'client_id': str})

df = df.head()

extra_info = [{'cd1': 'custom1', 'cd2': 'custom2'}]

for index, row in df.iterrows():
    event = Event(category=category, action=action)
    cid = str(row['client_id'])
    report(tid, cid, event, extra_info=extra_info)
    print 'Sent', cid

print 'Done!'
