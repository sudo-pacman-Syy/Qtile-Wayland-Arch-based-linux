#!/bin/bash


mkdir -p ~/.config/qtile
mkdir -p ~/.config/alacritty
mkdir -p ~/.config/fastfetch
mkdir -p ~/Pictures/Screenshots
sudo pacman -S --needed grim slurp swaybg --noconfirm

cp -v config/qtile/config.py ~/.config/qtile/
cp -v config/alacritty/alacritty.toml ~/.config/alacritty/ 2>/dev/null || echo "Alacritty config not found, skipping..."
cp -v config/fastfetch/config.jsonc ~/.config/fastfetch/ 2>/dev/null || echo "Fastfetch config not found, skipping..."

echo "Setup complete! Restart Qtile to see changes."
