#%%
# /workspaces/daytwostuff

# Should you include the environment in your repo or not?
# No

# Now what is your terminal display "path"? Is it different?
# /workspaces/daytwostuff
# Not different

# pip freeze requirements


#%%
import pandas as pd

df = pd.read_csv('Depression.csv')
df.head()

# %%
# What are three useful elements of Data Wrangler?
# 1. Can inspect data in interactive window in a clean way
# 2. This helps with aesthetically viewing and organizing data
# 3. Shows data and variable summaries automatically for the user  

# Plotly version: 6.5.1

# Why requirements.txt is used:
# We use a requirements.txt file to avoid version conflicts or conflicts that arise in 
# other environments since it keeps track of packages and versions. 