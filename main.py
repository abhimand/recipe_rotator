import pandas as pd 
import json
import inquirer

with open('./recipies.json') as f: 
    data = json.load(f)

print(data)

df = pd.read_json('./recipies.json')
print(df)


questions = [
  inquirer.List('mood',
                message="What are you in the mood for today?",
                choices=data['cuisine'],
            ),
]
answers = inquirer.prompt(questions)
print(answers['mood'])