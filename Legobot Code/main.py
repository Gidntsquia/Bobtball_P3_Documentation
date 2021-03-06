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
    u.calibrate()
    a.hold_cube_and_deliver_ambulance()
    a.hold_cube_and_get_prism()
    u.sd()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()