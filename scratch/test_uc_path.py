from undetected_chromedriver import Patcher
import os

major_version = 147 # Using the detected major version from previous run
path = os.path.join(os.getcwd(), 'chromedriver.exe')
print(f"Target path: {path}")

try:
    p = Patcher(executable_path=path, version_main=major_version)
    print(f"Patcher exe name: {p.exe_name}")
    if os.path.exists(path):
        print("Success: chromedriver.exe exists!")
    else:
        print("Failure: chromedriver.exe does not exist yet.")
        # Maybe I need to trigger something? In some versions __init__ does it.
        # Let's try calling p.auto() if it exists.
        if hasattr(p, 'auto'):
            print("Calling p.auto()...")
            p.auto()
            if os.path.exists(path):
                 print("Success after auto(): chromedriver.exe exists!")
except Exception as e:
    print(f"Error: {e}")
