## The bulk of commands should go here

from wallaby import *
import constants as c
import movement as m
import sensors as s
import utils as u
import webcam as w

def deliver_ambulance():
    print "Starting deliver_ambulance()"
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
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        s.backwards_through_line_third()
        m.lower_arm()
        # Ambulance delivered
        s.drive_until_black_third()
        s.turn_left_until_black()
        s.turn_left_until_white()
        s.drive_through_line_left()
        m.lower_cube_arm()
        m.open_claw()
    else:  # Safe hospital is far zone
        s.backwards_through_line_third()
        s.turn_right_until_white(0)
        s.turn_right_until_black()
        s.backwards_until_white_right(0)
        m.backwards(500)
        m.lower_arm()
        # Ambulance delivered
        s.drive_through_line_third()
        s.turn_right_until_black()
        m.turn_left(200)
        m.open_claw()
        m.lift_cube_arm()
        s.turn_left_until_black()
    print "Finished delivering ambulance and yellow cube"


def get_prism():
    print "Starting get_prism()"
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        s.backwards_through_line_left()
        s.turn_right_until_black(0)
        s.turn_right_until_white(0)
        s.turn_right_until_black(0)
        s.turn_right_until_left_senses_black(0)
        s.turn_right_until_left_senses_white()
        s.lfollow_left_until_right_senses_black_smooth()
        s.drive_through_line_right(0)
        s.drive_until_black_right()
        m.lower_cube_arm()
        m.close_claw()
        m.lift_cube_arm()
        s.align_close()
        s.turn_left_until_white(0)
        s.turn_left_until_black(0)
        s.turn_left_until_right_senses_black(0)
        s.turn_left_until_right_senses_white()
        s.lfollow_right_until_left_senses_black_smooth(0)
        s.drive_through_line_left()
        m.lower_cube_arm()
        m.open_claw()
        m.lift_cube_arm()

    else:  # Safe hospital is far zone
        s.lfollow_left_until_right_senses_black_smooth()
        m.lower_cube_arm()
        s.drive_through_line_right(0)
        s.drive_until_black_right()
        m.close_claw()
        m.lift_cube_arm()
        s.align_close()
        s.turn_left_until_white(0)
        s.turn_left_until_black(0)
        s.turn_left_until_right_senses_black(0)
        s.turn_left_until_right_senses_white()
        m.lower_cube_arm()
        m.open_claw()
    print "Finished getting and delivering yellow prism"


def get_blue_cube():
    print "Starting get_blue_cube()"
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        s.turn_right_until_black(0)
        s.turn_right_until_white(0)
        s.turn_right_until_black(0)
        s.turn_right_until_left_senses_black(0)
        s.turn_right_until_left_senses_white()
        s.lfollow_left_until_right_senses_black_smooth(0)
        s.drive_through_line_right(0)
        s.drive_until_black_right()
    else:  # Safe hospital is far zone
        m.lift_cube_arm()
        s.turn_right_until_black(0)
        s.turn_right_until_white(0)
        s.turn_right_until_black(0)
        s.turn_right_until_left_senses_black()
    s.align_close()
    m.lower_cube_arm()
    s.drive_until_white_third(0)
    s.drive_until_black_third(0)
    m.drive(900)
    # Drive until the blue cube is in claw
    m.close_claw()
    m.lift_cube_arm()
    m.turn_left()
    m.bumpfollow_right_until_left_senses_black(0)
    m.bumpfollow_right_until_left_senses_white()
    m.lower_cube_arm()
    m.open_claw()
    print "Finished delivering blue cube"

