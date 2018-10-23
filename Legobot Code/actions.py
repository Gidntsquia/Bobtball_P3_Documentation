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
    f.drive_until_black_third()
    f.drive_until_white_third()
    f.drive_until_black_third()
    m.turn_left(800)
    f.align_close()    
    f.lfollow_left_smooth(3350)
    m.turn_left(800)                                                                                        
    m.backwards(2350)
    m.lower_arm()
    m.close_claw()
    m.drive(2500)
    m.turn_left()
    f.lfollow_right_smooth(3150)
    m.turn_right(800)
    f.align_close()
    f.drive_until_black_third()
    f.drive_until_white_third()
    f.drive_until_black_third()

