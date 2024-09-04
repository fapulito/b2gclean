# -*- coding: utf-8 -*-
import time
from pinpong.board import Board, Pin
from pinpong.extension.unihiker import *

Board().begin()  # Initialize the UNIHIKER

# Music: DADADADUM ENTERTAINER PRELUDE ODE NYAN RINGTONE FUNK BLUES BIRTHDAY WEDDING FUNERAL PUNCHLINE
# Music: BADDY CHASE BA_DING WAWAWAWAA JUMP_UP JUMP_DOWN POWER_UP POWER_DOWN
# Play mode: Once (play once) Forever (play continuously) OnceInBackground (play once in the background) ForeverInBackground (play continuously in the background)
buzzer.play(buzzer.DADADADUM, buzzer.Once)  # Play music once
# buzzer.set_tempo(4, 60)  # Set the number of notes per beat and the beats per minute
buzzer.pitch(494, 4)  # Play a pitch/note
# buzzer.pitch(494)  # Play a pitch/note in the background
# time.sleep(10)
# buzzer.stop()  # Stop playing in the background
# buzzer.redirect(Pin.P0)  # Redirect the buzzer to a specific pin, only supports PWM pins
# buzzer.play(buzzer.ENTERTAINER, buzzer.ForeverInBackground)  # Play music continuously in the background
while True:
    time.sleep(1)  # Wait for 1 second to maintain the state