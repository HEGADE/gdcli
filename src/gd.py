
import sys
import os
from commands.cli import Cli
from helpers.browser import open_browser
from utils.query.select import options
selected_option=options()
cli=Cli(selected_option=selected_option["selected_option"])
print(cli.args.site,cli.args.search_query,cli.args.file_type,cli.args.exclude)

