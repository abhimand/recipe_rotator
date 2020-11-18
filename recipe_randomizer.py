import pandas as pd 
import inquirer
import random

# dataframe object passed thru and raw data
def randomSelect(df, data): 
    # inquire
    answers = inquire(data)

    # choose recipe
    mood = df['cuisine'][answers['mood']]
    index = random.randint(0,len(mood) - 1)

    # ingredients list
    print(ingredientsList(mood[index]))


def inquire(data) -> dict: 
    questions = [
        inquirer.List('mood',
                    message="What are you in the mood for today?",
                    choices=data['cuisine'],
                )
        # inquirer.Text('count', message="For how many folks?")
    ]
    answers = inquirer.prompt(questions)
    return answers

def ingredientsList(meal) -> str: 
    numLen = 50 # change if necessary
    string = '-'* numLen + '\n'
    string += 'Our choice: ' + meal['name'] + '\n'
    string += '-'* numLen + '\n'
    string += 'List of Ingredients:' + '\n\n'

    ingredients = meal['ingredients']
    for ingredient in ingredients:
        name = ingredient['name'].ljust(numLen)
        quant = ingredient['quantity'].rjust(numLen)
        lenAmt = numLen - len(ingredient['quantity'])
        string += name[0:lenAmt - 1] + ' ' + quant[lenAmt:numLen] + '\n'    
    string += '-'*numLen + '\n'
    string += stepList(meal)
    return(string)

def stepList(meal) -> str: 
    string = 'Steps: \n'
    for index, step in enumerate(meal['steps']): 
        string += str(1 + index) + '. ' + step + '\n'
    return string
        


