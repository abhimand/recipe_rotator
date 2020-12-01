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

while True: 
    ### questionnaire flow
    prelimChoices = ['Randomly select a recipe', 'Choose a recipe',  'Add a recipe']
    prelimQuestions = [
        inquirer.List('choice',
                    message="What do you want to do today?",
                    choices=prelimChoices
                    )
    ]
    answers = inquirer.prompt(prelimQuestions)

    ### Random
    if answers['choice'] == prelimChoices[0]: 
        rr.randomSelect(df, data)

    ### Select
    if answers['choice'] == prelimChoices[1]: 
        rs.selecting(df, data)

    ### Add
    if answers['choice'] == prelimChoices[2]: 
        rr.randomSelect(df, data)

    ### Check if user is done
    finishedQuestion = [
        inquirer.List('fin',
                    message="Finished?",
                    choices=['Yes','No']
                    )
    ]
    answers = inquirer.prompt(finishedQuestion)
    if answers['fin'] == 'Yes': 
        break
print('Thank you! Have a good day :)' + '\n\n\n\n')
print('P.S. There is a text file for all the recipes we displayed for your viewing purposes. Enjoy!' + '\n')

    