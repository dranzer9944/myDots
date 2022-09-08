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

from colors import onedark_darker
from unicodes import left_half_circle, right_half_circle

# Remove portions of windows group_names
def parse_func(text):
  for string in ["Brave", "Firefox", "Code"]:
        if string in text:
            text = string
        else:
            text = text
  return text


bar = Bar([
        #Sep(
        #    linewidth = 0,
        #    padding = 2,
        #    foreground = onedark_darker["color4"],
        #    background = onedark_darker["color4"]
        #),
        left_half_circle(onedark_darker["colorfore"], onedark_darker["colorback"]),
        Image(
            filename = "~/.config/qtile/icons/archlinux_blue.png",
            scale = "False",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("alacritty")},
            background = onedark_darker["colorfore"],
        ),
        #widget.Sep(
        #    linewidth = 0,
        #    padding = 2,
        #    foreground = onedark_darker["colorback"],
        #    background = onedark_darker["colorback"]
        #),
        right_half_circle(onedark_darker["colorfore"], onedark_darker["colorback"]),
        left_half_circle(onedark_darker["colorback"], onedark_darker["colorback"]),
        GroupBox(
            font = "JetBrains Nerd Font Mono Bold",
            fontsize = 12,
            fmt = '{}',
            borderwidth = 2,
            background = onedark_darker["color12"],
            active = onedark_darker["color6"],
            inactive = onedark_darker["color5"],
            rounded = False,
            #Block_highlight_text_color = onedark_darker["color3"],
            highlight_method = 'line',
            highlight_color = onedark_darker["colorback"],  #  line block colour
            this_current_screen_border = onedark_darker["color4"],
            this_screen_border = onedark_darker["color7"],
            urgent_alert_method = 'line',
            urgent_border = onedark_darker["color10"],
            urgent_text = onedark_darker["color14"],
            disable_drag = True,
        ),
        right_half_circle(onedark_darker["colorback"], onedark_darker["colorback"]),
        Sep(
            linewidth = 0,
            padding = 6,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["colorback"],
        ),
        left_half_circle(onedark_darker["color14"], onedark_darker["colorback"]),

        CurrentLayoutIcon(
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color14"],
            padding = 0,
            scale = 0.7
        ),
        CurrentLayout(
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color14"],
            padding = 5,
        ),
        right_half_circle(onedark_darker["color14"], onedark_darker["color9"]),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            background = onedark_darker["color9"],
            foreground = onedark_darker["color4"],
            padding = 2
        ),
        WindowCount(
            format = ' {num} ',
            background = onedark_darker["color9"],
            foreground = onedark_darker["color4"],
            show_zero = True,
        ),
        right_half_circle(onedark_darker["color9"], onedark_darker["color1"]),
        Sep(
            linewidth = 0,
            padding = 6,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["colorback"],
        ),
        left_half_circle(onedark_darker["color16"], onedark_darker["colorback"]),
        WindowName(
            foreground = onedark_darker["color1"],
            background = onedark_darker["color16"],
            padding = 5,
            format = '[ {name} ]',
            empty_group_string = '[ ]',
            parse_text = parse_func,
        ),
        right_half_circle(onedark_darker["color16"], onedark_darker["colorback"]),
        #widget.Spacer(),
        Sep(
            linewidth = 0,
            padding = 6,
            foreground = onedark_darker["color1"],
            background = onedark_darker["color1"],
        ),
        left_half_circle(onedark_darker["color2"], onedark_darker["color1"]),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color2"],
        ),
        Net(
            interface = "wlp44s0",
            format = '{down} {up}',
            prefix = 'M',
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color2"],
            padding = 5,
        ),
        right_half_circle(onedark_darker["color2"], onedark_darker["colorback"]),
        Sep(
            linewidth = 0,
            padding = 6,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["colorback"],
        ),
        left_half_circle(onedark_darker["color3"], onedark_darker["colorback"]),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color3"]
        ),
        CPU(
            background = onedark_darker["color3"],
            foreground = onedark_darker["colorback"],
            fmt = 'Cpu: {}',
            #format = '{freq_current}GHz {load_percent}%',
            format = '[ {load_percent} ]%',
            padding = 5,
        ),
        right_half_circle(onedark_darker["color3"], onedark_darker["colorback"]),
        Sep(
            linewidth = 0,
            padding = 6,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["colorback"],
        ),
        left_half_circle(onedark_darker["color4"], onedark_darker["colorback"]),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color4"]
        ),
        ThermalSensor(
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color4"],
            threshold = 90,
            fmt = 'Temp: {}',
            format='[ {temp:.0f}{unit} ]',
            padding = 5,
        ),
        right_half_circle(onedark_darker["color4"], onedark_darker["colorback"]),
        Sep(
            linewidth = 0,
            padding = 6,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["colorback"],
        ),
        left_half_circle(onedark_darker["color5"], onedark_darker["colorback"]),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color5"]
        ),
        Memory(
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color5"],
            #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            fmt = 'Mem: {}',
            #format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            format = '[ {MemUsed:.0f} ]{mm}',
            padding = 5,
        ),
        right_half_circle(onedark_darker["color5"], onedark_darker["colorback"]),
        Sep(
            linewidth = 0,
            padding = 6,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["colorback"],
        ),
        left_half_circle(onedark_darker["color6"], onedark_darker["colorback"]),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color6"]
        ),
        Battery(
            padding = 5,
            background = onedark_darker["color6"],
            foreground = onedark_darker["colorback"],
            charge_char = 'AC',
            discharge_char = '',
            empty_char = 'ﮣ',
            full_char = 'ﭹ',
            fmt = 'Bat: {}',
            format = '{char}[ {percent:2.0%} ]', #{hour:d}:{min:02d} {watt:.2f} W'
            #low_background = none,
            low_forground = '#ff0000',
            update_interval = 60,
        ),
        #battery,
        right_half_circle(onedark_darker["color6"], onedark_darker["colorback"]),
        Sep(
            linewidth = 0,
            padding = 6,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["colorback"],
        ),
        left_half_circle(onedark_darker["color7"], onedark_darker["colorback"]),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color7"]
        ),
        PulseVolume(
            background = onedark_darker["color7"],
            foreground = onedark_darker["colorback"],
            fmt = 'Vol: [ {} ]',
            device = 'default',
            channel = 'Master',
            limit_max_volume = True,
            padding = 5,
            update_interval = 0.1,
            mute_command = 'pactl set-sink-mute @DEFAULT_SINK@ toggle',
            volume_up_command = 'pactl set-sink-volume @DEFAULT_SINK@ +5%',
            volume_down_command = 'pactl set-sink-volume @DEFAULT_SINK@ -5%',
        ),
        #volume,
        #widget.Volume(
        #    foreground = onedark_darker[8],
        #    background = onedark_darker[0],
        #    fmt = 'Vol: {}',
        #    padding = 5,
        #    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e alsamixer')}
        #),
        right_half_circle(onedark_darker["color7"], onedark_darker["colorback"]),
        Sep(
            linewidth = 0,
            padding = 6,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["colorback"],
        ),
        left_half_circle(onedark_darker["color10"], onedark_darker["colorback"]),
        TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color10"]
        ),
        Clock(
            foreground = onedark_darker["colorback"],
            background = onedark_darker["color10"],
            format = "%a %d, %b [ %I:%M ]%P",
            padding = 5,
        ),
        right_half_circle(onedark_darker["color10"], onedark_darker["colorback"]),
        Sep(
            linewidth = 0,
            padding = 6,
            foreground = onedark_darker["colorback"],
            background = onedark_darker["colorback"],
        ),
        left_half_circle(onedark_darker["color15"], onedark_darker["colorback"]),
        Systray(
            background = onedark_darker["color15"],
            padding = 2
        ),
        right_half_circle(onedark_darker["color15"], onedark_darker["colorback"]),

        #widget.TextBox(
        #    text = '',
        #    font = "Mononoki Regular Bold",
        #    fontsize = 18,
        #    padding = 0,
        #    background = onedark_darker[0],
        #    foreground = onedark_darker[9],
        #),
    ], size=25)

