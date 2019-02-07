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
    
def prismriver():
    s.forwards_until_black_lcliff()
    s.forwards_until_white_lcliff()
    s.forwards_until_black_lcliff()
    m.turn_left(1600)
    s.lfollow_lfcliff_smooth_until_rfcliff_senses_white()
    s.forwards_until_black_lcliff()
    s.forwards_until_white_lcliff()
    s.forwards_until_black_lfcliff()
    m.turn_left()
    m.turn_left()
    s.forwards_until_white_rcliff()
    s.forwards_until_black_rfcliff()
    s.forwards_until_white_rfcliff()
    s.forwards_until_black_rfcliff()
    s.lfollow_lcliff_smooth_until_bump()
    m.turn_right()
    m.turn_right()
    s.forwards_until_black_lcliff()
    s.forwards_until_white_lcliff()
    s.forwards_until_black_lfcliff()
    m.turn_left()
    s.lfollow_lfcliff_smooth_until_rfcliff_senses_black()
    m.turn_right()
    s.lfollow_lcliff_smooth(4000)
    m.turn_left()
    m.turn_left()
    s.lfollow_lcliff_smooth(4000)
    m.turn_left()
    s.lfollow_lcliff_smooth_until_bump(999999)
    m.turn_left()
    s.forwards_until_black_lcliff()
    m.forwards(1000)
    m.turn_right()
    m.forwards_until_black_lcliff()
    m.forwards_until_white_lcliff()
    m.forwards_until_black_lfcliff()
    m.turn_left()
    s.forwards_until_black_lcliff()
    m.forwards(1000)
    m.turn_right()
    m.forwards_until_black_lcliff()
    m.forwards_until_white_lcliff()
    m.forwards_until_black_lfcliff()