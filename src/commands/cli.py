import argparse
from typing import Dict
from inquirer.questions import Password
from helpers.browser import open_browser
from .options import cli_options
from argparse import Namespace
from utils.query import builder


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
        url = None
        try:
            if(self.args.option == 1):
                url = self.__query_build_general__(vars(self.args))
            elif(self.args.option == 2):
                url = self.__query_build_insta__(vars(self.args))
            elif(self.args.option == 3):
                url = self.__query_build_phone__(vars(self.args))
            else:
                raise Exception("Invalid option Error")
        except Exception as e:
            self.parser.print_usage()
            return
        print(url)
        open_browser(url=url)

    def __query_build_general__(self, args: Dict) -> str:
        '''Need add two more features'''

        site = f' site: {args.get("site")}' if args.get(
            "site") is not None else None
        url: str = f' https://google.com/search?q={args.get("search_query")}{site} '
        url += builder.exclude_site(args.get("exclude"))
        return url


    def __query_build_insta__(self, args: Dict) -> str:
        if any(args):
            pass

    def __query_build_phone__(self, args: Dict) -> str:
        if any(args):
            pass
