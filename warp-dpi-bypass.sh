#!/bin/bash
set -e

echo "[1/7] stopping and disabling systemd-resolved"
sudo systemctl disable --now systemd-resolved
sudo systemctl mask systemd-resolved

echo "[2/7] activating and initializing warp-svc"
sudo systemctl enable --now warp-svc

echo "[3/7] waiting 3 seconds"
sleep 3

echo "[4/7] establishing a warp connection..."
sudo warp-cli connect
