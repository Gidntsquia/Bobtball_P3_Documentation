# The bulk of commands should go here

from wallaby import *
import constants as c
import movement as m
import linefollow as f
import webcam as w

crate_zone = 30  # In place for ease of GitHub compilation.
botguy_zone = 30  # Ditto to above.

def emmett_command():
    m.drive(3000)
    m.turn_left()
    m.drive(3000)
    m.turn_left()
    m.drive(3000)
    m.turn_left()
    m.drive(3000)
    m.turn_left()
        
def linefollow_command():
    f.drive_until_black_left()
    f.drive_until_white_left()
    f.drive_until_black_left()
    m.turn_left()
    f.lfollow_left_smooth(6000)
        
def crate_challenge():
    m.drive(3000)
    m.turn_left()
    f.lfollow_left_smooth(3000)
    m.turn_left()
    m.backwards(1000)
    m.lower_arm()
    m.close_arm()
    m.turn_left()
    m.drive(3000)
    f.lfollow_right_smooth()
