from undetected_chromedriver import Patcher
import os
import shutil

try:
    major_version = 147
    exe_name = '.exe'
    target = f'chromedriver{exe_name}'
    
    print("Initializing Patcher without explicit path...")
    p = Patcher(version_main=major_version)
    print(f"Default executable path: {p.executable_path}")
    
    print("Calling auto()...")
    p.auto()
    
    if os.path.exists(p.executable_path):
        print(f"File exists at default path. Copying to {target}...")
        shutil.copy(p.executable_path, target)
        if os.path.exists(target):
            print("Success: copied to target!")
    else:
        print("Failure: file not found at default path.")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
