# import pandas as pd 
# import json
import inquirer
import recipe_randomizer as rr


# data is a dataframe
def selecting(df, data):
    ### inquire mood
    answers = inquireMood(data)
    ### extract mood
    mood = df['cuisine'][answers['mood']]
    ### inquire Meal
    answers = inquireMeal(mood)
    # present chosen list of meal
    for m in mood: 
        if m['name'] == answers['meal']:
            string = rr.ingredientsList(m)
            rr.saveAsTextFile(m, string)
            print(string)
            break


def inquireMood(data) -> dict:
    questionMood = [
        inquirer.List('mood',
                    message="Which cuisine?",
                    choices=data['cuisine'],
                )
    ]
    answers = inquirer.prompt(questionMood)
    return answers

def inquireMeal(mood) -> dict:
    questionMeal = [
        inquirer.List('meal',
                    message="Which meal?",
                    choices=[m['name'] for m in mood],
                )
    ]
    answers = inquirer.prompt(questionMeal)
    return answers