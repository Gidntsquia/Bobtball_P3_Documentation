## The bulk of commands should go here

from wallaby import *
import constants as c
import movement as m
import sensors as s
import utils as u
import webcam as w

def get_firefighters():
    m.turn_left()
    s.drive_until_black()
    s.smart_close_align()
    s.drive_through_two_lines_third()
    s.turn_left_until_left_black()
    s.lfollow_left_until_right_senses_black()


def deliver_ambulance():
    u.enable_servo(c.CLAW_SERVO)
    m.lower_arm()
    s.backwards_until_black_third()                                                                                                                                    
    m.lift_arm()
    s.backwards_through_line_third(c.SAFETY_TIME)    
    s.turn_right_until_black()
    s.lfollow_right_until_left_senses_black_smooth()
    w.check_zones_hospital()
    if c.SAFE_HOSPITAL == c.FAR_ZONE:
        s.drive_through_line_left()
        s.drive_until_black_third()
        s.turn_right_until_black()
        s.lfollow_right_until_left_senses_black_smooth()
        s.drive_through_line_left()
        s.drive_until_black_third()
        s.turn_right_until_black(0)
        s.turn_right_until_white(0)
        s.turn_right_until_black(0)
        s.turn_right_until_black(0)
        s.turn_right_until_white(0)
        m.lower_arm()
        m.drive(700)
    else:
        s.drive_through_line_left()
        m.drive(300)
        s.turn_left_until_right_senses_white(0)
        s.turn_left_until_right_senses_black(0)
        s.turn_left_until_right_senses_white(0)
        s.turn_left_until_black()
        m.lower_arm()
        m.drive(700)
        s.backwards_through_line_third()