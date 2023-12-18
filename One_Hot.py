import pandas as pd
import random
# Создаем исходный DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()


# Создаем новый DataFrame для хранения one hot видов
one_hot_data = pd.DataFrame(index=data.index, columns=['robot', 'human'])

# Заполняем значения в one hot виде
for index, row in data.iterrows():
    one_hot_data.loc[ index, 'robot'] = 1 if row['whoAmI'] == 'robot' else 0
    one_hot_data.loc[ index, 'human'] = 1 if row['whoAmI'] == 'human' else 0


# Выводим one hot вид
print(one_hot_data)