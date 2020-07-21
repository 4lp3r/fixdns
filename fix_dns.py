# AUTHOR == 4LP3R
__author__ = '4LP3R'

import os,subprocess,time,sys
from araclar import error,success,status
def main():
    status(f"Code by {__author__}")
    status("STARTED!")
    os.system("touch /etc/resolv.conf")
    os.system("rm /etc/resolv.conf")
    success("removed resolv.conf")
    time.sleep(0.6)
    os.chdir("/etc")
    cmd = str(subprocess.check_output("pwd")).lstrip("b'").rstrip("\\n'")
    success(f"changed directory from {cmd} to /etc/")
    time.sleep(0.7)
    file = open("resolv.conf", "w", encoding="utf-8")
    file.write("#nameserver 127.0.0.1\nnameserver 1.1.1.1\nnameserver 1.0.0.1")
    file.close()
    success("reloaded DNS!")
    time.sleep(0.6)
    os.system("service network-manager restart")
    success("Network Manager service restarted ! Please try connect internet...")
    time.sleep(0.6)
    status("System will restarting please confirm")
    cvp = input("Confirm ? (Y/n):")
    if (str(cvp).startswith("Y") or str(cvp).startswith("y")):
        success("You are confirmed !")
        status("System is restarting...")
        time.sleep(1)
        os.system("reboot")
    else:
        error("You are not confirmed !")
        sys.exit()
if os.getuid() != 0:
    error("Please run this script as root...")
else:
    main()
