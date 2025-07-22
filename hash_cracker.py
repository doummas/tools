import hashlib
import sys
from hasher import hasherr





if sys.argv[1] == "-h" or sys.argv[1] == "--help" or len(sys.argv)<3:
    print("" \
    "[+] Usage python3 hash.cracker.py  <wordlist>  <The hash> <algorithm>\n" \
    "the algorithm must be lower chase letter\n" \
    "supported algorithm:\n" \
    "md5\n" \
    "sha1\n" \
    "sha512")
    sys.exit(1)

algorithm=sys.argv[3]


def hashing_wordlist():
    wordlist = sys.argv[1]
    with open(wordlist , "r",encoding='latin-1') as file:
        for line in file:
            words=line.strip()
            hashed_pass=hasherr(words,algorithm)
            if hashed_pass == sys.argv[2]:
                try:
                    print(f"[+] the hash cracked Your password is {words}")
                except UnicodeDecodeError:
                    print("invalid charactere")
                exit()
                

            

            
hashing_wordlist()