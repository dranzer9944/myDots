from typing import Optional
from libqtile.widget.textbox import TextBox

#################################
###########  CIRCLE   ##########
#################################
def left_half_circle(fg_color,  bg_color: Optional['str'] = None):
    return TextBox(
        text='',
        fontsize=25,
        font="Mononoki Regular",
        foreground=fg_color,
        background=bg_color,
        padding=0
    )

def right_half_circle(fg_color, bg_color: Optional['str'] = None):
    return TextBox(
        text='',
        fontsize=25,
        font="Mononoki Regular",
        background=bg_color,
        foreground=fg_color,
        padding=0
    )


########################################
#########  TRIANGLE   ##################
########################################
def upper_left_triangle(fg_color, bg_color):
    return TextBox(
        text='',
        padding=0,
        font="Mononoki Regular",
        fontsize=25,
        background=bg_color,
        foreground=fg_color
    )


def lower_right_triangle(fg_color, bg_color):
    return TextBox(
        text='',
        padding=0,
        fontsize=25,
        font = "Mononoki Regular",
        background=bg_color,
        foreground=fg_color
    )



def left_arrow(fg_color, bg_color):
    return TextBox(
        text='',
        padding=0,
        fontsize=25,
        font = "Mononoki Regular",
        background=bg_color,
        foreground=fg_color
    )


def right_arrow(fg_color, bg_color):
    return TextBox(
        text='',
        padding=0,
        fontsize=25,
        font = "Mononoki Regular",
        background=bg_color,
        foreground=fg_color
    )
