import sys
import os
import time

class TimeManager:

    def __init__(self, file_path):
        self.file_path = file_path


    def __enter__(self):
        log = []
        start = time.time()
        os.system(self.file_path)
        finish = time.time()
        log.append(start)
        log.append(finish)
        return log


    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

with TimeManager('homeworkfile.py') as log:
    print('Время старта выполнения скрипта - {} '.format (log[0])+ '\nВремя окончания выполнения скрипта - {} '.format (log[1]) + '\nСкрипт выполнился за  - {} '.format (log[1]-log[0]))


