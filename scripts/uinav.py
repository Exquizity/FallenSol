from turtle import speed
from ahk import AHK
ahk = AHK()

# INGAME Ui Navigation Stuff
# functions work like this: ui(type)_uielement()
# for example, the button to exit collection would be ui_collection_exit()
# Automatically clicks the button too
# This is here js so i remember how to work this script cuz im gonna forget at some point

def click():
    ahk.click()

def move(x, y):
    ahk.mouse_move(x, y, speed=3)
    click()


# NPC UI

def ui_npc_option1():
    move(650, 946)


def ui_npc_option2():
    move(956, 943)

def ui_npc_option3():
    move(1273, 947)

def ui_npc_skipdialogue():
    move(788, 805)
    click()


# MAIN UI
# Aura Menu

def ui_aura_button():
    move(34, 402)

def ui_aura_search():
    move(827, 367)

def ui_aura_firstslot():
    move(820, 430)

def ui_aura_equip():
    move(627, 634)

# Collection Menu

def ui_collection_open():
    move(33, 456)

def ui_collection_exit():
    move(385, 128)

# Inventory Menu

def ui_inventory_button():
    move(33, 510)

def ui_inventory_itemsmenu():
    move(1273, 337)

def ui_inventory_search():
    ui_aura_search() # yes im that lazy and its in the same position so who cares

def ui_inventory_firstslot():
    move(850, 474)

def ui_inventory_useamount():
    move(568, 579)

def ui_inventory_use():
    move(682, 576)



# ROBLOX STUFF

def ui_chat_button():
    move(138, 30)

def ui_chat_servermessage():
    move(432, 78)

def ui_chat_check(): # Where the mouse moves to show the chat window to close it if the server message tab is open
    move(197, 222)

# FISHING STUFF

def ui_fishing_button():
    move(850, 836)

def ui_fishing_exitsummary():
    move(1112, 341)

def ui_fishing_sellmenu():
    move(1304, 312)

def ui_fishing_firstitem():
    move(827, 404)

def ui_fishing_sell():
    move(516, 806)

def ui_fishing_sellall():
    move(667, 806)

def ui_fishing_sellconfirm():
    move(805, 621)