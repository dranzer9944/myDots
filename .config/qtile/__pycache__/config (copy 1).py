# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.command import lazy
from libqtile.config import Click, ScratchPad, DropDown, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from imp import create_dynamic
#from libqtile.widget.battery import Battery, BatteryState
#from libqtile.widget.volume import Volume
# For theme
from colors import tokyonight


mod = "mod4"
mod1 = "alt"
mod2 = "control"
myTerm = "kitty"
home = os.path.expanduser('~')

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


# Remove portions of windows group_names
def parse_func(text):
  for string in ["Brave", "Firefox", "Code"]:
        if string in text:
            text = string
        else:
            text = text
  return text

# Resize Floating Window
@lazy.window.function
def resize_floating_window(window, width: int = 0, height: int = 0):
    if window.floating == True or window.qtile.current_layout.name == 'floating':
        window.cmd_set_size_floating(window.width + width, window.height + height)


# Swap with Master
def cmd_swap_main(self):
    if self.align == self._left:
        self.cmd_swap_left()
    elif self.align == self._right:
        self.cmd_swap_right()


## Cycle through floating
@lazy.window.function
def float_to_front(window):
    if window.floating:
        window.cmd_bring_to_front()
    else:
        window.cmd_bring_to_front()
        window.cmd_disable_floating()


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
####  Resize Floating Window   ##########################################
    Key(["mod1", "control"], "h", resize_floating_window(width=10), desc='increase width by 10'),
    Key(["mod1", "control"], "l", resize_floating_window(width=-10), desc='decrease width by 10'),
    Key(["mod1", "control"], "j", resize_floating_window(height=10), desc='increase height by 10'),
    Key(["mod1", "control"], "k", resize_floating_window(height=-10), desc='decrease height by 10'),

### Gaps  ######################################################


####  SWITCH WINDOWS   #################################################
    ## By-directional window focus
    Key([mod], "j",
            lazy.layout.down(),
            desc="Move focus down"
            ),
    Key([mod], "k",
            lazy.layout.up(), desc="Move focus up"),
    Key([mod], "h",
            lazy.layout.left(), desc="Move focus left"),
    Key([mod], "l",
            lazy.layout.right(), desc="Move focus right"),

    ## Default client focus
    Key(["mod1"], "j",
                lazy.group.next_window(),
                float_to_front(),
                desc="move focus to next window"
                ),

    Key(["mod1"], "k", lazy.group.prev_window(), desc="move focus to previous window"),

####  SHUFFLE WINDOWS   ##################################################
    Key([mod], "BackSpace", lazy.layout.swap_main(), desc="Swap Master"),


    Key([mod, "shift"], "h",
                lazy.layout.shuffle_left(),
                desc="Move window to the left"),

    Key([mod, "shift"], "l",
                lazy.layout.shuffle_right(),
                desc="Move window to the right"),

    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),  ## Move window down in stack
        desc="Move window down"),

    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),  ## Move window Up in stack
        desc="Move window up"),

####  RESIZE UP, DOWN, LEFT, RIGHT   #########################################
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

#### Stack controls    ################################################
    Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'),
    Key([mod], "space",
             lazy.layout.next(),
             desc='Move window focus to other Window'),
    Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'),

#### ADDED FEATURES
    Key([mod], "Tab",
            lazy.next_layout(),
            desc="Toggle between layouts"
            ),

    Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),

Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),

    Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),

     Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),

