from undetected_chromedriver import Patcher
import platform
import subprocess
import os

def get_version():
    try:
        process = subprocess.Popen(
            ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
        )
        return process.communicate()[0].decode('UTF-8').strip().split()[-1]
    except:
        return None

version = get_version()
if version:
    major_version = int(version.split('.')[0])
    print(f"Detected Chrome version: {version}, major: {major_version}")
    try:
        # In newer UC, Patcher handles the download
        patcher = Patcher(version_main=major_version)
        print(f"Patcher initialized. Exe name: {patcher.exe_name}")
        # The auto() method downloads and patches
        # By default it might put it in a temp folder or current folder depending on config
        # But let's see where it puts it.
        # uc.install() used to put it in current dir as 'chromedriver' or 'chromedriver.exe'
        
        # In recent UC, you can just use:
        from undetected_chromedriver import Patcher
        p = Patcher(version_main=major_version)
        # This will download it if not present
        print("Done.")
    except Exception as e:
        print(f"Patcher failed: {e}")
        import traceback
        traceback.print_exc()
else:
    print("Could not detect Chrome version")
