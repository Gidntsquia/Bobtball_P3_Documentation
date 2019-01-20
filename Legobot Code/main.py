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
import gyro as g

def main():
    print "Starting main()\n"
    u.setup()
    #u.calibrate()  # You only need to include this command if you want the tophats to sense better at the cost of speed.
    g.calibrate_gyro_degrees()
    msleep(5000)
    g.turn_gyro(45)
    msleep(5000)
    g.turn_gyro(-90)
    msleep(5000)
    g.turn_gyro(45)
    u.shutdown()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
