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
   s.drive_until_black_third(99999,False)
   s.drive_until_white_third(99999,False)
   s.drive_until_black_third()
   s.left_point_turn_until_black()
   s.align_close()
   s.lfollow_left_until_right_senses_black_smooth()
   s.lfollow_left_smooth(1500)
   m.turn_left(650)
   s.align_far()
   m.lower_arm()
   m.backwards(2200)
   m.close_claw()
   s.lfollow_left_until_right_senses_black_smooth()
   s.left_point_turn_until_right_senses_black()
   s.lfollow_right_smooth(7600)
   m.turn_right()
   s.backwards_until_black_third()
   m.open_claw()
       
def length_test():
   s.lfollow_left_smooth(7500)
   f.left_point_turn_until_right_senses_black()
   f.lfollow_right_smooth(8200)
   m.turn_left()
   m.backwards(1300)
       
