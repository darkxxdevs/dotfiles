#! /bin/bash 

exec dunst &

exec mpv --no-video ~/.config/startupSounds/psp_startup_sound.mp3 & 

exec /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &	# Graphical authentication agent

