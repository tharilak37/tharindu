import os
import pyjokes

print("This is done bro again")  # Prints a message

def create_hello_file(filename):
    with open(filename, 'w') as file:
        file.write("Hello, world!")

create_hello_file("hello.txt")    # Creates the file
print("File 'hello.txt' created with message.")


print("[+] Telling you a programmer joke:\n")
print(pyjokes.get_joke(language='en', category='programming'))


#def shutdown_windows():
    #print('shutting down bro')
    #os.system("shutdown /s /t 0")  # Shutdowns Windows after 2 seconds

#shutdown_windows()                # Executes the shutdown
