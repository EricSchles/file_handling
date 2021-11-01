import subprocess
from typing import List, Tuple

def save_data(command: List) -> Tuple:
    file_data = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    while file_data.poll() is None:
        continue
    return file_data.communicate()

if __name__ == '__main__':
    #["cat", "file.txt"]
    output, _ = save_data(["python", "python_program.py"])
    output = str(output)
    print(len(output.split("\n")))

