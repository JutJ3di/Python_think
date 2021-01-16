import random
from typing import final
import os

CONST_PATH = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789!£$%&/()="

def main():
    pass

def gen(len,path = CONST_PATH):
    pas = ""
    for n in range(len):
        z = random.choice(path)
        pas = pas + z
    return pas




def save(text,pas,save_file = "pass.txt"):
    print(f"pass scritta sul file {save_file}")  
    file = open(save_file,'a')
    content = "account "+ text + "   pass " + pas
    file.write(f"\n{content}")



n = input("Password quanto grande ? ")

print("la lunghezza pass DEVE essere un intero")

text = input("per quale account : ")

pas = gen(int(n))

print(f"password generata : {pas}")

save(text,pas)


if __name__ == "__main__":
    main()