#!/usr/bin/env python3
import pandas as pd 
import json
import inquirer
import random
import recipe_randomizer as rr
import recipe_selector as rs

# open json and convert to dataframe
with open('/Users/abhi.mand/Documents/Programming/Scripts/recipe_rotator/recipes.json') as f: 
    data = json.load(f)
df = pd.read_json('/Users/abhi.mand/Documents/Programming/Scripts/recipe_rotator/recipes.json', orient=str)

while True: 
    ### questionnaire flow
    prelimChoices = ['Randomly select a recipe', 'Choose a recipe']
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
print('Thank you! Have a good day :)' + '\n\n')
print('P.S. There is a folder for all the recipes we displayed for your viewing purposes. Enjoy!' + '\n\n\n')

    