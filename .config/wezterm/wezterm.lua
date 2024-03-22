local wezterm = require("wezterm")

local config = {}

config.font = wezterm.font("JetBrains Mono NF semiBold")

-- config.color_scheme = "Batman"
config.color_scheme = "Tango (terminal.sexy)"

config.colors = {
	background = "#0a0b0c",
	foreground = "#cccccc",
}

config.harfbuzz_features = {
	"calt=0",
}
-- config.window_frame = {
-- 	-- font = wezterm.font({ family = "Liga SFMono Nerd Font", weight = "Medium" }),
-- }

config.font_size = 10.6

config.enable_tab_bar = false

config.window_close_confirmation = "NeverPrompt"

config.default_prog = { "/usr/bin/fish", "-l" }

return config
