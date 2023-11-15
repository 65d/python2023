import pandas as pd

data = pd.read_csv("russia_losses_equipment.csv")


# data = data.dropna()
data = data.drop_duplicates()
print(data.head())

statistics = data.describe()
print(statistics)

# grouped_data = data.groupby('aircraft').mean()
# print(grouped_data)



import matplotlib.pyplot as plt
#
# # Приклад візуалізації гістограми для стовпця "змінна"
data['helicopter'].plot(kind='hist', bins=20)
plt.title('Назва графіку')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.show()
