#!/usr/bin/env python
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


This example illustrates using callbacks for digital and analog input.

Monitor the current analog input and digital input of two pins.
"""

import signal
import sys
import time


from PyMata.pymata import PyMata


# Instantiate PyMata
board = PyMata("/dev/ttyACM0", verbose=True)

board.encoder_config(7,2)

# Set up pin modes for both pins with callbacks for each
board.set_pin_mode(5, board.PWM, board.DIGITAL)
board.set_pin_mode(6, board.PWM, board.DIGITAL)

board.analog_write(5, 255)
board.analog_write(6, 0)

time.sleep(2)
count = board.digital_read(2)
print count
time.sleep(2)
board.analog_write(5, 0)
