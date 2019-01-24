Any Roomba code should go here.

Feel free to just ignore this folder if you're not working on the Roomba.

def prismriver():
    m.turn_left()
    s.forwards_until_black_cliff(999999999)
    m.turn_left()
    s.lfollow_right_smooth_until_rcliff_senses_white()
    s.forwards_until_black_cliff()
    s.forwards_until_white_cliff()
    s.forwards_until_black_cliff()
    m.turn_left()
    m.turn_left()
