
#  ██████╗ ████████╗██╗██╗     ███████╗
# ██╔═══██╗╚══██╔══╝██║██║     ██╔════╝   config
# ██║   ██║   ██║   ██║██║     █████╗
# ██║▄▄ ██║   ██║   ██║██║     ██╔══╝
# ╚██████╔╝   ██║   ██║███████╗███████╗
# ╚══▀▀═╝    ╚═╝   ╚═╝╚══════╝╚══════╝
##################################################


# IMPORTS

import os
import socket
import platform
import webbrowser
import subprocess
from typing import List 
from libqtile import qtile
from libqtile.command import lazy
from libqtile.dgroups import simple_key_binder
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group,  Key, Match, Screen, ScratchPad, DropDown

# CONTROLERS SETTINGS

mod = "mod4"
myTerm = "alacritty"
myBrowser = "firefox"
myGithubUrl ="https://github.com/darkxxdevs" 


# OPEN GITHUB
def open_github():
    webbrowser.open_new_tab(myGithubUrl)

# get kernel version
def getKernelVersion():
    return platform.release()


# KEYBINDINGS


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
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod], "x", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("sh -c 'mpv --no-video ~/.config/startupSounds/menu-01.mp3 & dmenu_run'"),
        desc="play specific PMV file and launch dmenu"),
    Key([mod], "z", lazy.spawn("reboot"),
        desc="rebooting the system instantly"),
    Key([mod], "h", lazy.layout.grow()),
    Key([mod], "l", lazy.layout.shrink()),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([mod], "space", lazy.group['drxterm'].dropdown_toggle("myTerm")),
    Key([] , "XF86AudioRaiseVolume" , lazy.spawn("amixer set Master 5%+")),
    Key([] , "XF86AudioLowerVolume" , lazy.spawn("amixer set Master 5%-")),
    Key([mod], "b" , lazy.spawn(myBrowser) ),
	Key([mod], "g" , lazy.spawn(f"{myBrowser} {myGithubUrl}"))
]

# calculations for the screen size
screen_width = 1366
screen_height = 768
width = 0.6
height = 0.4
x = (1 - width) / 2
y = (1 - height) / 2

# WORKSPACES

groups = [Group("DEV", layout='monadtall'),
          Group("WEB", layout='monadtall'),
          Group("DEV", layout='monadtall'),
          Group("CODE", layout='monadtall'),
          Group("EXE", layout='monadtall'),
          Group("FIX", layout='monadtall'),
          Group("EWW", layout='monadtall'),
          Group("AI", layout='floating'),

          ScratchPad(
    "drxterm",
    [
        DropDown(
            'myTerm',
            [myTerm],
            height=height,
            width=width,
            x=x,
            y=y,
            on_focus_lost_hide=False,
            opacity=1.0,
            warp_pointer=False,
        ),
    ]
)
]


dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 7,
                "border_focus": "#e1acff",
                "border_normal": "#1D2330"
                }


layouts = [
    layout.MonadWide(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
        font="Ubuntu",
        fontsize=10,
        sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize=10,
        border_width=2,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200
    ),
    layout.Floating(**layout_theme,
                    float_rules=[
                        *layout.Floating.default_float_rules,
                        Match(wm_class='confirmreset'),])

]


colors = [["#0f1014", "#0f1014",],
          ["#0f1014", "#0f1014"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#dddddd", "#dddddd"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="CasKaydiaCove Nerd Font Bold",
    fontsize=12,
    padding=2,
    background=colors[2]
)

icon_ = widget.TextBox(
    text="󰘯 ",
    fontsize=22,
    padding=0,
    foreground="#dddddd",
    background=colors[0],
    mouse_callbacks={
        "Button1": open_github
    }

)

kernel_ = widget.TextBox(
    text="  {}".format(getKernelVersion()),
    foreground="#dbafa4",
    background="#0f1014",
    padding=5,
)

userName_ = widget.TextBox(
    text=" ",
    background=colors[0]
)



extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=4,
            foreground="#debfff",
            background=colors[0]
        ),
        icon_,
        widget.Sep(
            linewidth=0,
            padding=1,
            foreground="#debfff",
            background=colors[0]
        ),
        widget.GroupBox(
            font="CaskaydiaCove Nerd Font Bold",
            fontsize=9,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            foreground="#9a989c",
            background=colors[0],
            padding=5,
            fontsize=14
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[2],
            background=colors[0],
            padding=0,
            scale=0.8
        ),

        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground="#9a989c",
            padding=2,
            fontsize=14
        ),
        widget.WindowName(
            foreground=colors[6],
            background=colors[0],
            padding=0,
            max_chars=16
        ),
        kernel_,
        widget.Sep(
            linewidth=0,
            padding=2,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.Volume(
            foreground=colors[3],
            background=colors[0],
            fmt='󰎈 {}',
            padding=5,
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        
        widget.Memory(
            foreground="#abb2bf",
            background=colors[0],
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e gotop')},
            fmt='󰍛 {}',
            padding=5,
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Arch_checkupdates",
            display_format="   Updates: {updates} ",
            foreground=colors[5],
            colour_have_updates=colors[5],
            colour_no_updates=colors[5],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                myTerm + ' -e sudo pacman -Syu')},
            padding=5,
            background=colors[0],
        ),
        widget.Net(
            interface="wlan0",
            format='  {down} ↓↑ {up}',
            foreground=colors[7],
            background=colors[0],
            padding=5,
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.Battery(
            low_foreground=colors[3],
            format='{char} {percent:2.0%}',
            discharge_char="󱟞",
            low_percentage=0.1,
            charge_char="󰂄",
            hide_threshold=None,
            background=colors[0],
            foreground=colors[4]
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.Clock(
            foreground=colors[6],
            background=colors[0],
            format="  %H:%M ",
        ),

        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.Systray(
            background=colors[0],
            padding=5,
            foreground=colors[3],
        ),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    # Slicing removes unwanted widgets (systray) on Monitors 1,3
    del widgets_screen1[9:10]
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    # Monitor 2 will display all widgets in widgets_list
    return widgets_screen2


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


subprocess.Popen(["nitrogen", "--restore"])
# picom on startup
os.system("picom --config ~/.config/picom/picom.conf &")
# run nm-applet on startup
subprocess.Popen("nm-applet")
