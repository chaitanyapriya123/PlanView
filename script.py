import subprocess

list_files=subprocess.run(["ls", "-lart"], capture_output=True, shell=True)
print(list_files.stdout)
