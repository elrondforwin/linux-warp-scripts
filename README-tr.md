# linux-warp-scripts

# NOT: CLOUDFLARE WARP GEREKLİDİR!

# NOT 2: SADECE DPI'YI (Derin Paket İncelemesi) AŞMAK İÇİN KULLANIN

# Kurulum:

Konsolu açın:

Arch Linux (AUR): yay -S cloudflare-warp-bin

Debian, Ubuntu, Red hat: https://pkg.cloudflareclient.com/ Takip edin.

Yükledikten sonra:

Komutları çalıştırın:

sudo systemctl start warp-svc

warp-cli registration new

Sonra:

python warp-dpi-bypass.py

Unbypass için

python warp-dpi-unbypass.sh
