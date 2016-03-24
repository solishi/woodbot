#!/usr/bin/env python

_author__ = 'Copyright (c) 2015 Alan Yorinks All rights reserved.'

"""
Copyright (c) 2015 Alan Yorinks All rights reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU  General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""

"""
This example illustrates manipulating a servo motor.
"""

import time
import sys
import signal

from PyMata.pymata import PyMata


SERVO_MOTOR = 9  # servo attached to this pin

# create a PyMata instance
board = PyMata("/dev/ttyACM0")


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!!!!')
    if board is not None:
        board.reset()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
# control the servo - note that you don't need to set pin mode
# configure the servo
board.servo_config(SERVO_MOTOR)

while (1):
    # move the servo to 20 degrees
    board.analog_write(SERVO_MOTOR, 20)
    time.sleep(1)

    # move the servo to 100 degrees
    board.analog_write(SERVO_MOTOR, 100)
    time.sleep(1)

# move the servo to 20 degrees
board.analog_write(SERVO_MOTOR, 20)

# close the interface down cleanly
board.close()
