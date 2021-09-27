import pandas as pd

# Create dataframe from CSV
df = pd.read_csv('Field_Requests.2021.09.27.csv', na_filter = '')

# Filters

# Eliminate named customer subtasks
df = df[~df['Name'].str.contains(r'(^Customer |^Existing |^Prospect )')]

# Restrict to New Requests section
df= df[ df['Section/Column'] == 'New Requests' ]

# Tasks get a Completed At date when marked complete
#
# This will be empty for New/incomplete tasks
df = df[ df['Completed At'] == '' ]
#
# This will find Completed tasks
#df = df[ df['Completed At'] != '' ]

# Searching specific columns
# Works like grep. Add multiple lines for AND. Use regex | for OR.
#
# ldap AND root
#df = df[df['Name'].str.contains(r'(ldap|ad |active directory)', case=False)]
#df = df[df['Name'].str.contains(r'(ui)', case=False)]
#df = df[df['Created At'] > '2021-01-01']
#
# ldap OR root
# df = df[df['Name'].str.contains(r'(ldap|root)', case=False)]

# Add direct link to each task. Add your project ID in place of xxxx
df['Link'] = 'https://app.asana.com/0/xxxx/' + df['Task ID']
#df = df[ ['Link', 'Created At','Completed At', 'Name','Section/Column']]
df = df[ ['Link', 'Created At', 'Name','Section/Column']]

#df.to_excel (r'vfr-output.xlsx', index = None, header=True)
