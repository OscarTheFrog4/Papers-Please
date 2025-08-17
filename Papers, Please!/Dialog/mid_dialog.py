from Dialog import Dialog
from utils import wait, dialog
import utils
import random

class MidDialog(Dialog):

    @staticmethod
    def print_purpose(category, dia_options, fake_info, purpose):
        if category == purpose and not fake_info or fake_info == category:
            print(f"<< '{random.choice(dia_options)}'")

    def interrogate(self):

        wait(1.5, 2)

        if self.f_name == "Robert":
            dialog("inspector", "Purpose of visit?")
            wait(1.5, 0)
            dialog("applicant", "I was called for diplomatic purposes.")
            wait(1.5, 0)
            dialog("inspector", "Duration of stay?")
            wait(1.5, 0)
            dialog("applicant", "However long the discussions last.")

        # Ask for Name
        elif self.day <= 2 or self.planet == "Nexus Harbor":

            print(f"{"'Name?' >>":>70}")
            wait(1, 0)
            # Chance of responding with a fake first name
            if random.randint(1, 10) == 1:
                fake_info = self.f_name
                while fake_info == self.f_name:
                    if self.f_name in utils.b_names:
                        fake_info = random.choice(utils.b_names)
                    if self.f_name in utils.g_names:
                        fake_info = random.choice(utils.g_names)
                print(f"<< '{fake_info} ", end="")
                self.has_dis = "forgery"

            # Real First Name
            else:
                print(f"<< '{self.f_name} ", end="")

            # Chance of responding with a fake last name
            if random.randint(1, 10) == 1:
                fake_info = self.l_name
                while fake_info == self.l_name:
                    fake_info = random.choice(utils.l_names)
                print(f"{self.l_name}'")
                self.has_dis = forgery

            # Real last name
            else:
                print(f"{self.l_name}'")


        # Ask for purpose and duration of stay
        else:

            # Ask for purpose of visit
            dialog("inspector", "Purpose of visit?")
            wait(1.5, 0)

            # Chance of Responding With a Fake Purpose
            self.fake_info = None
            if random.randint(1, 10) == 1:
                self.fake_info = self.purpose
                while self.fake_info == self.purpose:
                    self.fake_info = random.choice(utils.reasons)
                self.has_dis = "forgery"

            # Natural dialog
            self.print_purpose("Asylum", ["I am seeking refuge", "Protection from the androids", "Asylum"], self.fake_info, self.purpose)
            self.print_purpose("Visiting Persons", ["Visiting relatives", "Visiting friends", "Visiting people"], self.fake_info, self.purpose)
            self.print_purpose("Immigration", ["Immigration", "I am immigrating", "I am going to live here"], self.fake_info, self.purpose)
            self.print_purpose("Tourism", ["Tourism", "I am a tourist", "Touring the Nexus Harbor alone"], self.fake_info, self.purpose)

            # Ask for Duration of Stay
            wait(1.5, 0)
            print(f"{"'Duration of stay?' >>":>70}")  # 50 spaces
            wait(1.5, 0)

            # Flavor text in duration response
            if not self.duration == "Immigration" and not self.fake_info == "Immigration":
                print(f"<< '{random.choice(["", "", "About ", "Around ", "Uh, like "])}", end="")
            else:
                print(f"<< '", end="")

            # Chance of Responding With a Fake Duration
            if random.randint(1, 10) == 1:
                fake_info = random.choice(utils.durations)
                while fake_info == self.duration:
                    fake_info = random.choice(utils.durations)
                print(f"{fake_info}'")
                self.has_dis = "forgery"

            # Real Duration
            else:
                print(f"{self.duration}'")

        return self.has_dis, self.event_occurred

    def event(self):
        match self.day:
            case 2:
                # Person begging to be let through
                if self.event_occurred == "go ahead" and self.has_dis:
                    wait(2, 1)
                    print(f"{"'There is a discrepancy here' >>":>70}")
                    wait(2, 0)
                    print("<< 'Look, I know my papers are out of order'")
                    wait(2, 0)
                    print("<< 'I couldn't get them to update my name in time'")
                    wait(2, 0)
                    print("<< 'But my son is alone across the border'")
                    wait(2, 0)
                    print("<< 'Please. I am begging you. I am not an android'")
                    wait(2, 0)
                    self.event_occurred = True

        return self.has_dis, self.event_occurred