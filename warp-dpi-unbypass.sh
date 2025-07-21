#!/bin/bash
set -e

echo "[1/3] Warp disconnect..."
sudo warp-cli disconnect

echo "[2/3] disabling the warp-svc service"
sudo systemctl disable --now warp-svc

echo "[3/3] re-enabling systemd-resolved..."
sudo systemctl unmask systemd-resolved
sudo systemctl enable --now systemd-resolved
