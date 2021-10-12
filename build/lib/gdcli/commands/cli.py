
from typing import Dict

from gdcli.helpers.browser import open_browser
from gdcli.utils.query import builder
from gdcli.utils.cli_arguments.args import Init
import sys


class Cli(Init):
    def __init__(self) -> None:
        self._initialise_args__()

    def __call__(self):
        url = None
        try:
            if(self.args.option == 1):
                url = self.__query_build_general__(vars(self.args))
            elif(self.args.option == 2):
                url = self.__query_build_insta__(vars(self.args))
            elif(self.args.option == 3):
                url = self.__query_build_phone__(vars(self.args))
            else:
                raise Exception("Invalid option specified")

        except Exception as e:
            sys.stdout.write(str(e))
            print()
            self.parser.print_usage()
            exit()
        if url is not None:
            print(url)
            open_browser(url=url)

    def __query_build_general__(self, args: Dict) -> str:
        try:
            if(any(args)):
                if(args.get("search_query") or args.get("bio") or args.get("location")):
                    site = f' site: {args.get("site")}' if args.get(
                        "site") else ''
                    url: str = f' https://google.com/search?q={args.get("search_query")} {site} '
                    excluded_site = builder.exclude_site(args.get("exclude"))
                    url += excluded_site if excluded_site else ''
                    return url
                else:
                    raise Exception(
                        "All required arguments are not provided\n")

            else:
                raise Exception("All values are empty")

        except Exception as e:
            sys.stdout.write(str(e))
            return

    def __query_build_insta__(self, args: Dict) -> str or None:
        if any(args):
            if args.get("search_query"):

                url: str = f' https://google.com/search?q=site: instagram.com (inurl:{args.get("search_query")}* | intext:{args.get("bio")}*) {args.get("location")}'
                return url
            else:
                raise Exception("User name is not provided")

        else:
            sys.stdout.write(str("Values can not be empty"))
        return None

    def __query_build_phone__(self, args: Dict) -> str:
        try:

            if any(args):
                if(args.get("search_query")):
                    url: str = f' https://google.com/search?q=inurl {args.get("search_query")} | intext: {args.get("search_query")} | inurl: {args.get("search_query")}'
                    return url
                else:
                    raise Exception("Should not be empty provide number\n")

            else:
                raise Exception("Values are empty")
        except Exception as e:
            sys.stdout.write(str(e))
            self.parser.print_usage()
        return None
