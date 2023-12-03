#########################################
##  ██████╗ ████████╗██╗██╗     ███████╗##
## ██╔═══██╗╚══██╔══╝██║██║     ██╔════╝##
## ██║   ██║   ██║   ██║██║     █████╗  ##
## ██║▄▄ ██║   ██║   ██║██║     ██╔══╝  ##
###╚██████╔╝   ██║   ██║███████╗███████╗##
####╚══▀▀═╝    ╚═╝   ╚═╝╚══════╝╚══════╝##
##########################################
##--- imports---##
import os
import platform
import subprocess
import webbrowser
from libqtile.lazy import lazy
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown


# setting up the mod key 
mod = "mod4"  

#setting up the default terminal 
terminal = "alacritty"  



#getting the kernel version 
def getKernelVersion():
    return platform.release()


# definiton of brigness control
@hook.subscribe.startup_once
def autostart():
    brightnessctl_cmd = "brightnessctl s 50%"
    subprocess.Popen(brightnessctl_cmd.split())
    subprocess.Popen(["nm-applet"])


# -<< STARTUP PROGRAMS VIA AUTOSTART SCRIPT >>-#

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])

# -<< floating laoyout config >>-#


class FloatingLayout(layout.floating.Floating):
    pass


# picom setup
os.system("picom --config ~/.config/picom/picom.conf &")
#  volume controls


# open github
def open_github():
    webbrowser.open_new_tab("https://github.com/darkxxdevs")


keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod], "x", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("sh -c 'mpv --no-video ~/.config/startupSounds/menu-01.mp3 & dmenu_run'"),
        desc="play specific PMV file and launch dmenu"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    Key([mod], "z", lazy.spawn("reboot"),desc="rebooting the system instantly"),
    Key([mod, "shift"], "s", lazy.spawn(
        "bash /home/darkxx/.screenlayout/monitor.sh")),
    Key([mod, "shift"], "s", lazy.spawn("shutdown")),
    Key([mod], "h", lazy.layout.grow()),
    Key([mod], "l", lazy.layout.shrink()),
    Key([mod], "f", lazy.window.toggle_floating(
        border_focus="#fff"), desc="Toggle floating"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle")),
]


groups = []

group_names = ["1", "2", "3", "4", "5", "6",]
group_labels = ["", "", "", "", "", "",]
group_layouts = ["monadtall", "monadtall", "monadtall",
                 "monadtall", "monadtall", "monadtall",]


for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name), lazy.group[i.name].toscreen()),
        Key([mod], "space", lazy.group["scratchpad"].dropdown_toggle("kitty")),
    ])


layouts = [
    layout.Columns(border_focus_stack=["#e1acff", "#e1acff"], border_width=4),
    layout.Max(),
    layout.Stack(num_stacks=2, border_focus="#ffffff",
                 border_normal="#9e8d9d", border_width=2),
    layout.Bsp(),
    layout.Matrix(),
    layout.MonadTall(border_focus="#e1acff",
                     border_normal="#9e8d9d", border_width=2, margin=7),
    layout.MonadWide(),
    layout.RatioTile(border_focus="#e1acff",
                     border_normal="#9e8d9d", border_width=2),
    layout.Tile(),
    layout.TreeTab(),
    layout.VerticalTile(),
    layout.Zoomy(),
    FloatingLayout(),
]

widget_defaults = dict(
    font="CaskaydiaCove Nerd Font bold",
    fontsize=12,
    padding=1,
)
extension_defaults = widget_defaults.copy()

# -- widget list --
separator_widget = widget.TextBox(
    text="|",
    fontsize=14,
    padding=5,
    foreground="#9a989c",
    background="#0f1014"
)
icon_ = widget.TextBox(
    text=" ",
    fontsize=20,
    padding=0,
    foreground="#dddddd",
    mouse_callbacks={
        "Button1": open_github
    }
)
sep3 = widget.TextBox(
    text="]",
    fontsize=14,
    padding=5,
    foreground="#ffc0cb",
    background="#0f1014"
)

speaker_widget = widget.TextBox(
    text="󰎈",
    foreground="#e06c75",
    fontsize=14,
    padding=5,
)
clock_widget = widget.TextBox(
    text="",
    foreground="#51afef",
    fontsize=12,
    padding=5,
)
win_layout = widget.TextBox(
    text=" ",
    foreground="#6bfff3",
    fontsize=12,
    padding=5,
)
cpu_widget = widget.TextBox(
    text=" ",
    foreground="#abb2bf",
    fontsize=12,
    padding=2,
)
Spacer_ = widget.TextBox(
    text=" ",
)
kernel_ = widget.TextBox(
    text="  {}".format(getKernelVersion()),
    foreground="#dbafa4",
    background="#0f1014",
    padding=5,
)
user = widget.TextBox(
    text="darkxxdevs",
    mouse_callbacks={
        "Button1": open_github
    },
    fontsize=10
)


screens = [
    Screen(
        top=bar.Bar(
            [

                Spacer_,
                icon_,
                user,
                Spacer_,
                widget.GroupBox(
                    the_current_screen_border='#6a0c8a',
                    inactive='#6a0c8a',
                    active="#ddd",
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    highlight_method="line",
                    highlight_color="#0f1014",
                ),
                separator_widget,
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser(
                        "~/.config/qtile/icons")],
                    foreground="#ffff",
                    background="#0f1014",
                    padding=0,
                    scale=0.7
                ),
                separator_widget,
                widget.WindowName(foreground="#9cd3f7",
                                  max_chars=15,

                                  ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # separator_widget,
                kernel_,
                Spacer_,
                speaker_widget,
                widget.Volume(
                    foreground="#e06c75"
                ),
                Spacer_,
                Spacer_,
                cpu_widget,
                widget.Memory(
                    foreground="#abb2bf",
                    measure_mem='M',
                    paddin=0
                ),
                Spacer_,
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_checkupdates",
                    display_format="   Updates: {updates} ",
                    foreground="#ddd",
                    colour_have_updates="#ddd",
                    colour_no_updates="#ddd",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                        terminal + ' -e sudo pacman -Syu')},
                    padding=3,
                    background="#0f1014"

                ),

                widget.Net(interface="wlan0",
                           format="  {down} ↓↑ {up}",
                           padding=2,
                           foreground="#b566ed",
                           background="#0f1014",
                           ),
                Spacer_,
                Spacer_,
                widget.Battery(
                    low_foreground="#ff0000",
                    format='{char} {percent:2.0%}',
                    charge_char='🗲',
                    discharge_char='󰂁',
                    low_percentage=0.1,
                    hide_threshold=None,
                    foreground="#98be65"
                ),
                Spacer_,
                Spacer_,
                clock_widget,
                widget.Clock(format="%H:%M %p",
                             foreground="#51afef"
                             ),
                Spacer_,
                widget.Systray(),
            ],
            20,
            background="#0f1014"
        )
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
# wallaper setting using the ntriogen program
subprocess.Popen(["nitrogen", "--restore"])
