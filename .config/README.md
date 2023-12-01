# ____.Dotfiles____

## Introduction

Welcome to my Dotfiles repository! This repository holds my configuration files for various Linux utilities and window managers. It includes configurations for zsh, fish, qtile, i3wm, and a collection of wallpapers.

## Installation

To use these dotfiles on your system, you have two options for installation: manual installation and automated installation using a script.

### Manual Installation

Follow these steps to manually install the dotfiles:

1. **Clone the repository:**
    - use git clone :
       ```
       git clone https://github.com/darkxxdevs/dotfiles.git
       cd dotfiles
       ```

2. **Zsh Configuration:**

   - Copy the `.zshrc` file to your home directory:

     ```
     cp  .zshrc ~/
     ```

3. **Fish Configuration:**

   - Copy the `fish` file to your fish configuration directory:

     ```
     cp  .config/fish/ ~/.config/fish/
     ```

4. **Qtile Configuration:**

   - Copy the `qtile/` directory to your Qtile configuration directory:

     ```
     cp -r .config/qtile/ ~/.config/qtile/
     ```

5. **i3wm Configuration:**

   - Copy the `i3/` directory to your i3wm configuration directory:

     ```
     cp -r ./config/i3/  ~/.config/i3/
     ```
6. **kitty Configuration:**
   - Copy the `kitty/` directory to your kitty config directory:

     ```
      cp .config/kitty/  ~/.config/kitty/
     ```

7. **Starship Prompt Config:**
   - Copy the `starship.toml` file to your config directory:

    ```
     cp .config/starship.toml ~/.config/
    ```


8. **Wallpapers:**

   - The `my_walls/` directory contains a collection of wallpapers. Feel free to use and customize them as you like.

### Automated Installation (Not Tested)

Please note that the following installation script has not been tested and may fail. Use it at your own risk.

1. **Clone the repository:**

   ```
   git clone https://github.com/darkxxdevs/dotfiles.git
   cd dotfiles
   ```

2. **Run the installation script:**

   ```
   chmod +x install.sh
   ./install.sh
   ```

## Additional Information

- **Dependencies:** Some configurations might require specific packages or programs to be installed on your system. Please refer to the individual files or directories for any specific dependencies.

- **Customization:** The configurations provided here are tailored to my preferences. However, feel free to modify them to suit your needs and style.

## Feedback and Contributions

If you encounter issues, have suggestions for improvements, or wish to contribute to these dotfiles, please open an issue or submit a pull request on the repository.

## License

This project is licensed under the [MIT License](./LICENSE).

## Acknowledgments

I extend my gratitude to the open-source community and the developers behind the tools and utilities that made these configurations possible.

---

Thank you for exploring my Dotfiles repository! I trust you'll discover something useful or inspiring here. Should you require assistance or have inquiries, don't hesitate to reach out.

Enjoy the customization process!

\- DARKXX