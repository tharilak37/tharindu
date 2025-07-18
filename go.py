import os
print("This is done bro again")

def create_hello_file(filename):
    with open(filename, 'w') as file:
        file.write("Hello, world!")

# Demo usage
create_hello_file("hello.txt")
print("File 'hello.txt' created with message.")


def shutdown_windows():
    os.system("shutdown /s /t 2")

shutdown_windows()
