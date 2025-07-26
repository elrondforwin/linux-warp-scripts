#!/usr/bin/env
# set -e

import subprocess
import time
import shutil
import sys

def run_command(command, require_sudo=False):
    try:
        if require_sudo:
            command.insert(0, 'sudo')
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"ERROR: Command failed: {' '.join(command)}")
        sys.exit(1)
        
# Check if Cloudflare WARP is installed
print("Check if Cloudflare WARP is installed")
if shutil.which("warp-cli") is None:
    print("Cloudflare WARP is not installed. Please install it and try later.")
    sys.exit(1)

# [1/7] stopping and disabling systemd-resolved
print("[1/7] stopping and disabling systemd-resolved")
run_command(["systemctl", "disable", "--now", "systemd-resolved"], require_sudo=True)
run_command(["systemctl", "mask", "systemd-resolved"], require_sudo=True)

# [2/7] activating and initializing warp-svc
print("[2/7] activating and initializing warp-svc")
run_command(["systemctl", "enable", "--now", "warp-svc"], require_sudo=True)

# [3/7] waiting 5 seconds
print("[3/7] waiting 5 seconds")
time.sleep(5)

# [4/7] establishing a warp connection...
print("[4/7] establishing a warp connection...")
run_command(["warp-cli", "connect"], require_sudo=True)
