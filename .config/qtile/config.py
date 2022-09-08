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
# from libqtile import qtile
from libqtile import layout, hook
from libqtile.command import lazy
from libqtile.config import Click, ScratchPad, DropDown, Drag, Group, Key, Match, Screen
# from imp import create_dynamic
# from libqtile.widget.battery import Battery, BatteryState
# from libqtile.widget.volume import Volume
# For theme
from colors import dracula
from bars.box_bar import bar


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



# Resize Floating Window
@lazy.window.function
def resize_floating_window(window, width: int = 0, height: int = 0):
    if window.floating == True or window.qtile.current_layout.name == 'floating':
        window.cmd_set_size_floating(window.width + width, window.height + height)

# For adjusting margin
@lazy.layout.function
def change_layout_gap(layout, adjustment):
    layout.margin += adjustment
    layout.cmd_reset()

#@lazy.function
#def increase_gaps(qtile):
#    qtile.current_layout.margin += 10
#    qtile.current_group.layout_all()


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
    Key([mod, "shift"], 'd', change_layout_gap(adjustment=-5), desc='decrease gap by 1'),
    Key([mod, "shift"], 'i', change_layout_gap(adjustment=5), desc='increase gap by 1'),
    #Key([mod], 'i', increase_gaps()),

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
    Key([mod], "d", lazy.spawn("dmenu_run -i -nb '#282a36' -nf '#bd93f9' -sb '#bd93f9' -sf '#282a36' -fn 'Mononoki Nerd Font:bold:pixelsize=14'")),
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

#group_labels = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 0 ",]
#group_labels = ["  ", "  ", " </> ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",]
group_labels = ["dev", "www", "sys", "doc", "vim", "chat", "mus", "vid", "gfx", "vbox",]

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
                   DropDown("term", myTerm, opacity=0.8, height=0.5, width=0.6),
                   DropDown("mixer", "pavucontrol", width=0.4, x=0.3, y=0.1),
                   #DropDown('khal', "alacritty -t ikhal -e ikhal", x=0.6785, width=0.32, height=0.997, opacity=1),
               ]),
)

## ScratchPad KeyBindings
keys.extend([
        # DropDown Term
        Key([mod], "s", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([mod], "v", lazy.group["scratchpad"].dropdown_toggle("mixer")),
        #Key([mod], "c", lazy.group["scratchpad"].dropdown_toggle("khal")),
])

layout_theme = {
    "margin": 15,
    "border_width": 2,
    "border_focus": dracula["color4"],
    "border_normal": dracula["colorback"],
}


layouts = [
    layout.MonadTall( **layout_theme),
    #layout.MonadWide(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
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
         font = "Mononoki Nerd Font",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = dracula["colorback"],
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
    font="Mononoki Nerd Font Bold",
    fontsize = 13,
    padding = 2,
    background= dracula["colorback"],
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


#widgets_list = init_widgets_list()


screens = [
    Screen(top=bar)
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
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
    border_focus = dracula["color2"],
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
