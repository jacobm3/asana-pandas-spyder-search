#!/usr/bin/python3

import pandas as pd

# Create dataframe from CSV
# This comes from Google Sheet 'Request List - Read Only'
# Save the 'Requests' tab to 'fr.csv'
df = pd.read_csv('fr.csv', na_filter = '')

print(len(df), 'initial rows')

# Filter down to just Vault requests
df= df[ df['Product'].str.contains('Vault',case=False) ]
print(len(df), 'rows Product=Vault')

# Only look at the new requests, not the additional customer subtasks on existing tasks
df= df[ df['New or Existing'].str.contains('New', case=False) ]
print(len(df), 'rows only New')

# Text string used to search
search_str = 'azure'

# Return any tasks that have that string in the title or the currently happens or desired fields.
df= df[ df['Feature Request Title'].str.contains(search_str,case=False) | \
        df['What Currently Happens'].str.contains(search_str,case=False) | \
        df['What is Desired'].str.contains(search_str,case=False) ]

print(len(df), 'rows searching for %s' % search_str)

# Filter previous results down to only include results that also have an additional string
search_str = 'storage'
df= df[ df['Feature Request Title'].str.contains(search_str,case=False) | \
        df['What Currently Happens'].str.contains(search_str,case=False) | \
        df['What is Desired'].str.contains(search_str,case=False) ]

print(len(df), 'rows searching for %s' % search_str)

# Negative search, omit any FRs with 'TLS' in the title
neg_str = 'TLS'
df = df[~df['Feature Request Title'].str.contains(neg_str)]
print(len(df), 'rows after omitting %s' % neg_str)
print()

# Create a new dataframe with only the columns we're interested in
df = df[ ['Feature Request Title', 'What Currently Happens', 'What is Desired', 'Asana Task ID']]

# Add a direct link to the task
df['Asana Link'] = "https://app.asana.com/0/112957393038545/" + df['Asana Task ID']
df['Asana Link Excel'] = '=HYPERLINK("https://app.asana.com/0/112957393038545/' + df['Asana Task ID'] + '", "link")'

print('Dataframe Head:')
print(df.head())

outputfile='fr-search-output.xlsx'
print('Writing new spreadsheet: %s' % outputfile)
df.to_excel(outputfile, index=None, header=True)