# NECESSARY KEYS
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "p", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "d", lazy.spawn("dmenu_run -i -nb '#282a36' -nf '#bd93f9' -sb '#bd93f9' -sf '#282a36' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key([mod], "r", lazy.spawn('rofi -show run')),

# SUPER + FUNCTION KEYS
    Key([mod], "F1", lazy.spawn('pavucontrol')),
    Key([mod], "F2", lazy.spawn('blueman-manager')),
    Key([mod], "F3", lazy.spawn('xfce4-power-manager-settings')),
    Key([mod], "F4", lazy.spawn('font-manager')),

# ALT + ....KEYS (Apps)
    Key(["mod1"], "f", lazy.spawn('firefox')),
    Key(["mod1"], "e", lazy.spawn('kitty -e nvim')),
    Key(["mod1"], "t", lazy.spawn('thunar')),
    Key(["mod1"], "r", lazy.spawn('kitty -e ranger')),
    Key(["mod1"], "p", lazy.spawn('pamac-manager')),
    Key(["mod1"], "n", lazy.spawn('nitrogen')),
    Key(["mod1"], "b", lazy.spawn('brave')),
    Key(["mod1"], "c", lazy.spawn('code')),
    Key(["mod1"], "h", lazy.spawn('haruna')),
    Key(["mod1"], "l", lazy.spawn('lxappearance')),
    Key(["mod1"], "x", lazy.spawn('xfce4-terminal')),
    Key(["mod1"], "v", lazy.spawn('vlc')),
    Key(["mod1"], "a", lazy.spawn('alacritty')),

# CONTROL + keys
    Key(["mod2"], "r", lazy.spawn('rofi-theme-selector')),
    Key([mod], "p", lazy.spawn('xfce4-screenshooter'), desc="for taking screenshot"),

# SYSTEM KEYS
## INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10")),
## INCREASE/DECREASE/MUTE VOLUME
    ### Alsa
    #Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    #Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    #Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    ### PULSEAudio
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),

    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),


    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

]


groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

group_labels = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 0 ",]
#group_labels = [" ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",]
#group_labels = ["dev", "www", "sys", "doc", "vim", "chat", "mus", "vid", "gfx", "vbox",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        # Add key command for ScratchPad DropDown
        #Key([mod], "space", lazy.group["scratchpad"].dropdown_toggle("term")),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

# Append ScratchPad to group list
groups.append(
    ScratchPad("scratchpad", [
                   # define a drop down terminal.ScratchPad
                   DropDown("term", myTerm, opacity=0.8, height=0.5, width=0.80),
                   DropDown("mixer", "pavucontrol", width=0.4, x=0.3, y=0.1),
                   #DropDown("cal", "alacritty -e cal", height=0.1, width=0.2),
               ]),
)

