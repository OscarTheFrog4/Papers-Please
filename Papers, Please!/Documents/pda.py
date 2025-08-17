from Documents import Documents
import random
from utils import wait, stutter
import utils
class PDA(Documents):
    def print(self):

        wait(0.5, 0)
        stutter()
        wait(0.5, 0)

        print(f"   ──────────────────────────────────────")

        #Chance of Fake Name
        if random.randint(1, 5) == 1:
            fake_info = self.f_name
            while fake_info == self.f_name:
                if self.f_name in utils.b_names:
                    fake_info = random.choice(utils.b_names)
                if self.f_name in utils.g_names:
                    fake_info = random.choice(utils.g_names)
            print(f"  /{fake_info + " " + self.l_name + "'s PDA":^34}/‾\\ \\")
            self.has_dis = True

        # Real Name
        else:
            print(f"  /{self.f_name + " " + self.l_name + "'s PDA":^34}/‾\\ \\")
        print(f" /  {"‾" * (len(self.f_name + self.l_name) + 9):^32}/   \\ \\")
        print(f"/                                  /     \\ \\")
        print(f"\\                                  \\     / /")
        print(f" \\                                  \\   / /")

        # Planet and Passport Number
        print(f"  \\ {self.planet:20} {self.pass_num:11} \\_/ /")
        print("   ──────────────────────────────────────")
        return self.has_dis
