from wallaby import *
import constants as c
import sensors as s
import movement as m
import utils as u

def my_command():
    print "Starting my_command()"
    
    
    print "Finished my_command()"

def point_a_to_b():
    pass
    
def nuclearfusion():
    s.lfollow_lcliff_smooth_until_bump()
    
def gas():
    s.forwards_until_black_rfcliff_safe()
    s.forwards_until_white_rfcliff_safe()
    s.forwards_until_black_rfcliff_safe()
    s.align_close_fcliffs()
    s.forwards_until_white_rfcliff_safe()
    m.drive(500)
    m.turn_left(1500)
    s.lfollow_lfcliff_smooth_until_rfcliff_senses_white()
    s.forwards_until_black_lfcliff()
    s.align_close_fcliffs()
    m.turn_right(117)
    s.forwards_until_bump()
    m.backwards(1000)
    m.turn_left()
    m.turn_left()
    s.forwards_until_black_lfcliff()
    s.align_close_fcliffs()
    m.lower_arm()
    #left turn of doom. 
    m.backwards(1100)
    m.lift_arm()
    s.forwards_until_black_rfcliff()
        
def magnet():
    m.turn_left()
    s.forwards_until_black_rfcliff_safe()
    s.forwards_until_white_rfcliff_safe()
    s.forwards_until_black_rfcliff_safe()
    s.align_close_fcliffs()    
    m.turn_right()
    s.align_close_fcliffs()    
    m.turn_right()
    s.lfollow_lfcliff_smooth_until_bump()
   
def a(): 
    m.turn_right()
    m.turn_right()
    s.forwards_until_black_lcliff()
    s.align_close_fcliffs()
    s.forwards_until_white_lcliff()
    s.forwards_until_black_lfcliff()
    s.align_close_fcliffs()
    m.turn_left()
    m.turn_left()
    s.forwards_until_white_rfcliff_safe()
    s.forwards_until_black_rfcliff_safe()
    s.forwards_until_white_rfcliff_safe()
    s.forwards_until_black_rfcliff_safe()
    s.lfollow_lcliff_smooth_until_bump()
    s.align_close_fcliffs()
    m.turn_right()
    m.turn_right()
    s.forwards_until_black_lfcliff()
    s.forwards_until_white_lfcliff()
    s.forwards_until_black_lfcliff()
    m.turn_left()
    s.lfollow_lfcliff_smooth_until_rfcliff_senses_black()
    m.turn_right()
    s.lfollow_lcliff_smooth(4000)
    s.align_close_fcliffs()
    m.turn_left()
    m.turn_left()
    s.lfollow_lcliff_smooth(4000)
    s.align_close_fcliffs()
    m.turn_left()
    s.lfollow_lcliff_until_bump(999999)
    s.align_close_fcliffs()
    m.turn_left()
    s.forwards_until_black_lcliff()
    m.forwards(1000)
    s.align_close_fcliffs()
    m.turn_right()
    m.forwards_until_black_lcliff()
    m.forwards_until_white_lcliff()
    m.forwards_until_black_lfcliff()
    s.align_close_fcliffs()
    m.turn_left()
    s.forwards_until_black_lcliff()
    m.forwards(1000)
    s.align_close_fcliffs()
    m.turn_right()
    m.forwards_until_black_lcliff()
    m.forwards_until_white_lcliff()
    m.forwards_until_black_lfcliff()
    s.align_close_fcliffs()
    m.turn_right()
    m.forwards_until_black_lcliff()
    m.forwards_until_white_lcliff()
    m.forwards_until_black_lfcliff()
