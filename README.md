# linux-warp-scripts
# NOTE: CLOUDFLARE WARP IS REQUIRED!
# NOTE 2: USE ONLY FOR EXCEEDING DPI (Deep Packet Inspection)

# Installation:
Open the console:

Arch Linux (via AUR): yay -S cloudflare-warp-bin

Debian, Ubuntu, Red hat:
https://pkg.cloudflareclient.com/
Follow

# After installing:
Run commands:

sudo systemctl start warp-svc

warp-cli registration new

Then:

python warp-dpi-bypass.py

For Unbypass

python warp-dpi-unbypass.py

Updates:

Switched from Bash language to Python language
