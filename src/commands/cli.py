import argparse
from .options import cli_options

class Cli():
    def __init__(self) -> None:
        self.parser=argparse.ArgumentParser("Commamd line tool for Google dorks")
        self.parser.add_argument(cli_options[0],dest="search_query", type=str, help="Enter the search Query ")
        self.parser.add_argument(cli_options[1], dest="site", type=str, help=" Specifc site for searching ")
        self.parser.add_argument(cli_options[2], dest="file_type", type=str, help="File type")
        self.parser.add_argument(cli_options[3], dest="exclude", type=str, help="Things to exclude")
        self.args = self.parser.parse_args()



            
