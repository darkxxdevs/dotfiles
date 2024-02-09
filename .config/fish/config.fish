##################################################################################
###██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗    ███████╗██╗███████╗██╗  ██╗###
##██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝    ██╔════╝██║██╔════╝██║  ██║###
##██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗   █████╗  ██║███████╗███████║###
##██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║   ██╔══╝  ██║╚════██║██╔══██║###
##╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝██╗██║     ██║███████║██║  ██║###
##╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝####
##################################################################################

if status is-interactive
    # Commands to run in interactive sessions can go here
end

set fish_greeting

#echo "i use arch btw!!! >_<"
uptime

#initializing the starship prompt 
starship init fish | source

#git bare repository control alias 
function dotfiles
  git --git-dir=$HOME/pc_dotfiles/ --work-tree=$HOME $argv
end

#setting up some of my alias 
alias vim="nvim"
alias ls="exa"

 set -q GHCUP_INSTALL_BASE_PREFIX[1]; or set GHCUP_INSTALL_BASE_PREFIX $HOME ; set -gx PATH $HOME/.cabal/bin /home/darkxx/.ghcup/bin $PATH # ghcup-env

