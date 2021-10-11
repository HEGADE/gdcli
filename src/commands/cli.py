import argparse
from inquirer.questions import Password

from helpers.browser import open_browser
from .options import cli_options
from utils.query import build


class Cli():
    def __init__(self) -> None:

        self.parser = argparse.ArgumentParser(
            "Commamd line tool for Google dorks")
        self.parser.add_argument(
            cli_options[4], dest="option", type=int, help="Option [1 2 3]")
        self.parser.add_argument(
            cli_options[0], dest="search_query", type=str, help="Search Query ")
        self.parser.add_argument(
            cli_options[1], dest="site", type=str, help=" Specifc site for searching ")
        self.parser.add_argument(
            cli_options[2], dest="file_type", type=str, help="File type")
        self.parser.add_argument(
            cli_options[3], dest="exclude", type=str, help="Things to exclude")
        self.args = self.parser.parse_args()

        print(type(self.args))

    def build_query(self):
        url=None
        try:
            if(self.args.option == 1):
                url = build.query_build_general(self.args)
            elif(self.args.option == 2):
               url= build.query_build_insta(self.args)
            elif(self.args.option == 3):
                url=build.query_build_phone(self.args)
            else:
                raise Exception("Invalid option ")
        except Exception as e:
            self.parser.print_usage()
            return
        open_browser(url)
                