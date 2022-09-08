import os
from libqtile import qtile
from libqtile.bar import Bar
from libqtile.widget.sep import Sep
from libqtile.widget.image import Image
from libqtile.widget.textbox import TextBox
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget import ThermalSensor
from libqtile.widget.pulse_volume import PulseVolume
from libqtile.widget.battery import Battery
from libqtile.widget import CurrentLayoutIcon
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName

from colors import dracula


# Remove portions of windows group_names
def parse_func(text):
  for string in ["Brave", "Firefox", "Code"]:
        if string in text:
            text = string
        else:
            text = text
  return text



bar = Bar([
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = dracula["color4"],
            background = dracula["color4"]
        ),
        Image(
            filename = "~/.config/qtile/icons/python.png",
            scale = "False",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("alacritty")},
            #background = dracula["color4"],
        ),
        #Sep(
        #    linewidth = 0,
        #    padding = 2,
        #    foreground = dracula["colorback"],
        #    background = dracula["colorback"]
        #),
        TextBox(
            text = "",
            fontsize = 20,
            padding = 2,
            foreground = dracula["color4"],
            background = dracula["colorback"],
        ),
        GroupBox(
            font = "JetBrains Nerd Font Mono Bold",
            fontsize = 10,
            padding = 4,
            borderwidth = 2,
            background = dracula["colorback"],
            active = dracula["color6"],
            inactive = dracula["color5"],
            rounded = False,
            ##Block_highlight_text_color = dracula["color3"],
            highlight_method = 'line',
            highlight_color = dracula["colorback"],  #  line block colour
            this_current_screen_border = dracula["color4"],
            this_screen_border = dracula["color8"],
            urgent_alert_method = 'text',
            #urgent_border = dracula["color10"],
            urgent_text = dracula["color2"],
            disable_drag = True,
        ),
         TextBox(
            text = "",
            padding = 2,
            fontsize = 20,
            foreground = dracula["color4"],
            background = dracula["colorback"],
        ),
        CurrentLayoutIcon(
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = dracula["color14"],
            background = dracula["colorback"],
            padding = 0,
            scale = 0.7
        ),
        CurrentLayout(
            foreground = dracula["color14"],
            background = dracula["colorback"],
            padding = 5,
        ),
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = dracula["color9"],
            background = dracula["colorback"]
        ),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            background = dracula["colorback"],
            foreground = dracula["color4"],
            padding = 2
        ),
        WindowCount(
            format = ' {num} ',
            background = dracula["colorback"],
            foreground = dracula["color4"],
            show_zero = True,
        ),
        Sep(
            linewidth = 2,
            padding = 4,
            foreground = dracula["color9"],
            background = dracula["colorback"]
        ),
        TextBox(
            text = "",
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = dracula["color2"],
            background = dracula["colorback"]
        ),
        WindowName(
            foreground = dracula["colorfore"],
            background = dracula["colorback"],
            padding = 5,
            format = '{name}',
            empty_group_string = '[ ]',
            parse_text = parse_func,
        ),
        #widget.Spacer(),
        #Sep(
        #    linewidth = 0,
        #    padding = 6,
        #    foreground = dracula["color1"],
        #    background = dracula["color1"],
        #),
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = dracula["color9"],
            background = dracula["color9"]
        ),
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = dracula["color1"],
            background = dracula["color2"],
        ),
        Net(
            interface = "wlp44s0",
            format = '{down} {up}',
            prefix = 'M',
            foreground = dracula["color2"],
            background = dracula["colorback"],
            padding = 5,
        ),
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = dracula["color9"],
            background = dracula["color9"]
        ),
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = dracula["color1"],
            background = dracula["color3"]
        ),
        CPU(
            background = dracula["colorback"],
            foreground = dracula["color3"],
            fmt = '{}',
            #format = '{freq_current}GHz {load_percent}%',
            format = '[ {load_percent} ]%',
            padding = 5,
        ),
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = dracula["color9"],
            background = dracula["color9"]
        ),
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = dracula["color1"],
            background = dracula["color4"]
        ),
        ThermalSensor(
            foreground = dracula["color4"],
            background = dracula["colorback"],
            threshold = 90,
            fmt = '{}',
            format='[ {temp:.0f}{unit} ]',
            padding = 5,
        ),
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = dracula["color9"],
            background = dracula["color9"]
        ),
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = dracula["color1"],
            background = dracula["color5"]
        ),
        Memory(
            foreground = dracula["color5"],
            background = dracula["colorback"],
            #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            fmt = '{}',
            #format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            format = '[ {MemUsed:.0f} ]{mm}',
            padding = 5,
        ),
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = dracula["color9"],
            background = dracula["color9"]
        ),
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = dracula["color1"],
            background = dracula["color6"]
        ),
        Battery(
            padding = 5,
            background = dracula["colorback"],
            foreground = dracula["color6"],
            charge_char = 'AC',
            discharge_char = '',
            empty_char = 'ﮣ',
            full_char = 'ﭹ',
            fmt = '{}',
            format = '{char}[ {percent:2.0%} ]', #{hour:d}:{min:02d} {watt:.2f} W'
            #low_background = none,
            low_forground = '#ff0000',
            update_interval = 30,
        ),
        #battery,

        Sep(
            linewidth = 2,
            padding = 2,
            foreground = dracula["color9"],
            background = dracula["color9"]
        ),
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = dracula["color1"],
            background = dracula["color7"]
        ),
        PulseVolume(
            background = dracula["colorback"],
            foreground = dracula["color7"],
            fmt = '[ {} ]',
            device = 'default',
            channel = 'Master',
            limit_max_volume = True,
            padding = 5,
            mute_command = 'pactl set-sink-mute @DEFAULT_SINK@ toggle',
            volume_up_command = 'pactl set-sink-volume @DEFAULT_SINK@ +5%',
            volume_down_command = 'pactl set-sink-volume @DEFAULT_SINK@ -5%',
            update_interval = 0.2
        ),
        #volume,
        #widget.Volume(
        #    foreground = dracula[8],
        #    background = dracula[0],
        #    fmt = 'Vol: {}',
        #    padding = 5,
        #    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e alsamixer')}
        #),
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = dracula["color9"],
            background = dracula["color9"]
        ),
        TextBox(
            text = '  ',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = dracula["color1"],
            background = dracula["color8"]
        ),
        Clock(
            foreground = dracula["color8"],
            background = dracula["colorback"],
            format = "%a %d, %b [ %I:%M ]",
            padding = 5,
        ),
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = dracula["color9"],
            background = dracula["color9"]
        ),
        Systray(
            background = dracula["colorback"],
            padding = 2
        ),
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = dracula["colorback"],
            background = dracula["colorback"]
        ),
        Sep(
            linewidth = 2,
            padding = 2,
            foreground = dracula["color4"],
            background = dracula["color4"]
        ),

    ], size=25, margin=[5, 5, 0, 5],
    #border_width=[5, 0, 5, 0], border_color=dracula["colorback"]
)

