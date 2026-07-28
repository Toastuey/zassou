from aqt import gui_hooks
from .homepage import display_weeds

def init_hooks():
    print("REGISTERING MY ADDON")
    gui_hooks.deck_browser_will_render_content.append(display_weeds)
    