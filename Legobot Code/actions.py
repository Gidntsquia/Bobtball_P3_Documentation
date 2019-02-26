# The bulk of commands should go here

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

def deliver_ambulance():
    u.enable_servo(c.CLAW_SERVO)
    u.set_servo_position(c.CLAW_SERVO, c.STARTING_CLAW_POS)
    m.open_claw()
    s.backwards_until_black_third()                                                                                                                                    
    m.close_claw()
    m.drive(450)    
    m.turn_left()
    m.turn_left(750)
    m.drive(250)
    s.drive_until_black_third()
    s.left_point_turn_until_black()
    s.lfollow_left_until_right_senses_black_smooth()
    #w.check_zones_hospital()
    m.turn_left(75)
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        m.drive(300)
        #m.open_claw_2()
        m.backwards(300)
        m.turn_left()
        m.turn_left()
        m.backwards(400)
        m.open_claw()
    if c.SAFE_HOSPITAL == C.FAR_ZONE:
        m.drive(1)
        s.drive_through_line_third()
        s.lfollow_right_until_left_senses_black_smooth()
