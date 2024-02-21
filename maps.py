# every different sprite is a new "code" (g is a code, x is a code)
# how to integrate npc's into this? must have their own codes (how to make them turn and stuff)
#
# to do the calculation of where the player should be placed onto a new map im thinking of making a linked list to do it
# like a sorta map thing ? future thing prob
#

TEST_MAP = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','x','x','x','x','x','x','g','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','b','x','x','x','x','x','x','x'],
['x','x','x','x','x','g','b','g','b','g','x','x','x','x','x'],
['x','x','x','x','x','b','g','b','g','b','x','x','x','x','x'],
['x','x','x','x','x','g','b','g','b','g','x','x','x','x','x'],
['x','x','x','x','x','b','g','b','g','b','x','x','x','x','x'],
['x','x','x','x','x','g','b','g','b','g','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
]

AI_MAP = [

['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','g','g','g','x','g','g','g','g','g','g','g','g','g','x'],
['x','g','x','g','x','g','x','x','x','x','x','g','x','g','x'],
['x','g','x','g','x','g','x','g','g','g','x','g','x','g','x'],
['x','g','x','g','x','g','x','g','x','g','x','g','x','g','x'],
['x','g','x','g','x','g','x','g','x','g','x','g','x','g','x'],
['x','g','x','x','x','g','x','g','x','g','x','g','x','g','x'],
['x','g','g','g','g','g','x','g','x','g','g','g','x','g','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']

]