'''
Title    -  Summarizing Data & Performing Statistics  
Problem  -  Crunch thru large datasets & generate summaries or 
            other kinds of stats  
'''

# pandas module 
# data analysis: stats, time series, etc
import pandas
rats = pandas.read_csv('statistics.csv', skip_footer=1)
print(rats)

print('\n!---SECTION---\n')

# investigate range of values for a certain field 
print(rats['status'].unique())

print('\n!---SECTION---\n')

# Filter the data 
crew_dispatched = rats[rats['status'] == 'SERVER_VERSION']
print(crew_dispatched)

print('\n!---SECTION---\n')



print('\n!---SECTION---\n')



print('\n!---SECTION---\n')



print('\n!---SECTION---\n')

