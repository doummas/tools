import sys
import requests

#This script used to grab all source directory of website from their source code

def get_source_code(website):
    source=requests.get(website)
    if source.status_code == 200:
        return source.text
    else:
        print(f"reponse must be 200 and you get {source.status_code}\n")
        return False
    
def filter_source_code(code):
    for i in range(len(code)):
        if  code[i:i+3] == "src":
            ai=code.find("<",i)
            s=code.find(" ",i)
            eq=code.find("=",i)
            if s<ai:
                y=code[eq+2:s]
            else:
                y=code[eq+2:ai]
            y=y.strip()
            y=y.strip('"')
            
            with open("directories.txt", "a") as file:
                file.write(f"{y}\n")

            

def help():
    print(f"Usage: python3 {__file__} website_url")




try:
    website=sys.argv[1]
    if website == "-h" or website=="--help" or website=="":
        help()
    else:
        code=get_source_code(website)
        filter_source_code(code)
except IndexError:
    help()



