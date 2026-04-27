from undetected_chromedriver import Patcher
import os

try:
    path = os.path.join(os.getcwd(), 'chromedriver.exe')
    p = Patcher(executable_path=path, version_main=147)
    print(f"Patcher initialized. exe_name: {p.exe_name}")
    print(f"Executable path: {p.executable_path}")
    print("Calling auto()...")
    p.auto()
    print("Done.")
    if os.path.exists(path):
        print(f"File exists at: {path}")
    else:
        print(f"File does NOT exist at {path}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
