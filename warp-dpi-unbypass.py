#!/usr/bin/env
# set -e

import subprocess
import sys

def run_command(command, require_sudo=False):
    try:
        if require_sudo:
            command.insert(0, 'sudo')
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"ERROR: Command failed: {' '.join(command)}")
        sys.exit(1)

# [1/3] Warp disconnect...
print("[1/3] Warp disconnect...")
run_command(["warp-cli", "disconnect"], require_sudo=True)

# [2/3] disabling the warp-svc service
print("[2/3] disabling the warp-svc service")
run_command(["systemctl", "disable", "--now", "warp-svc"], require_sudo=True)

# [3/3] re-enabling systemd-resolved...
print("[3/3] re-enabling systemd-resolved...")
run_command(["systemctl", "unmask", "systemd-resolved"], require_sudo=True)
run_command(["systemctl", "enable", "--now", "systemd-resolved"], require_sudo=True)
