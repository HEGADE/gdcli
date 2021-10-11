import inquirer
from typing import Dict
 
def options()->Dict: 
    questions = [
        inquirer.List(
            "selected_option",
            message="Select the options to continue",
            choices=["General topics and files", "Instgram user finder", "Phone number finder",],
        ),
    ]

    selected_options = inquirer.prompt(questions)
    return selected_options

if __name__=="__main__":
    print(options())