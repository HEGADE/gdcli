
from typing import Dict
from helpers.browser import open_browser
from argparse import Namespace
from utils.query import builder
from utils.cli_arguments.args import Init
import sys


class Cli(Init):
    def __init__(self) -> None:
        self._initialise_args__()

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
        '''Need add two more features in general category'''
        if(any(args)):
            site = f' site: {args.get("site")}' if args.get(
                "site") is not None else None
            url: str = f' https://google.com/search?q={args.get("search_query")}{site} '
            url += builder.exclude_site(args.get("exclude"))
            return url
        else:
            sys.stdout.write(str("All values are entry"))
        return ''

    def __query_build_insta__(self, args: Dict) -> str:
        if any(args):
            #site:instagram.com (intext:ninja | intext:gamer) usa
            url: str = f' https://google.com/search?q=site: instagram.com (inurl:{args.get("search_query")}* | intext:{args.get("bio")}*) {args.get("location")}'
            return url

        else:
            sys.stdout.write(str("Values can not be empty"))
        return ''

    def __query_build_phone__(self, args: Dict) -> str:
        if any(args):
            pass
