#!/bin/bash

# Alacritty configuration file path
alacritty_config=~/.config/alacritty/alacritty.yml

# Function to reset padding
reset_padding() {
  sed -i 's/^\(\s\+x:\s\+\)[0-9]\+/\110/' "$alacritty_config"
  sed -i 's/^\(\s\+y:\s\+\)[0-9]\+/\110/' "$alacritty_config"
}

# Save the current padding
current_padding=$(grep -E '^\s+padding:' "$alacritty_config")

# Set padding to 10
sed -i 's/^\(\s\+x:\s\+\)[0-9]\+/\110/' "$alacritty_config"
sed -i 's/^\(\s\+y:\s\+\)[0-9]\+/\110/' "$alacritty_config"

# Trap to reset padding on EXIT signal
trap reset_padding EXIT


