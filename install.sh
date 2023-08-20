#!/bin/bash

# Detect distribution
if [ -f "/etc/os-release" ]; then
    source /etc/os-release
    distro_name=$ID
else
    echo "Unable to detect distribution."
    exit 1
fi

# Install packages based on distribution
if [ "$distro_name" == "debian" ] || [ "$distro_name" == "ubuntu" ]; then
    sudo apt-get update
    sudo apt-get install -y kitty nitrogen picom dmenu zsh fish qtile i3 i3blocks
    echo "please install qtile extras package manually"
elif [ "$distro_name" == "arch" ] || [ "$distro_name" == "manjaro" ]; then
    sudo pacman -Syu --noconfirm kitty nitrogen picom dmenu zsh fish qtile i3 i3blocks qtile-extras
else
    echo "Unsupported distribution: $distro_name"
    exit 1
fi

# Install starship prompt for both zsh and fish
sh -c "$(curl -fsSL https://starship.rs/install.sh)"

# Clone dotfiles repository
github_url="https://github.com/darkxxdevs/dotfiles.git"
git clone "$github_url" ~/dotfiles

cd ~/dotfiles || exit

declare -A config_files=(
    [".config/fish/"]="~/.config/fish/"
    [".config/i3/"]="~/.config/i3/"
    [".config/kitty/"]="~/.config/kitty"
    [".config/qtile/"]="~/.config/qtile"
    ["Screenshots"]="~/Screenshots"
    ["dmenu"]="~/dmenu"
    [".zshrc"]="~/.zshrc"
    ["my_walls"]="~/my_walls"
    [".config/starship.toml"]="~/.config/starship.toml"
    [".bashrc"]="~/.bashrc"
    # Add more entries as needed
)

for source_file in "${!config_files[@]}"; do
    destination_file="${config_files[$source_file]}"

    destination_file="${destination_file/#\~/$HOME}"

    destination_dir=$(dirname "$destination_file")
    if [ ! -d "$destination_dir" ]; then
        mkdir -p "$destination_dir"
    fi

    cp -r "$source_file" "$destination_file"
done

echo "-------[SETUP COMPLETE]-------------"

