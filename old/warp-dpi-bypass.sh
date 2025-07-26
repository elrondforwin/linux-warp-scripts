#!/bin/bash
set -e

echo "Check if Cloudflare WARP is installed"
if ! command -v warp-cli &> /dev/null; then
    echo "Cloudflare WARP is not installed. Please install it and try later."
    exit 1
fi

echo "[1/7] stopping and disabling systemd-resolved"
sudo systemctl disable --now systemd-resolved
sudo systemctl mask systemd-resolved

echo "[2/7] activating and initializing warp-svc"
sudo systemctl enable --now warp-svc

echo "[3/7] waiting 5 seconds"
sleep 5

echo "[4/7] establishing a warp connection..."
sudo warp-cli connect
