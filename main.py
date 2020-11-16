import pandas as pd 
import json
import inquirer
import random

# open json and convert to dataframe
with open('./recipes.json') as f: 
    data = json.load(f)
df = pd.read_json('./recipes.json')

print(len(df['cuisine']['Asian'][0]['ingredients'][0]))

# questionnaire flow
questions = [
    inquirer.List('mood',
                message="What are you in the mood for today?",
                choices=data['cuisine'],
            )
    # inquirer.Text('count', message="For how many folks?")
]
answers = inquirer.prompt(questions)

# choose recipe
cuisine = df['cuisine']

mood = answers['mood']
length = len(cuisine[mood])
index = random.randint(0,length - 1)

# ingredients list
print('Our choice: ' + cuisine[mood][index]['name'])
print()
print('List of Ingredients:')
ingredients = cuisine[mood][index]['ingredients']
for ingredient in ingredients:
    print(ingredient['name'])
    # if meat option