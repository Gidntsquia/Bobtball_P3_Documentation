## The bulk of commands should go here

from wallaby import *
import constants as c
import movement as m
import sensors as s
import utils as u
import webcam as w


def near_zone_to_firefighter():
    u.sd

def deliver_goods():
    s.backwards_through_line_third()
    m.lift_arm()
    s.drive_through_line_third()
    s.turn_right_until_black()
    m.close_claw()
    s.drive_through_line_right()
    s.left_backwards_until_third_senses_black()
    s.backwards_through_line_left(0)
    s.backwards_through_line_third()
    s.turn_right_until_left_senses_black(0)
    s.turn_right_until_left_senses_white()
    s.lfollow_left_until_right_senses_black_smooth()
    w.check_zones_hospital()
    

def deliver_ambulance():
    s.backwards_until_black_third()
    m.lift_arm()
    s.drive_until_black_third()
    s.turn_right_until_black()
    msleep(1000)
    m.turn_left(int(c.RIGHT_TURN_TIME/1.25))
    s.backwards_through_line_left(0)
    s.backwards_through_line_third()
    s.turn_right_until_left_senses_black(0)
    s.turn_right_until_left_senses_white()
    s.lfollow_right_until_left_senses_black(2000)
    s.lfollow_right_until_left_senses_black_smooth()
    w.check_zones_hospital()
    #c.SAFE_HOSPITAL = c.FAR_ZONE
    if c.SAFE_HOSPITAL == c.FAR_ZONE:
        s.drive_through_line_left(0)
        s.drive_until_black_third()
        s.turn_right_until_black()
        s.lfollow_right_until_left_senses_black_smooth()
        s.drive_through_line_left(0)
        s.drive_until_black_third()
        s.turn_right_until_black(0)
        s.turn_right_until_white(0)
        s.turn_right_until_black(0)
        s.turn_right_until_black(0)
        s.turn_right_until_white()
        m.lower_arm()
        s.drive_until_black_left()
    else:  # Near zone
        s.drive_through_line_left(0)
        s.snap_to_line_left(0)  # this makes it turn 180 reliably
        s.turn_left_until_right_senses_white(0)
        s.turn_left_until_right_senses_black(0)
        s.turn_left_until_right_senses_white(0)
        s.turn_left_until_black()
        m.lower_arm()
        #s.drive_until_black_left()
        s.backwards_through_line_third()

            
def get_firefighters():
    if c.SAFE_HOSPITAL == c.FAR_ZONE:
        s.drive_through_line_third()
        s.turn_left_until_black()
        s.left_forwards_until_white()
        s.left_forwards_until_black()
        #TODO: Finish this if statement
    else:
        s.turn_right_until_black()
        s.drive_through_line_left(0)
        s.drive_through_line_third()
        s.turn_right_until_black(0)
        s.turn_right_until_white()
        #s.drive_until_white_left()
        #s.turn_right_until_left_senses_black()
        #s.turn_left_until_left_senses_white()
        #print "starting ending lfollow"
        #s.lfollow_left_until_third_senses_black_smooth()
            
