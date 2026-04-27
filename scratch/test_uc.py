import undetected_chromedriver._compat as uc
import platform
import subprocess

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
    major_version = version.split('.')[0]
    print(f"Detected Chrome version: {version}, major: {major_version}")
    uc.TARGET_VERSION = major_version
    try:
        uc.install()
        print("uc.install() successful")
    except Exception as e:
        print(f"uc.install() failed: {e}")
else:
    print("Could not detect Chrome version")
