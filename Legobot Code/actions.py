## The bulk of commands should go here

from wallaby import *
import constants as c
import movement as m
import sensors as s
import utils as u
import webcam as w

def near_zone_to_firefighter():
    u.sd
    
def deliver_ambulance():
    #u.enable_servo(c.CLAW_SERVO)
    m.lower_arm()  # makes sure claw is down just in case
    s.backwards_until_black_third()                                                                                                                       
    m.lift_arm()
    s.backwards_until_black_left()
    s.align_close()
    s.lfollow_left_inside_line_smooth(2000)
    #does the code below actualy get the firefghter
    s.backwards_through_line_third(c.SAFETY_TIME)    
    s.turn_right_until_black()
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
        s.drive_until_black_third() 
        # this makes it turn 180 reliably---------------------------------------------------------
        s.turn_left_until_right_senses_black(0)
        s.turn_left_until_right_senses_white(0)
        s.turn_left_until_right_senses_black(0)
        s.turn_left_until_right_senses_white(0)
        s.turn_left_until_black()
        # end of 180---------------------------------------------------------------
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
            
