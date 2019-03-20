from wallaby import *
import constants as c
import sensors as s
import movement as m
import utils as u

def nuclearfusion():
    s.lfollow_lcliff_smooth_until_bump()


def get_gas_valve():
    s.forwards_until_black_rfcliff_safe()
    s.forwards_until_white_rfcliff_safe()
    s.align_far_fcliffs()
    s.forwards_until_white_rfcliff_safe()
    s.forwards_until_black_rfcliff_safe()
    s.align_close_fcliffs()
    m.backwards(300)    
    s.forwards_until_white_rfcliff_safe()
    s.forwards_through_line_rcliff()
    m.turn_left()
    s.forwards_through_line_lfcliff()
    s.align_far_fcliffs()
    s.forwards_until_bump()
    m.backwards(1000)
    m.turn_left(1800)
    m.turn_left()
    s.forwards_until_black_lfcliff()
    s.align_close_fcliffs()
    m.lower_arm()
    #left turn of doom. 
    m.backwards(950)
    m.lift_arm()
    s.forwards_until_black_lfcliff()
    s.align_close_fcliffs()
    s.forwards_until_bump()
    m.backwards(200)    
    m.turn_right(1650)
    s.backwards_until_black_lfcliff()   
    s.align_far_fcliffs()    
    s.forwards_until_white_rfcliff()
    s.forwards_until_black_rfcliff()
    s.align_close_fcliffs()
    m.backwards(200)    
    m.turn_right(c.RIGHT_TURN_TIME / 3)
    m.backwards(500)
    m.lower_arm(1, 3, c.ARM_DELIVERY_POS)
    m.turn_left(c.LEFT_TURN_TIME / 3)    
    m.backwards(500)

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
