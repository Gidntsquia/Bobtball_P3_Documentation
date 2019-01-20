# The bulk of commands should go here

from wallaby import *
import constants as c
import movement as m
import sensors as s
import webcam as w

def deliver_ambulance():
    print "Starting deliver_ambulance()"
    s.drive_through_two_lines_third()
    s.left_point_turn_until_black()
    w.check_zones_hospital()
    s.lfollow_left_until_right_senses_black_smooth()
    s.align_close()
    if c.SAFE_HOSPITAL == c.NEAR_ZONE:
        s.drive_through_line_left()
        #m.open_claw()
    else:
        s.drive_through_line_right()
        m.drive(200)
        s.right_point_turn_until_black()
        s.right_point_turn_until_white()
        s.lfollow_right_inside_line_until_left_senses_black_smooth()
        s.lfollow_right_inside_line_until_left_senses_white_smooth()
        s.lfollow_right_inside_line_smooth(1000)
        m.turn_left()
        #m.open_claw()
    print "Finished deliver_ambulance()"


