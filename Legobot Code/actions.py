## The bulk of commands should go here

from wallaby import *
import constants as c
import movement as m
import sensors as s
import utils as u
import webcam as w

far_safe_zone = False



def ambulance_guy():
    s.drive_through_line_third(0)
    s.drive_through_line_third()
    s.turn_left_until_black()
    print "turned"
    #s.lfollow_left_until_right_senses_black_smooth()
    print "done"


def deliver_ambulance():
    u.enable_servo(c.CLAW_SERVO)
    m.lower_arm()
    s.backwards_until_black_third()                                                                                                                                    
    m.lift_arm()
    s.backwards_through_line_third(c.SAFETY_TIME)    
    s.turn_right_until_black()
    s.lfollow_right_until_left_senses_black_smooth()
    w.check_zones_hospital()
    #c.SAFE_HOSPITAL == c.FAR_ZONE:

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
    else:
        s.drive_through_line_left()
        m.drive(300)
        s.turn_left_until_right_senses_white(0)
        s.turn_left_until_right_senses_black(0)
        s.turn_left_until_right_senses_white(0)
        s.turn_left_until_black()
        m.lower_arm()
        s.drive_until_black_left()
        s.backwards_through_line_third()

        
            
def fireFighters():
    if c.SAFE_HOSPITAL == c.FAR_ZONE:
        s.lfollow_left_until_right_senses_black(0)
        s.drive_through_line_right()
        
    else:
        pass
            
