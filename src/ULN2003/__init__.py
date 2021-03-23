import RPi.GPIO as GPIO
import time

FORWARD = True
BACKWARD = False

class ULN2003_driver:
    _seq = [
        [0,1,0,0],
        [0,1,0,1],
        [0,0,0,1],
        [1,0,0,1],
        [1,0,0,0],
        [1,0,1,0],
        [0,0,1,0],
        [0,1,1,0]
    ]

    _current_seq = 0
    _speed = 0
    _step_interval = 1

    def __init__(self, in1: int, in2: int, in3: int, in4: int) -> None:
        self._pins = [
            in1, in2, in3, in4
        ]

        for pin in self._pins:
            GPIO.setup(pin, GPIO.OUT)

    def _step_up(self):
        self._current_seq += 1

        if self._current_seq > 7:
            self._current_seq = 0

    def _step_down(self):
        self._current_seq -= 1

        if self._current_seq < 0:
            self._current_seq = 7
        
    def _write_seq(self):
        for i in range(0, 4):
            GPIO.output(self._pins[i], self._seq[self._current_seq][i])
    
    def set_speed(self, spd: float):
        self._speed = abs(spd)

        self._step_interval = abs(1000.0 / spd)

    def microsteps(self, steps: int, direction: bool = FORWARD):
        for step in range(steps):
            if direction:
                self._step_up()
            else:
                self._step_down()
            
            self._write_seq()
            time.sleep(self._step_interval / 1000.0)