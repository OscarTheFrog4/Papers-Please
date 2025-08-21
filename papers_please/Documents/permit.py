from Documents import Documents
from utils import wait, stutter
import random
class Permit(Documents):

    def print(self):

        stutter()


        # Header
        print(f" ︵ ︵ ︵ ︵ ︵ ︵ ︵ ︵ ︵ ︵ ︵ ")
        print(f"(        ASTRAL PERMIT        )")
        print(f"(                             )")

        # Name
        print(f"(         ᴇɴᴛɪᴛʟᴇᴅ ᴛᴏ         )")
        print(f"({self.f_name.upper() + ' ' + self.l_name.upper():^29})")
        print(f"({'‾' * (len(self.f_name + self.l_name) + 3):^29})")
        print(f"(                             )")

        # Planet
        print(f"(       ᴠᴀʟɪᴅᴀᴛᴇᴅ ғʀᴏᴍ        )")
        print(f"({self.planet.upper():^29})")
        print(f"({'‾' * (len(self.planet) + 2):^29})")
        print(f"(                             )")

        # Duration of Stay and Purpose
        print(f"( ᴅᴜʀᴀᴛɪᴏɴ {self.duration:>18} )")
        print(f"( ─────────────────────────── )")
        print(f"( ᴘᴜʀᴘᴏsᴇ {self.purpose:>19} )")
        print(f" ︶ ︶ ︶ ︶ ︶ ︶ ︶ ︶ ︶ ︶ ︶")

        return self.has_dis
