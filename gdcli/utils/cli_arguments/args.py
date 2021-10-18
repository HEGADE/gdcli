from gdcli.commands.options import CLI_OPTIONS, DISPLAY_OPTIONS
import argparse


class Init():
    def _initialise_args__(self):
        self.parser = argparse.ArgumentParser(
            '''Commamd line tool for Google dorks\n

            1) -op 1 for general query \n
             >> gdcli -op 1 -q ninja -s instagram -e gamer \n

            2) -op 2 for instagram user finding
              >> gdcli -op 2 -q ninja -b gamer -l usa
              
            3) -op 2 for phone number search
              >> gdcli -op 2 "223234566"

            4) -op to for specific filetype
              >> gdcli -op 3 -q python  -f docx
               
            ''')
        self.parser.add_argument(
            CLI_OPTIONS[4], dest=DISPLAY_OPTIONS[0], type=int, help="Option [1 2 3 4]")
        self.parser.add_argument(
            CLI_OPTIONS[0], dest=DISPLAY_OPTIONS[1], type=str, help="Search Query ")
        self.parser.add_argument(
            CLI_OPTIONS[1], dest=DISPLAY_OPTIONS[2], type=str, help=" Specifc site for searching ")
        self.parser.add_argument(
            CLI_OPTIONS[2], dest=DISPLAY_OPTIONS[3], type=str, help="File type")
        self.parser.add_argument(
            CLI_OPTIONS[3], dest=DISPLAY_OPTIONS[4], type=str, help="Things to exclude")
        self.parser.add_argument(
            CLI_OPTIONS[5], dest=DISPLAY_OPTIONS[5], type=str, help="Bio of the user")
        self.parser.add_argument(
            CLI_OPTIONS[6], dest=DISPLAY_OPTIONS[6], type=str, help="Bio of the user")
        self.args = self.parser.parse_args()

    def __str__(self) -> str:
        return f'Class that helps to initialize the commandline arguments'
