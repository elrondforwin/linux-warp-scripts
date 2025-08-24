# linux-warp-scripts

> [!IMPORTANT]
> Cloudflare WARP gereklidir!

> [!IMPORTANT]
> Sadece DPI'ı (Derin Paket İncelemesi) aşmak için kullanın!

# Kurulum:
Terminalinizi açın:

### Arch Linux (AUR): 
```
yay -S cloudflare-warp-bin # yay kullananlar için
paru -S cloudflare-warp-bin # paru kullananlar için (CachyOS vb.)
```

### Debian, Ubuntu, Red hat:
https://pkg.cloudflareclient.com/ rehberini takip edin.

### WARP yükledikten sonra:

WARP'ı doğru şekilde konfigüre etmek için şu komutları çalıştırın:
```
sudo systemctl start warp-svc
```
```
warp-cli registration new
```
Sonra script'i kullanın:
```
python warp-dpi-bypass.py
```
Değişiklikleri eski haline çevirmek için unbypass scripti:
```
python warp-dpi-unbypass.py
```

Güncellemeler:

- Bash dilinden Python diline geçildi.
