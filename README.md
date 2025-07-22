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

chmod +x warp-dpi-bypass.sh

chmod +x warp-dpi-unbypass.sh

The script will run to run

./warp-dpi-bypass.sh

For Unbypass

./warp-dpi-unbypass.sh
