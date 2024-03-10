local wezterm = require("wezterm")

local config = {}

config.font = wezterm.font("Liga SFMono Nerd Font")
config.color_scheme = "Batman"

config.colors = {
	background = "#0a0b0c",
	foreground = "#cccccc",
}

config.window_frame = {
	font = wezterm.font({ family = "Liga SFMono Nerd Font", weight = "Medium" }),
}

config.font_size = 10.6

config.enable_tab_bar = false

config.window_close_confirmation = "NeverPrompt"

return config
