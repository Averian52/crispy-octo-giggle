import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


# Read data from spreadsheet
data = pd.read_excel('Risk_Distribution.xlsx', sheet_name='Deliquency Scores')

# Get unique names and IDs
names = data['Business Name'].unique()
ids = data['D-U-N-S Number'].unique()

# Create a list to store the scores for each company
scores_list = []

# Create a dictionary to store data for each company
data_dict = {name: data[data['Business Name'] == name] for name in names}

# Loop through each company
for name in data_dict:
    company_data = data_dict[name]
    
    # Get current score
    current_score = company_data[['Current Score']].values[0][0]
    current_date = company_data[['Current Date']].iloc[0,0]
    
    # Get monthly scores for last year
    monthly_scores = company_data.iloc[:, 4:16]
    monthly_dates = [current_date - pd.DateOffset(months=i) for i in range(1,13)]
    monthly_dates.reverse()
    
    # Convert date to string
    current_date = current_date.strftime("%Y-%m-%d")
    monthly_dates = [date.strftime("%Y-%m-%d") for date in monthly_dates]
    
    # Create a list of scores and dates for this company
    company_scores = list(monthly_scores.values[0])
    company_scores.insert(0, current_score)
    company_dates = [datetime.strptime(d, '%Y-%m-%d') for d in [current_date] + monthly_dates]
    
    # convert score to int
    company_scores = [int(i) for i in company_scores]
    
    # Add the scores and dates for this company to the main list
    scores_list.append({'name': name, 'scores': company_scores, 'dates': company_dates})
    
# Extract scores of all companies
all_scores = [score['scores'] for score in scores_list]
all_scores = np.concatenate(all_scores)

# Find percentiles
lower_percentile = np.percentile(all_scores, 25)
middle_percentile = np.percentile(all_scores, 50)
upper_percentile = np.percentile(all_scores, 75)

# Create lists to store scores for lower, middle and upper percentiles
lower_scores = []
middle_scores = []
upper_scores = []

# Iterate through the list of scores
for score in scores_list:
    name = score['name']
    scores = score['scores']
    dates = score['dates']    
    
    if name == 'Bouygues UK':
        lower_scores.append({'name': name, 'scores': scores, 'dates': dates})
        middle_scores.append({'name': name, 'scores': scores, 'dates': dates})
        upper_scores.append({'name': name, 'scores': scores, 'dates': dates})
    elif scores[0] < lower_percentile:
        lower_scores.append({'name': name, 'scores': scores, 'dates': dates})
    elif scores[0] < upper_percentile:
        middle_scores.append({'name': name, 'scores': scores, 'dates': dates})
    else:
        upper_scores.append({'name': name, 'scores': scores, 'dates': dates})

# Create a figure and axes for the lower percentile graph
fig1, ax1 = plt.subplots(figsize=(15, 8))
ax1.xaxis_date()

# Plot scores for lower percentile
for score in lower_scores:
    ax1.plot(score['dates'], score['scores'], label=score['name'])
    
# Add labels and legend to the graph
plt.xlabel('Date')
plt.ylabel('Score')
plt.legend()

# Set title
ax1.set_title('Scores for lower percentile')

# Create a figure and axes for the middle percentile graph
fig2, ax2 = plt.subplots(figsize=(15, 8))
ax2.xaxis_date()

# Plot scores for middle percentile
for score in middle_scores:
    ax2.plot(score['dates'], score['scores'], label=score['name'])
    
# Add labels and legend to the graph
plt.xlabel('Date')
plt.ylabel('Score')
plt.legend()

# Set title
ax2.set_title('Scores for middle percentile')

# Create a figure and axes for the upper percentile graph
fig3, ax3 = plt.subplots(figsize=(15, 8))
ax3.xaxis_date()

# Plot scores for upper percentile
for score in upper_scores:
    ax3.plot(score['dates'], score['scores'], label=score['name'])
    
# Add labels and legend to the graph
plt.xlabel('Date')
plt.ylabel('Score')
plt.legend()

# Set title
ax3.set_title('Scores for upper percentile')

# Show the plots
plt.show()