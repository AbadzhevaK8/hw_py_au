#! python3
"""
countdown.py - простой сценарий обратного отсчета
"""

import time
import subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft -= 1

# воспроизведение звукового файла по завершении обратного отсчета
subprocess.Popen(['start', 'alarm.wav'], shell=True)
