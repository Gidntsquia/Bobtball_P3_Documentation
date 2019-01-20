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
    #a.get_ambulance()
    m.close_claw()
    g.calibrate_gyro()
    g.drive_gyro(20000, 2, 0, 0)
    
    #a.get_ambulance()
    #u.calibrate()  # You only need to include this command if you want the tophats to sense better at the cost of speed.
    #msleep(1000)
    #g.calibrate_gyro()
    #msleep(5000)
    #g.drive_gyro(5000)
    u.shutdown()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
