from wallaby import *
import constants as c
import movement as m
import actions as a
import sensors as s

def initialize_camera():
    # Wait two seconds for camera to initialize
    print "Initializing Camera"
    i = 0  # Counter
    print "Starting Step 1..."
    while i < 55:
        camera_update()
        i += 1
        msleep(1)
    print "Finished Step 100\n"


def check_zones_hospital():
    print "Checking zones"
    msleep(25)
    ao()
    # This fully turns of the motors instead of just stopping them. Do not remove.
    camera_open()
    initialize_camera()
    if get_object_area(c.YELLOW, 0) > 50:
        c.FIRE_HOSPITAL = c.NEAR_ZONE
        c.SAFE_HOSPITAL = c.FAR_ZONE
    else:
        c.FIRE_HOSPITAL = c.FAR_ZONE
        c.SAFE_HOSPITAL = c.NEAR_ZONE
    print "Fire Hospital Zone: " + str(c.FIRE_HOSPITAL)
    print "Safe Hospital Zone: " + str(c.SAFE_HOSPITAL)

"""
#    Psuedocode:
#    check zone in front of robot
#    if zone is yellow, that zone is the fire zone and the other zone is the safe zone
#    if zone is not yellow, that zone is the safe zone and the other zone is the fire zone
#    finish
"""