## ScratchPad KeyBindings
keys.extend([
        # DropDown Term
        Key([mod], "s", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([mod], "v", lazy.group["scratchpad"].dropdown_toggle("mixer")),
        #Key([mod], "", lazy.group["scratchpad"].dropdown_toggle("cal")),
])

layout_theme = {
    "margin": 15,
    "border_width": 2,
    "border_focus": tokyonight["color4"],
    "border_normal": tokyonight["colorback"],
}


layouts = [
    layout.MonadTall( **layout_theme),
    #layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme),
    #layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    #layout.Max(**layout_theme),
    #layout.Stack(num_stacks=2),
    #layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "UbunutuMono Nerd Font",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = tokyonight["colorback"],
         active_bg = "#c678dd",
         active_fg = "#000000",
         inactive_bg = "#a9a1e1",
         inactive_fg = "#1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]


#prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


widget_defaults = dict(
    font="UbunutuMono Nerd Font Bold",
    fontsize = 11,
    padding = 2,
    background= tokyonight["colorback"],
)
extension_defaults = widget_defaults.copy()

### WIDGET REPLACEMENTS ###
# Battery Icon & % | Replaces widget.Battery
#class MyBattery(Battery):
  #def build_string(self, status):
    #symbols = ""
    #index = int(status.percent * 10)
    #index = max(index, 0) # 0 or higher
    #index = min(index, 9) # 9 or lower start at 0
    #char = symbols[index]
    #if status.state == BatteryState.CHARGING:
      #char += ""
      #if status.state == BatteryState.UNKNOWN:
        #char = ""
    #return self.format.format(char=char, percent=status.percent)

#battery = MyBattery(
    #format = 'Bat: {char} [ {percent:2.0%} ]',
    #foreground = colors[7],
    #notify_below = 10,
    #fontsize = 12,
#)

# Audio Volume/still needs work | replacing widget.Volume
#class MyVolume(Volume):
#  def create_amixer_command(self, *args):
#    return super().create_amixer_command("-M")
#  def _update_drawer(self):
#    if self.volume <= 0:
#      self.volume = '0%'
#      self.text = '🔇' + str(self.volume)
#    elif self.volume < 30:
#      self.text = '🔈' + str(self.volume) + '%'
#    elif self.volume < 80:
#      self.text = '🔉' + str(self.volume) + '%'
#    else: # self.volume >=80:
#      self.text = '🔊' + str(self.volume) + '%'
#
#    def restore(self):
#      self.timer_setup()
#
#volume = MyVolume(
#    foreground = colors[8],
#    fmt = 'Vol: {}',
#    fontsize = 12,
#)



def init_widgets_list():
    #prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = tokyonight["color4"],
            background = tokyonight["color4"]
        ),
        widget.Image(
            filename = "~/.config/qtile/icons/archlinux_blue.png",
            scale = "False",
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
            background = tokyonight["color4"]
        ),
        #widget.Sep(
        #    linewidth = 0,
        #    padding = 2,
        #    foreground = tokyonight["colorback"],
        #    background = tokyonight["colorback"]
        #),
        widget.TextBox(
            text = '',
            font = "Mononoki Nerd Font",
            fontsize = 24,
            padding = 0,
            background = tokyonight["colorback"],
            foreground = tokyonight["color4"]
        ),
        widget.GroupBox(
            font = "JetBrains Nerd Font Mono Bold",
            fontsize = 12,
            fmt = '{}',
            borderwidth = 2,
            background = tokyonight["colorback"],
            active = tokyonight["color6"],
            inactive = tokyonight["color5"],
            rounded = False,
            #Block_highlight_text_color = tokyonight["color3"],
            highlight_method = 'line',
            highlight_color = tokyonight["colorback"],  #  line block colour
            this_current_screen_border = tokyonight["color4"],
            this_screen_border = tokyonight["color7"],
            urgent_alert_method = 'line',
            urgent_border = tokyonight["color10"],
            urgent_text = tokyonight["color14"],
            disable_drag = True
        ),
        widget.TextBox(
            text = '',
            font = "Mononoki Nerd Font",
            background = tokyonight["color14"],
            foreground = tokyonight["colorback"],
            padding = 0,
            fontsize = 24
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = tokyonight["colorback"],
            background = tokyonight["color14"],
            padding = 0,
            scale = 0.7
        ),
        widget.CurrentLayout(
            foreground = tokyonight["colorback"],
            background = tokyonight["color14"],
            padding = 5
        ),
        widget.TextBox(
            text = '',
            font = "Mononoki Nerd Font",
            background = tokyonight["color9"],
            foreground = tokyonight["color14"],
            padding = 0,
            fontsize = 24
        ),
        widget.TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            background = tokyonight["color9"],
            foreground = tokyonight["color4"],
            padding = 2
        ),
        widget.WindowCount(
            format = ' {num} ',
            background = tokyonight["color9"],
            foreground = tokyonight["color4"],
            show_zero = True,
        ),
         widget.TextBox(
            text = '',
            font = "Mononoki Nerd Font",
            fontsize = 24,
            background = tokyonight["colorback"],
            foreground = tokyonight["color9"],
            padding = 0
        ),
        widget.WindowName(
            foreground = tokyonight["color5"],
            background = tokyonight["colorback"],
            padding = 5,
            format = '[ {name} ]',
            empty_group_string = '[ ]',
            parse_text = parse_func,
        ),
        #widget.Spacer(),
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = tokyonight["colorback"],
            background = tokyonight["colorback"]
        ),
        widget.TextBox(
            text = '',
            font = "Mononoki Nerd Font",
            background = tokyonight["colorback"],
            foreground = tokyonight["color2"],
            padding = 0,
            fontsize = 20
        ),
        widget.TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = tokyonight["colorback"],
            background = tokyonight["color2"],
        ),
        widget.Net(
            interface = "wlp44s0",
            format = '{down} {up}',
            prefix = 'M',
            foreground = tokyonight["colorback"],
            background = tokyonight["color2"],
            padding = 5
        ),
        widget.TextBox(
            text = '',
            font = "Mononoki Nerd Font",
            background = tokyonight["color2"],
            foreground = tokyonight["color3"],
            padding = 0,
            fontsize = 20
        ),
        widget.TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = tokyonight["colorback"],
            background = tokyonight["color3"]
        ),
        widget.CPU(
            background = tokyonight["color3"],
            foreground = tokyonight["colorback"],
            fmt = 'Cpu: {}',
            #format = '{freq_current}GHz {load_percent}%',
            format = '[ {load_percent} ]%',
            padding = 5
        ),
        widget.TextBox(
            text = '',
            font = "Mononoki Nerd Font",
            background = tokyonight["color3"],
            foreground = tokyonight["color4"],
            padding = 0,
            fontsize = 20
        ),
        widget.TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = tokyonight["colorback"],
            background = tokyonight["color4"]
        ),
        widget.ThermalSensor(
            foreground = tokyonight["colorback"],
            background = tokyonight["color4"],
            threshold = 90,
            fmt = 'Temp: {}',
            format='[ {temp:.0f}{unit} ]',
            padding = 5
        ),
        widget.TextBox(
            text = '',
            font = "Mononoki Nerd Font",
            background = tokyonight["color4"],
            foreground = tokyonight["color5"],
            padding = 0,
            fontsize = 20
        ),
        widget.TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = tokyonight["colorback"],
            background = tokyonight["color5"]
        ),
        widget.Memory(
            foreground = tokyonight["colorback"],
            background = tokyonight["color5"],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            fmt = 'Mem: {}',
            #format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            format = '[ {MemUsed:.0f} ]{mm}',
            padding = 5
        ),
        widget.TextBox(
            text='',
            font = "Mononoki Nerd Font Bold",
            background = tokyonight["color5"],
            foreground = tokyonight["color6"],
            padding = 0,
            fontsize = 20
        ),
        widget.TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = tokyonight["colorback"],
            background = tokyonight["color6"]
        ),
        widget.Battery(
            padding = 5,
            background = tokyonight["color6"],
            foreground = tokyonight["colorback"],
            charge_char = 'AC',
            discharge_char = '',
            empty_char = 'ﮣ',
            full_char = 'ﭹ',
            fmt = 'Bat: {}',
            format = '{char}[ {percent:2.0%} ]', #{hour:d}:{min:02d} {watt:.2f} W'
            #low_background = none,
            low_forground = '#ff0000',
            update_interval = 60
        ),
        #battery,

        widget.TextBox(
            text = '',
            font = "Mononoki Nerd Font",
            background = tokyonight["color6"],
            foreground = tokyonight["color7"],
            padding = 0,
            fontsize = 20
        ),
        widget.TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = tokyonight["colorback"],
            background = tokyonight["color7"]
        ),
        widget.PulseVolume(
            background = tokyonight["color7"],
            foreground = tokyonight["colorback"],
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
        #    foreground = tokyonight[8],
        #    background = tokyonight[0],
        #    fmt = 'Vol: {}',
        #    padding = 5,
        #    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e alsamixer')}
        #),
        widget.TextBox(
            text = '',
            font = "Mononoki Nerd Font",
            background = tokyonight["color7"],
            foreground = tokyonight["color10"],
            padding = 0,
            fontsize = 20
        ),
        widget.TextBox(
            text = '',
            font = "Font Awesome 6 Free Solid",
            fontsize = 15,
            padding = 2,
            foreground = tokyonight["colorback"],
            background = tokyonight["color10"]
        ),
        widget.Clock(
            foreground = tokyonight["colorback"],
            background = tokyonight["color10"],
            format = "%a %d, %b [ %I:%M ]%P",
            padding = 5
        ),
        widget.TextBox(
            text = '',
            font = "Mononoki Nerd Font",
            background = tokyonight["color10"],
            foreground = tokyonight["colorback"],
            padding = 0,
            fontsize = 20
        ),
         widget.Systray(
            background = tokyonight["colorback"],
            padding = 2
        ),

        #widget.TextBox(
        #    text = '',
        #    font = "Mononoki Nerd Font Bold",
        #    fontsize = 18,
        #    padding = 0,
        #    background = tokyonight[0],
        #    foreground = tokyonight[9],
        #),
    ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=24)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=24))]
screens = init_screens()




# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog", "Conky"]



floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='Arandr'),
        Match(wm_class='feh'),
        Match(wm_class='Galculator'),
        Match(wm_class='archlinux-logout'),
        Match(wm_class='Conky'),
        Match(wm_class='blueman-manager'),
        Match(wm_class='nm-connection-editor'),
        Match(wm_class='xarchiver'),

    ],
    border_width = 2,
    border_focus = tokyonight["color2"],
)


auto_fullscreen = True
focus_on_window_activation = "smart"  # or focus
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


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
