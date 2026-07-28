# ------------------------------------
#  ____   __   ____  ____   __   _  _ 
# (__  ) / _\ / ___)/ ___) /  \ / )( \
#  / _/ /    \\___ \\___ \(  O )) \/ (
# (____)\_/\_/(____/(____/ \__/ \____/
# ------------------------------------
# Written by Toastuy

from .src import hooks
from .src import homepage

def initialize():
    hooks.init_hooks()

initialize()
