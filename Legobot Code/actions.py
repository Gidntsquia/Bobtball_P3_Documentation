## The bulk of commands should go here

from wallaby import *
import constants as c
import movement as m
import sensors as s
import utils as u
import webcam as w
def fireFighters():
    m.turn_left()
    s.drive_until_black()
    s.smart_close_align()
    s.drive_through_two_lines_third()
    s.turn_left_until_left_black()
    s.lfollow_left_until_right_senses_black()

def ambulance_guy():
    s.drive_through_line_third(0)
    s.drive_through_line_third()
    s.turn_left_until_black()
    print "turned"
    #s.lfollow_left_until_right_senses_black_smooth()
    print "done"


def deliver_ambulance():
    u.enable_servo(c.CLAW_SERVO)
    u.set_servo_position(c.CLAW_SERVO, c.STARTING_CLAW_POS)
    m.open_claw()
    s.backwards_until_black_third()                                                                                                                                    
    m.close_claw()
    s.backwards_through_line_third(c.SAFETY_TIME)    
    s.turn_right_until_black()
    s.lfollow_right_until_left_senses_black_smooth()
    w.check_zones_hospital()
    if c.SAFE_HOSPITAL == c.FAR_ZONE:
        m.drive(300)
        #m.open_claw_2()
        m.backwards(300)
        m.turn_left()
        m.turn_left()
        m.backwards(400)
        m.open_claw()
    else:
        s.drive_through_line_left()
        m.drive(500)
        s.turn_left_until_right_senses_black(0)
        s.turn_left_until_right_senses_white(0)
        s.turn_left_until_black()
        m.open_claw()
        s.backwards_through_line_third()
        #s.lfollow_right_until_left_senses_black_smooth()
