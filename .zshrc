#otfiles control alias
alias dotfiles='git --git-dir=$HOME/dotfiles.git --work-tree=$HOME'


#figlet
figlet -f new "#darkxx"

#alias
alias la="ls -a"
alias vim="nvim"
# prompt settings  

if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Created by newuser for 5.9
source ~/powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

#zsh-autosuggestions 
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
