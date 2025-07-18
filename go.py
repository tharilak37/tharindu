import os
import webbrowser
print("This is done bro again")  # Prints a message

def create_hello_file(filename):
    with open(filename, 'w') as file:
        file.write("Hello, world!")

create_hello_file("hello.txt")    # Creates the file
print("File 'hello.txt' created with message.")

def open_vid():
 webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
 print('Video oepned')
open_vid()

#def shutdown_windows():
    #print('shutting down bro')
    #os.system("shutdown /s /t 0")  # Shutdowns Windows after 2 seconds

#shutdown_windows()                # Executes the shutdown
