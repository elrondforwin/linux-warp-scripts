# linux-warp-scripts

# NOT: CLOUDFLARE WARP GEREKLİDİR!

# NOT 2: SADECE DPI'YI (Derin Paket İncelemesi) AŞMAK İÇİN KULLANIN

# Kurulum:

Konsolu açın:

Arch Linux: yay -S cloudflare-warp-bin

Debian, Ubuntu, Red hat: https://pkg.cloudflareclient.com/ Takip edin.

Yükledikten sonra:

Komutları çalıştırın:

sudo systemctl start warp-svc

warp-cli registration new

Sonra:

chmod +x warp-dpi-bypass.sh

chmod +x warp-dpi-unbypass.sh

Komut dosyası çalıştırmak için çalışacaktır

./warp-dpi-bypass.sh

Unbypass için

./warp-dpi-unbypass.sh
