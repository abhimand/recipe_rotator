# import pandas as pd 
# import json
import inquirer
import recipe_randomizer as rr


# data is a dataframe
def selecting(df, data): 
    questionMood = [
        inquirer.List('mood',
                    message="Which cuisine?",
                    choices=data['cuisine'],
                )
        # inquirer.Text('count', message="For how many folks?")
    ]
    answers = inquirer.prompt(questionMood)

    mood = df['cuisine'][answers['mood']]

    questionMeal = [
        inquirer.List('meal',
                    message="Which meal?",
                    choices=[m['name'] for m in mood],
                )
    ]
    answers = inquirer.prompt(questionMeal)
    for m in mood: 
        if m['name'] == answers['meal']:
            string = rr.ingredientsList(m)
            rr.saveAsTextFile(m, string)
            print(string)
            break
