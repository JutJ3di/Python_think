import codecs

key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
rot = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"

diz = dict(zip(key,rot))

def crypt(text):
    new = ""
    for carattere in text:
        if carattere in diz:
            new += diz[carattere]
        else:
            new +=carattere
    return new


def decrypt(text):
    return (codecs.encode(text,"rot_13"))


print("Che vuoi fare ?")
scelta = input("crypt/decrypt")

if scelta == "decrypt":
    text = input("frase da decriptare :  ")
    print(decrypt(text))
elif scelta == "crypt":
    text = input("frase da criptare :  ")
    print(crypt(text))


def main():
    pass

if  __name__ == "__main__":
    main()
