import pandas as pd

class Details:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    #if wanting to use a dataframe
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }

list = []

list.append(Details(name='Jordon', age='24', gender='male'))
list.append(Details(name='Daniel', age='24', gender='male'))

print(list[0].name)

for person in list:
    print(person.name)

#convert to dataframe using the dictionary to create the coloumns
df = pd.DataFrame.from_records([info.to_dict() for info in list])
print(df)
