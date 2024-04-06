## Opjectives

# Explore features or characteristics to predict price of car
# Analyze patterns and run descriptive statistical analysis
# Group data based on identified parameters and create pivot tables
# Identify the effect of independent attributes on price of cars

# Import libraries:
import pandas as pd
import numpy as np

# Load the data and store it in dataframe df:
path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()
