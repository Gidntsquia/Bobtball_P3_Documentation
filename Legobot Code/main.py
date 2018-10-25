#!/usr/bin/env python2
import os
import sys
from wallaby import *
import constants as c
import actions as a
import sensors as s
import movement as m
import webcam as w
import utils as u

def main():
    print "Starting main()\n"
    u.setup()
    u.calibrate()  # You only need to include this command if you want the tophats to sense better at the cost of speed.
    s.drive_until_black_left(10000, False)
    s.drive_until_white_left(10000, False)
    s.align_far_smart()
    s.drive_until_black_third(10000, False)
    s.drive_until_white_third(10000, False)
    s.drive_until_black_third(10000, False)
    s.drive_until_white_third()
    s.left_point_turn_until_black()
    s.pid_lfollow_left_until_right_senses_black()
    m.drive(500)
    m.turn_left()
    s.align_far_smart()
    u.shutdown()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
