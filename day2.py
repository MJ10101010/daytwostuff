#%%
# /workspaces/daytwostuff

# Should you include the environment in your repo or not?
# No

# Now what is your terminal display "path"? Is it different?
# /workspaces/daytwostuff
# Not different


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

# Recipe:
# 1. Create an empty Github repository
# 2. Open VScode terminal and create a new project folder
# 3. Navigate/cd into the project folder
# 4. Initialize git and create the main branch
# 5. Create and activate a virtual environment
# 6. Install necessary python packages
# 7. Create requirements.txt from the installed packages
# 8. Create a .gitignore file and add lines to ignore unnecessary files like:
#       venv/
#       __pycache__/
#       *.pyc
# 9. Add other project files, like recipe.py 
# 10. Stage/add, commit, and push to github
