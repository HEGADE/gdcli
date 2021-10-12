import inquirer
from typing import Dict
from src.commands.options import DISPLAY_OPTIONS



def options() -> Dict:
    questions = [
        inquirer.List(
            "selected_option",
            message="Select the options to continue",
            choices=[DISPLAY_OPTIONS[0],
                     DISPLAY_OPTIONS[1], DISPLAY_OPTIONS[2]]
        ),
    ]

    selected_options = inquirer.prompt(questions)
    return selected_options


if __name__ == "__main__":
    print(options())
