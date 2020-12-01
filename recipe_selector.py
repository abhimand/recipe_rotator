# import pandas as pd 
# import json
import inquirer

# data is a dataframe
def selecting(df, data): 
    questions = [
        inquirer.List('mood',
                    message="Which cuisine?",
                    choices=data['cuisine'],
                )
        # inquirer.Text('count', message="For how many folks?")
    ]
    answers = inquirer.prompt(questions)
    displayList(answers['mood'], df, data)


def displayList(mood, df, data):
    print(data[mood])
