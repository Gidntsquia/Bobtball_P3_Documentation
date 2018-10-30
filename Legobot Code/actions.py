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
    s.drive_until_black_left()
    s.drive_until_white_left()
    s.drive_until_black_left()
    m.turn_left()
    s.lfollow_left_smooth(6000)
        
def crate_challenge():
    s.drive_until_black_third()
    s.drive_until_white_third()
    s.drive_until_black_third()
    m.turn_left(800)
    s.align_close()    
    s.lfollow_left_smooth(3550)
    m.turn_left(800)                                                                                        
    m.backwards(2150)
    m.lower_arm()
    m.close_claw()
    m.drive(2500)
    m.turn_left()
    s.lfollow_right_smooth(3050)
    m.turn_right(800)
    s.align_close()
    s.drive_until_black_third()
    s.drive_until_white_third()
    s.drive_until_black_third()
        
def crate_collapse():
   s.drive_until_black_third()
   s.drive_until_white_third()
   s.drive_until_black_third()
   s.left_point_turn_until_black()
   s.align_close()
   s.lfollow_left_smooth(8200)
   m.turn_left()
   m.lower_arm()
   m.close_claw(1500)
   s.lfollow_backwards(2500)
   m.close_claw()
   s.lfollow_left(2500)
   s.left_point_turn_until_right_senses_black()
   s.lfollow_right_smooth(8200)
   m.turn_left()
   m.backwards(1300)
       
def length_test():
   s.lfollow_left_smooth(7500)
   f.left_point_turn_until_right_senses_black()
   f.lfollow_right_smooth(8200)
   m.turn_left()
   m.backwards(1300)
       
