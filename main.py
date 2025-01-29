from pyscript import document  # webpage module links
# your roll_dice function should be saved in a file named 'dice.py'
# uncomment the next line when you have this prepared

import dice



# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = 6


def select_face_option(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code
    dice_type = int(event.target.vaule)


def roll_all_dice(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code
    result = dice.roll_dice(dice_type)
    document.querySelector("div#roll-history").innerHTML = "<p id='something'>" + str(result) + "</p>"

def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").value = ""
