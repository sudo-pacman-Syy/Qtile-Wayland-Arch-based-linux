import os
from libqtile import bar, layout, widget,hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.backend.wayland import InputConfig
from libqtile import hook
import subprocess

mod = "mod4"
mod1 = "mod1"
terminal = guess_terminal()


colors = {
    "bg": "#1e1e2e80",
    "fg": "#cdd6f4",
    "accent": "#89b4fa",
    "inactive": "#45475a"
}

wl_input_rules = {
    "type:keyboard": InputConfig(
        kb_layout="us,ru",
        kb_options="grp:alt_shift_toggle",
    ),
}
def run_waybar():
    subprocess.Popen(["killall", "waybar"])
    subprocess.Popen(["waybar"])


keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle layout"),
    Key([mod], "equal", lazy.spawn("pactl set-sink-volume 0 +10%"), desc='Volume Up'),
    Key([mod], "minus", lazy.spawn("pactl set-sink-volume 0 -10%"), desc='volume down'),
    #Open Rofi
    Key([mod1], "space", lazy.spawn("rofi -show drun"), desc="Rofi launcher"),
    #Screenshot
    Key([], "Print", lazy.spawn("sh -c 'grim -g \"$(slurp)\" ~/Pictures/Screenshots/$(date +%Y-%m-%d_%H-%M-%S).png'"))
]
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])


layouts = [
    layout.Columns(
        border_focus=colors["accent"],
        border_normal=colors["inactive"],
        border_width=3,
        margin=4,
        num_columns=3,
    ),
    layout.Max(),
]

widget_defaults = dict(font="DejaVu Sans Mono", fontsize=13, padding=3)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
            widget.GroupBox(   
                highlight_method="line",
                highlight_color=[colors["bg"], colors["bg"]],
                this_current_screen_border=colors["accent"],
                active=colors["fg"],
                inactive=colors["inactive"],
                rounded=False,
                padding=10,
            ),
            widget.Spacer(),
            widget.Clock(format='Time: %H:%M',fontsize=15, foreground=colors["fg"]),
            widget.Spacer(),
            widget.Memory(format='  RAM {MemUsed:.0f}{mm}', foreground=colors["accent"]),
            widget.CPU(format='CPU  {load_percent}%', foreground=colors["accent"], padding=10),
            widget.PulseVolume(fmt='VOL: {} ',foreground=colors["accent"]),
            ],
            23, # heigh bar
            background=colors["bg"],
            opacity=1.0,
            margin=[10, 0, 0, 0],
        ),),
]

# Autostart
@hook.subscribe.startup_once
def autostart():
    wallpaper_path = os.path.expanduser("images/Garou Skull Pose Wallpaper.png")
    subprocess.Popen(["swaybg", "-i", wallpaper_path, "-m", "fill"])


floating_layout = layout.Floating(float_rules=[Match(wm_class="confirmreset")])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_xcursor_theme = None
wl_xcursor_size = 24
