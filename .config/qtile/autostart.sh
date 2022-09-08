#!/usr/bin/env bash
picom --experimental-backends -b &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
nitrogen --restore &
#feh --bg-fill /home/ankur/Wallpaper/wallpapers-main/landscapes/forrest.png
xfce4-power-manager &
nm-applet &
(conky -c $HOME/.config/qtile/conky/tokyonight.conkyrc) &
#/usr/bin/conky &
xfce4-clipman &
dunst &
pasystray  &
#/usr/lib/xfce4/notifyd/xfce4-notifyd &
