import pandas as pd 
import inquirer
import random

### dataframe object passed thru and raw data
def randomSelect(df, data): 
    ### inquire
    answers = inquire(data)

    ### choose recipe
    mood = df['cuisine'][answers['mood']]
    index = random.randint(0,len(mood) - 1)

    ### ingredients list
    string = ingredientsList(mood[index])
    print(string)
    ### write to textfile
    text_file = open(mood[index]['name'] + ".txt", "w")
    n = text_file.write(string)
    text_file.close()


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
    numLen = 75 # change if necessary
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
    string += '-'*numLen + '\n' + stepList(meal) + '-'*numLen + '\n'
    return string

def stepList(meal) -> str: 
    string = 'Steps: \n\n'
    for index, step in enumerate(meal['steps']): 
        string += str(1 + index) + '. ' + step + '\n'
    return string
        


