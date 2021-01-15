import os,subprocess


print("Benvenuto nella mia baby shell pythonn\n\n")

while True:

    path = input(">>")

    if path == "exit":
        exit()
    else:
        p = path.split(" ")
        
    pid = os.fork()
    if pid == 0:
        subprocess.run(p)
        os._exit(0)

    os.wait()

        

if __name__ == "__main__":
    pass
