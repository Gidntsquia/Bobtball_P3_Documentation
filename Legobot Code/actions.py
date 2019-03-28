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
    #m.lift_cube_arm()
    #m.open_claw()
    s.backwards_until_black_left()
    m.lift_arm()
    s.drive_until_black_third()
    s.turn_right_until_black()
    s.backwards_through_line_third()
    m.backwards(300)
    m.lower_cube_arm()
    s.drive_through_line_third()
    m.close_claw()
    m.lift_cube_arm()
    m.turn_left(int(c.RIGHT_TURN_TIME/1.5))
    s.backwards_through_line_left(0)
    s.backwards_through_line_third()
    s.turn_right_until_left_senses_black(0)
    s.turn_right_until_left_senses_white()
    s.lfollow_left_until_right_senses_black(1000)
    s.lfollow_left_until_right_senses_black_smooth()
    s.turn_right_until_white(0)
    s.turn_right_until_black()
    m.lower_arm()
    w.check_zones_hospital()
    m.lift_arm()
    if c.SAFE_HOSPITAL == c.FAR_ZONE:
        s.backwards_through_line_third()
        s.turn_right_until_white(0)
        s.turn_right_until_black()
        s.backwards_until_white_right(0)
        m.backwards(500)
        m.lower_arm()
        s.drive_until_black_third()
        s.turn_right_until_left_senses_black(0)
        s.turn_right_until_left_senses_white()
        s.lfollow_left_until_right_senses_black_smooth(0)
        s.drive_through_line_right(0)
        s.drive_until_black_right()
        s.align_close()
        s.turn_right_until_white(0)
        s.turn_right_until_black(0)
        s.turn_right_until_white(0)
        s.turn_right_until_black()
        s.align_close()
        m.lower_cube_arm()
        m.open_claw()
    else:  # Near zone
        s.backwards_through_line_third()
        m.lower_arm()
        s.drive_until_black_third()
        s.turn_left_until_black()
        s.turn_left_until_white()
        s.drive_through_line_left()
        m.lower_cube_arm()
        m.open_claw()
        

            
def get_firefighters():
    if c.SAFE_HOSPITAL == c.FAR_ZONE:
        pass
        #s.drive_through_line_right(0)
        #s.snap_to_line_right()
        #s.lower_cube_arm()
        #s.close_claw()
        

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
            