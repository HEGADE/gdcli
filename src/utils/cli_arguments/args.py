from commands.options import cli_options
import argparse
class Init():
      def _initialise_args__(self):
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

      def __str__(self) -> str:
          return f'Class that helps to initialize the commandline arguments'