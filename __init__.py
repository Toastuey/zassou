# ------------------------------------
#  ____   __   ____  ____   __   _  _ 
# (__  ) / _\ / ___)/ ___) /  \ / )( \
#  / _/ /    \\___ \\___ \(  O )) \/ (
# (____)\_/\_/(____/(____/ \__/ \____/
# ------------------------------------
# Written by Toastuy
# 
# BRIEF
# The intent of this addon is to find problematic "super leeches" or "would be leeches" and give them extra attention
# I have found myself remining the same word multiple times, only for it to continuously become a leech
# This addon will present to you any cards that have >= a specified number of lapses
# 
# DISCLAIMER
# It is almost always better to delete and remine leeches in a better context, or to just be naturally exposed to them
# through immersion. That being said, I still do think there are use cases for this addon, or could be used out of
# personal preference. Some could also argue that this is the job of FSRS, and I agree, but I still wanted to make this :^)

from .src import hooks
from .src import homepage

def initialize():
    hooks.init_hooks()

initialize()
