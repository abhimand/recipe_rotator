import pandas as pd 
import json
import inquirer
import random
import recipe_randomizer as rr
import recipe_selector as rs

# open json and convert to dataframe
with open('./recipes.json') as f: 
    data = json.load(f)
df = pd.read_json('./recipes.json')

### questionnaire flow
prelimChoices = ['Choose a recipe', 'Randomly select a recipe', 'Add a recipe']
prelimQuestions = [
    inquirer.List('choice',
                message="What do you want to do today?",
                choices=prelimChoices
                )
]
answers = inquirer.prompt(prelimQuestions)

### Select
if answers['choice'] == prelimChoices[0]: 
    print(data['cuisine'])
    s.selecting(df)

### Random
if answers['choice'] == prelimChoices[1]: 
    rr.randomSelect(df, data)

### Add