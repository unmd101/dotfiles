#!/bin/sh

. "${XDG_CONFIG_HOME:-$HOME/.config}/x11/xprofile"

xwallpaper --zoom ~/.config/wall.jpg

ssh-agent dwm
