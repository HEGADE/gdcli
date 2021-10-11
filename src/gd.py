
import sys
import os
from commands.cli import Cli
from helpers.browser import open_browser

cli=Cli()
print(cli.args.site,cli.args.search_query,cli.args.file_type,cli.args.exclude)

