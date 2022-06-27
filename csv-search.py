import pandas as pd


# Create dataframe from CSV
df = pd.read_csv('fr.csv', na_filter = '')

df= df[ df['Product'].str.contains('Vault',case=False) ]
df= df[ df['New or Existing'].str.contains('New', case=False) ]

search_str = 'azure'

df= df[ df['Feature Request Title'].str.contains(search_str,case=False) | \
        df['What Currently Happens'].str.contains(search_str,case=False) | \
        df['What is Desired'].str.contains(search_str,case=False) ]
    
df = df[ ['Feature Request Title', 'What Currently Happens','What is Desired', 
          'Asana Task ID','Asana Sub Task ID']]

df.to_excel('fr-search-output.xlsx', index=None, header=True)
