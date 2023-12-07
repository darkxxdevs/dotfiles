#!/bin/bash

# Save current padding
current_padding=$(grep -E '^\s+padding:' ~/.config/alacritty/alacritty.yml)

# Set zero padding
sed -i 's/^\(\s\+x:\s\+\)10/\10/' ~/.config/alacritty/alacritty.yml
sed -i 's/^\(\s\+y:\s\+\)10/\10/' ~/.config/alacritty/alacritty.yml

# Open Neovim
nvim

# Hard code padding to 10 after closing Neovim
sed -i 's/^\(\s\+x:\s\+\)0/\110/' ~/.config/alacritty/alacritty.yml
sed -i 's/^\(\s\+y:\s\+\)0/\110/' ~/.config/alacritty/alacritty.yml

