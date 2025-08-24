# linux-warp-scripts

> [!IMPORTANT]
> Cloudflare WARP is required!

> [!IMPORTANT]
> Use only for bypassing DPI (Deep Packet Inspection)

> [!NOTE]
> Aynı rehberin Türkçesi için [buraya](https://github.com/mustafaby11/linux-warp-scripts/blob/main/README-tr.md) göz atabilirsiniz.

# Installation:
Open your preffered terminal:

### Arch Linux (via AUR):
```
yay -S cloudflare-warp-bin # for yay
paru -S cloudflare-warp-bin # for paru
```

### Debian, Ubuntu, Red hat:
Follow this guide
https://pkg.cloudflareclient.com/

## After installing WARP:
Run these commands in order to configure WARP properly:
```
sudo systemctl start warp-svc
```
```
warp-cli registration new
```
Then use the script
```
python warp-dpi-bypass.py
```
If you want to revert, simply run
```
python warp-dpi-unbypass.py
```

### Updates:

- Switched from Bash language to Python language
