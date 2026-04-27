from undetected_chromedriver import Patcher
import os

try:
    p = Patcher(version_main=147)
    print(f"Patcher initialized. exe_name: {p.exe_name}")
    print("Calling auto()...")
    p.auto()
    print("Done.")
    if os.path.exists(p.executable_path):
        print(f"File exists at: {p.executable_path}")
    else:
        print("File does NOT exist.")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
