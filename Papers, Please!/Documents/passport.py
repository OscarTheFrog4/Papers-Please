from Documents import Documents
import random, string
import utils
from utils import wait

# Passport
class Passport(Documents):

    def print(self):

        wait(1.5, 0)

        # Header
        print("┌──────────────────────────────────┐ ")
        print("│            STELLAPASS            │ ")
        print("│                                  │ ")

        # Chance for Wrong First Name
        if random.randint(1, 10) == 1 and not self.f_name == "Robert":
            fake_info = self.f_name
            while fake_info == self.f_name:
                if self.f_name in utils.b_names:
                    fake_info = random.choice(utils.b_names)
                else:
                    fake_info = random.choice(utils.g_names)
            print(f"│ {self.l_name + ', ' + fake_info:32} │")
            self.has_dis = "forgery"

        # Chance for Wrong Last Name
        elif random.randint(1, 10) == 1 and not self.f_name == "Robert":
            fake_info = self.l_name
            while fake_info == self.l_name:
                fake_info = random.choice(utils.l_names)
            print(f"│ {fake_info + ', ' + self.f_name:32} │")
            self.has_dis = "forgery"

        # Correct Full Name
        else:
            print(f"│ {self.l_name + ', ' + self.f_name:32} │")

        # Other Passport Information
        print(f"{'│':35}│")
        print(f"│ [DOB] {self.dob:27}│")
        print(f"│ [EXP] {self.exp:27}│")

        # Chance for wrong sex
        if random.randint(1, 10) == 1 and self.day >= 3:
            if self.sex == "M":
                self.fake_info = "F"
            else:
                self.fake_info = "M"
            print(f"│ [SEX] {self.fake_info:27}│")
            self.has_dis = "forgery"

        # Correct sex
        else:
            print(f"│ [SEX] {self.sex:27}│")

        print(f"{"│":35}│")

        # Chance for wrong planet
        if random.randint(1, 10) == 1 and day >= 3:
            fake_info = self.planet
            while fake_info == self.planet:
                fake_info = random.choice(utils.planets)
            print(f"│ {fake_info:20} ", end="")
            self.has_dis = "forgery"

        # Correct planet
        else:
            print(f"│ {self.planet:20} ", end="")

        # Chance for wrong passport number
        if random.randint(1, 10) == 1 and self.planet == "Nexus Harbor" and self.day >= 4:
            self.fake_info = self.pass_num
            while self.fake_info == self.pass_num:
                self.fake_info = ""
                for char in range(11):
                    self.fake_info += random.choice(list(string.ascii_uppercase + string.digits))
                self.fake_info = self.fake_info[0:5] + "-" + self.fake_info[6:11]
            print(f"{self.fake_info:11} │")

            self.has_dis = "forgery"


                # Try importing applicant_info and taking the pass_num attribute


        # Correct passport number
        else:
            print(f"{self.pass_num:11} │")

        print("└──────────────────────────────────┘ ")

        return self.has_dis