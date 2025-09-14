import sys
try:
        with open (sys.argv[1], "r") as file:
                for line in file:
                        for i in range (len(line)):
                                if line[i] == "\\":
                                        n=line[i+1:]
                                        for j in range (len(n)):
                                                if n[j] == "(":
                                                        r=n[:j]
                                                        with open ("output.txt", "a") as f:
                                                                f.writelines(f"{r}\n")
except IndexError:
        print("[+] usage: python3 lookupsid_filter <users file>")
