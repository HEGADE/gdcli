# CLI for google dorks

This is the command line tool made with pytohn which allows the users to perform
Google dorks easily 



## Installation

Install google dork cli

```bash
  >> pip Install gdcli
  
```
    
## Usage

```bash 
    gdcli -h
  

    1) -op 1 for general query

        >> gd -op 1 -q ninja -s instagram -e gamer

    2) -op 2 for instagram user finding
        >> gd -op 2 -q ninja -b gamer -l usa



[-h] [-op OPTION] [-q SEARCH_QUERY] [-s SITE] [-f FILE_TYPE] [-e EXCLUDE] [-b BIO] [-l LOCATION]        

optional arguments:
  -h, --help       show this help message and exit
  -op OPTION       Option [1 2 3]
  -q SEARCH_QUERY  Search Query
  -s SITE          Specifc site for searching
  -f FILE_TYPE     File type
  -e EXCLUDE       Things to exclude
  -b BIO           Bio of the user
  -l LOCATION      Bio of the user

```