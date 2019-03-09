#---------------------------------------------Motors-------------------------------------------

# Motor Ports (Not real - made to be consistent with Legobot)
LEFT_MOTOR = 2
RIGHT_MOTOR = 3

# Running Motor Powers
CURRENT_LM_POWER = 0
CURRENT_RM_POWER = 0
#---------------------------------------------Servos-------------------------------------------

# Servo Port
ARM_SERVO = 1
CLAW_SERVO = 2
MICRO_SERVO = 3

# Servo Limits
MAX_ARM_SERVO_POS = 1850
MIN_ARM_SERVO_POS = 200

# Servo Base Positions
ARM_UP_POS = 639 # 640  # The arm is just above the poms but below the frisbee.
ARM_DOWN_POS = 1598  # The arm is perpendicular to the ground.
ARM_DELIVERY_POS = 1240
ARM_START_POS = ARM_UP_POS
CLAW_OPEN_POS = 1024
CLAW_CLOSE_POS = 1024
CLAW_START_POS = CLAW_OPEN_POS

# Micro Servo Positions
MICRO_RIGHT_POS = 1520
MICRO_LEFT_POS = 815
MICRO_STRAIGHT_POS = 1176
MICRO_START_POS = MICRO_STRAIGHT_POS

#---------------------------------------------Movement---------------------------------------------

# Turn Values
RIGHT_TURN_TIME = 1582
LEFT_TURN_TIME = 1582

# Motor Values
BASE_LM_POWER = 109
BASE_RM_POWER = 100

# Default Drive Times
DEFAULT_DRIVE_TIME = 500
DEFAULT_BACKWARDS_TIME = 500

#----------------------------------------------Sensors--------------------------------------------- 

# Analog Sensor Ports
# Cliffs are built into the Roomba, no need for analog ports.
DEPTH_SENSOR = 0
LIGHT_SENSOR = 5

# Analog Sensor Values
LCLIFF_BW = 2451  # Min is 0, max is 4950
RCLIFF_BW = 2533  # If more white, if less black
LFCLIFF_BW = 2350
RFCLIFF_BW = 2750
LFOLLOW_REFRESH_RATE = 20 

# Smooth Lfollow Motor Values
LFOLLOW_SMOOTH_LM_POWER = int (.7 * BASE_LM_POWER)
LFOLLOW_SMOOTH_RM_POWER = int (.7 * BASE_RM_POWER)

# Depth Sensor Values
DEPTH_CF = 1250

