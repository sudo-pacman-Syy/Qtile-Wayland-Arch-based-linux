#!/bin/bash


mkdir -p ~/.config/qtile
mkdir -p ~/.config/alacritty
mkdir -p ~/.config/fastfetch
mkdir -p ~/Pictures/Screenshots
mkdir -p ~/.config/mako
sudo pacman -S --needed grim slurp swaybg --noconfirm
sudo pacman -S wl-clipboard
sudo pacman -S cliphist

cp -v config/qtile/config.py ~/.config/qtile/
cp -v config/alacritty/alacritty.toml ~/.config/alacritty/ 2>/dev/null || echo "Alacritty config not found, skipping..."
cp -v config/fastfetch/config.jsonc ~/.config/fastfetch/ 2>/dev/null || echo "Fastfetch config not found, skipping..."
cp -v config/mako/config ~/.config/mako/ 2>/dev/null || echo "Mako config not found, skipping..."

echo "Setup complete! Restart Qtile to see changes."
