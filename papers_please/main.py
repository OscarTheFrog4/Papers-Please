import time

from Dialog import *
from Dialog.mid_dialog import MidDialog
from Dialog.post_dialog import PostDialog
from Dialog.pre_dialog import PreDialog
from Documents.passport import Passport
from Documents.pda import PDA
from Documents.permit import Permit
from OtherClasses.applicant_info import ApplicantInfo
from OtherClasses.day import Day
from OtherClasses.decision import Decision
from OtherClasses.notice import Notice


def main():

    # Establish non-personal variables
    day = 8
    nexa = 0
    old_nexa = 0
    food = 3
    heat = 3
    loop = 1
    citations = 0
    is_running = True
    event_occurred = False
    verdict = None

    # Print Daily Notice
    Notice(day).print()

    start_time = time.time()

    while is_running:


        # Establish Applicant Information
        get_info = ApplicantInfo(day, loop, event_occurred)
        f_name = get_info.f_name
        l_name = get_info.l_name
        planet = get_info.planet

        sex = get_info.sex
        dob = get_info.dob
        exp = get_info.exp
        pass_num = get_info.pass_num

        purpose = get_info.purpose
        duration = get_info.duration

        event_occurred = get_info.event_occurred

        has_dis = get_info.has_dis


        # Dialog before documents
        event_occurred = PreDialog(f_name, l_name, planet, has_dis, purpose, duration, day, event_occurred, loop, nexa, verdict).event()

        if event_occurred == "dead":
            event_occurred = False

            # Daily Notice
            Notice(day).print()
            start_time = time.time()
            nexa = old_nexa

            wait(0, 30)
            loop = 1
            continue

        elif event_occurred == "continue":
            event_occurred = False
            wait(0, 30)
            loop += 1
            continue

        # Print passport
        has_dis = Passport(f_name, l_name, planet, dob, exp, sex, pass_num, has_dis, purpose, duration, day, event_occurred).print()

        # Chance of applicant missing entry permit
        if day >= 3 and not planet == "Nexus Harbor":
            if random.randint(1, 10) == 1 or f_name == "Robert":
                has_dis = True
            else:
                has_dis = Permit(f_name, l_name, planet, dob, exp, sex, pass_num, has_dis, purpose, duration, day, event_occurred).print()

        # Chance of applicant missing PDA
        if day >= 4 and planet == "Nexus Harbor":
            if random.randint(1, 10) == 1:
                has_dis = True
            else:
                has_dis = PDA(f_name, l_name, planet, dob, exp, sex, pass_num, has_dis, purpose, duration, day, event_occurred).print()

        # Dialog after documents are presented, but before user enters a verdict

        has_dis, event_occurred = MidDialog(f_name, l_name, planet, has_dis, purpose, duration, day, event_occurred, loop, nexa, verdict).interrogate()
        has_dis, event_occurred = MidDialog(f_name, l_name, planet, has_dis, purpose, duration, day, event_occurred, loop, nexa, verdict).event()
        # Decision
        nexa, verdict, citations = Decision(has_dis, nexa, day, loop, planet, event_occurred, citations).decide()

        # Dialog after the player enters their verdict
        event_occurred = PostDialog(f_name, l_name, planet, has_dis, purpose, duration, day, event_occurred, loop, nexa, verdict).remark()


        # Daily Evaluation
        loop += 1
        if time.time() - start_time > 30:

            nexa, food, heat, is_running = Day(nexa, is_running, food, heat).evaluate_day()

            # Reset Day
            event_occurred = False
            day += 1
            old_nexa = nexa
            loop = 1

            # Daily Notice
            Notice(day).print()

            start_time = time.time()

if __name__ == "__main__":
    main()