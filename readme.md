# CLI for google dorks

This is the command line tool made with python which allows the users to perform
Google dorks easily 



## Installation

Install google dork cli using pip

```bash
 >> pip install gdcli
```
    
## Usage

```bash 
    >> gdcli -h
  

    1) -op 1 for general query
        >> gdcli -op 1 -q ninja -s instagram -e gamer

    2) -op 2 for instagram user finding
        >> gdcli -op 2 -q ninja -b gamer -l usa        

    3) -op 2 for phone number search
        >> gdcli -op 2 "223234566"

    4) -op to for specific filetype
        >> gdcli -op 3 -q python  -f docx
               



```


 






    
## options



| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-op` | `int` | **Required**. available options are [1,2,3] |
| `-q` | `string` | **Required**. Search Query |
| `-s` | `string` |Specifc site for searching|
| `-f` | `string` | File type|
| `-e` | `string` | Things to exclude|
| `-b` | `string` | Bio of the user|
| `-l` | `string` | location of the user like usa ,uk etc..|




  
### Note this cli tool is still on development process and more features will be added very soon,and feel free to contribute 🚀🚀

