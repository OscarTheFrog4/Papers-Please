import time
import random

# Wait Function
def wait(secs=0, lines=0):
    time.sleep(secs)
    for i in range(lines):
        print()


# Tuples
planets = ("Spectra Confederacy", "Cygnus", "Arkonia", "Velorum", "Chargona", "Nexus Harbor",  "Nexus Harbor")
b_names = ("Lazarus", "Saitama")
g_names = ("Clarafina", "Aurora", "Ava")
l_names = ("Valtor", "Charius", "Dairox", "Lendrivax")
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
reasons = ("Asylum", "Visiting Persons", "Immigration", "Tourism")
durations = ("1 week", "2 weeks", "3 months", "6 months")

# Stutter function
def stutter():
    if random.randint(1, 10) == 1:
        wait(1, 2)
        print("<< 'Oops, hold on I've got one more.'")
        wait(2, 3)
    elif random.randint(1, 9) == 1:
        wait(1, 3)
        print("<< 'Hang on.'")
        wait(2, 3)
    elif random.randint(1, 8) == 1:
        wait(1, 3)
        print("<< 'One second please.'")
        wait(2, 3)
    elif random.randint(1, 7) == 1:
        wait(1, 3)
        print("<< 'Lemme just find it here...'")
        wait(2, 3)
    else:
        wait(1, 4)


def dialog(speaker, phrase):

    if speaker == "inspector":
        print(f"{f"'{phrase}' >>":>70}")

    elif speaker == "applicant":
        print(f"<< '{phrase}'")