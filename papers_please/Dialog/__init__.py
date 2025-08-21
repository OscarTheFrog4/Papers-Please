import random
import utils
from utils import wait




# Dialog
class Dialog:
    def __init__(self, f_name, l_name, planet, has_dis, purpose, duration, day, event_occurred, loop, nexa, verdict):
        self.f_name = f_name
        self.l_name = l_name
        self.planet = planet
        self.has_dis = has_dis
        self.purpose = purpose
        self.duration = duration
        self.day = day
        self.event_occurred = event_occurred
        self.loop = loop
        self.nexa = nexa
        self.verdict = verdict
        self.fake_info = ""

