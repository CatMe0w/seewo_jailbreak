import os
from sys import exit

original = bytes.fromhex("E8 16 E9 FF FF")
patched = bytes.fromhex("B0 01 90 90 90")

filename = "bind_zmodule.dll"
backup_filename = filename + ".bak"

sample_path = "C:\\Program Files (x86)\\Seewo\\SeewoService\\SeewoService_1.X.X.XXXX\\SeewoCore\\module\\bind\\"

if not os.path.exists(filename):
    print("File not found!")
    print("\nPlease copy this file:")
    print(f"    {filename}")
    print("from the following path:")
    print(f"    {sample_path}")
    print("to the current directory.")
    exit(1)

with open(filename, "rb") as f:
    data = f.read()

    if data.find(original) == -1:
        print("It looks like the file is already patched :)")
        exit(0)
    else:
        if not os.path.exists(backup_filename):
            with open(backup_filename, "wb") as out:
                out.write(data)
        else:
            print(f"{backup_filename} already exists!")
            print("\nFor safety reasons, we won't overwrite it.")
            print("Please remove it or rename it to something else.")
            exit(1)

        data = data.replace(original, patched)
        with open(filename, "wb") as out:
            out.write(data)

        print("File patched successfully!")
        print(f"And the original file is backed up as {backup_filename}")
        print("\nPlease copy this file:")
        print(f"    {filename}")
        print("to the following path:")
        print(f"    {sample_path}")
        print("and replace the original file.")
        print("\n================================")
        print("You may need to kill SeewoCore.exe and SeewoFreezeUpdateAssist.exe processes first.")
        print("If it doesn't work, even if you have killed the process, please restart to Safe Mode and try again.")
        print("================================")
        print("\nEnjoy your jailbreak!")
