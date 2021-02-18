import csv
import pandas as pd

'''
with open('weather_data.csv') as f:
    data = csv.reader(f)
    data_list = list(data)
    temperatures = []
    for row in data_list[1:]:
        temperature = int(row[1])
        temperatures.append(temperature)
'''

data = pd.read_csv('weather_data.csv')
data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(len(temp_list))
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

print(data['temp'].mean())
print(data['temp'].max())

print(data['condition'])
print(data.condition)

print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)

monday_temp = monday.temp
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)


scores_data = {
    'students': ['Amy', 'Betty', 'Candy', 'Darcy', 'Eve', 'Fred'],
    'scores': [87, 94, 65, 90, 72, 85]
}

scores_df = pd.DataFrame(scores_data)
scores_df.to_csv('new_scores.csv')