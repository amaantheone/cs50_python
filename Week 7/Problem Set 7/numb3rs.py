import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
     if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
         numbers_list = ip.split('.')
         for n in numbers_list:
             if int(n) > 255 or int(n) < 0:
                 return False
         return True
     else:
        return False

if __name__ == "__main__":
    main()
