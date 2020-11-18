# import pandas as pd 
# import json
import inquirer

# data is a dataframe
def selecting(data): 
    print(data)
    questions = [
        inquirer.List('mood',
                    message="Which cuisine?",
                    choices=data['cuisine'],
                )
        # inquirer.Text('count', message="For how many folks?")
    ]
    answers = inquirer.prompt(questions)