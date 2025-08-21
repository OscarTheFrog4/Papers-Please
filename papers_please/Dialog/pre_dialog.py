from utils import wait, dialog
from Dialog import Dialog

class PreDialog(Dialog):
    def __init__(self, f_name, l_name, planet, has_dis, purpose, duration, day, event_occurred, loop, nexa, verdict):
        super().__init__(f_name, l_name, planet, has_dis, purpose, duration, day, event_occurred, loop, nexa, verdict)

        self.event_occurred = ""
        wait(0, 30)
        wait(2, 0)

        dialog("inspector", "Papers, please")

    def event(self):

        match self.day:
            case 6:
                if self.event_occurred == "go ahead":
                    wait(2, 0)
                    dialog("applicant", "DEATH TO THE HUMANS!!")
                    wait(1, 1)

                    print("   /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\\   ")
                    print("  /  * Detonation Commencing *  \\  ")
                    print(" /                               \\ ")
                    print(" │\033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m│  ")
                    print(" │\033[1;31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m│  ")
                    print(" │\033[1;33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m│  ")
                    print(" │\033[1;34m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m│  ")
                    print(" └───────────────────────────────┘  ")
                    wait(4, 1)

                    dialog("inspector", "What on Velorum?")
                    wait(2, 0)
                    dialog("inspector", "Idiot terrorist.")
                    wait(2, 0)
                    dialog("inspector", "This bomb is pathetic.")
                    wait(2, 0)
                    dialog("inspector", "I thought the Khaosynths were supposed to be smart.")
                    wait(3, 0)
                    dialog("inspector", "Everyone knows you cut the red wire.")
                    wait(2, 1)

                    if input("Which color of wire do you want to cut?: ") == "red":
                        wait(2, 1)
                        print("   /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\\   ")
                        print("  /   * Detonation Disabled *   \\  ")
                        print(" /                               \\ ")
                        print(" │\033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m│  ")
                        print(" │\033[1;31m~~~~~~~~~~~~~~/ \\~~~~~~~~~~~~~~\033[0m│  ")
                        print(" │\033[1;33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m│  ")
                        print(" │\033[1;34m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m│  ")
                        print(" └───────────────────────────────┘  ")
                        wait(2, 0)
                        dialog("inspector", "Good.")
                        wait(2, 0)
                        dialog("inspector", "Glad that stupid bomb was dealt with.")
                        wait(2, 0)
                        dialog("inspector", "Idiot Khaosynths.")

                    else:
                        wait(1, 0)
                        dialog("inspector", "...")
                        wait(2, 0)
                        dialog("inspector", "Are you stupid? Now you're dead, dummy.")
                        wait(3, 0)
                        dialog("inspector", "I guess if you were idiotic enough to pick this option,")
                        dialog("inspector", "you'll have to restart this day.")
                        wait(4, 0)
                        dialog("inspector", "...Idiot.", "scoffs")
                        wait(2, 0)

                    self.event_occurred = "dead"

            case 7:
                if self.loop == 1:
                    wait(1, 0)
                    dialog("applicant", "Hello, inspector. I am the Nexan Defender.")
                    wait(2, 0)
                    dialog("inspector", "Oh. Ha, habit. Hello defender sir.")
                    wait(4, 0)
                    dialog("applicant", "I am much too qualified to be defending a dump like this.")
                    wait(3, 0)
                    dialog("applicant", "But whatever, I believe we will make a solid team.")
                    wait(2, 1)
                    input("(Enter anything to continue): ")
                    self.event_occurred = "continue"
                elif self.loop > 3:
                    wait(2, 0)
                    dialog("applicant", "Talk and you die.")
                    wait(1, 0)
                    print("  __________")
                    print(" /  ___.----'")
                    print("/  ( '")
                    print("`-'")
                    wait(2, 0)
                    dialog("applicant", "Don't try and be a hero.")
                    wait(3, 0)
                    dialog("inspector", "lol I'm not the one that has to be a hero.")
                    wait(4, 0)
                    dialog("applicant", "Wait, what do you mea-")
                    wait(3, 0)
                    dialog("applicant", "* pretend these are laser gun noises *")
                    wait(3, 0)
                    dialog("inspector", "Thank you, defender. Thank you.")
                    wait(2, 0)
                    dialog("applicant", "Just doing my job, inspector.")
                    wait(2, 0)
                    dialog("inspector", "And defender, one more thing.")
                    wait(3, 0)
                    dialog("inspector", "What is your name?")
                    wait(3, 0)
                    dialog("applicant", "Wh- what do you mean I don't have a-")
                    wait(4, 0)
                    dialog("applicant", "Or, my name is Teddy.")
                    wait(3, 0)
                    dialog("inspector", "My name is ______ (say your name out loud,")
                    dialog("inspector", "it is voice activated)")
                    wait(15, 1)
                    dialog("inspector", "Lol now you look like an idiot yelling at the laptop.")
                    self.event_occurred = "continue"
                    input("(Enter anything to continue): ")


        return self.event_occurred