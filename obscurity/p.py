import shutil
import os
while True:
    files = os.listdir("./SSH")
    for file in files:
        shutil.copy(os.path.join("./SSH", file), "./flag");
