import random
import utils
import string

class ApplicantInfo:
    def __init__(self, day, loop, event_occurred):

        self.day = day
        self.loop = loop
        self.event_occurred = event_occurred


        # Establishing Applicant Information
        self.planet = random.choice(utils.planets)
        self.l_name = random.choice(utils.l_names)
        self.sex = random.choice(["M", "F"])
        self.has_dis = False

        self.dob = f"{random.choice(utils.months)} {random.randint(1, 28)}, {random.randint(2910, 2970)}"
        self.exp = f"{random.choice(utils.months)} {random.randint(1, 28)}, {random.randint(2990, 3010)}"

        if self.sex == "M":
            self.f_name = random.choice(utils.b_names)
        else:
            self.f_name = random.choice(utils.g_names)

        self.pass_num = ""
        for char in range(11):
            self.pass_num += random.choice(list(string.ascii_uppercase + string.digits))
        self.pass_num = self.pass_num[0:5] + "-" + self.pass_num[6:11]


        self.purpose = random.choice(utils.reasons)
        match self.purpose:
            case "Asylum":
                self.duration = random.choice(("12 months", "Forever", "9 months"))
            case "Visiting Persons":
                self.duration = random.choice(("1 week", "2 weeks", "3 weeks", "4 weeks"))
            case "Immigration":
                self.duration = "Forever"
            case "Tourism":
                self.duration = random.choice(("4 days", "1 week", "2 weeks", "3 weeks"))

        match self.day:
            case 1:
                if random.choice([True, False]):
                    self.planet = random.choice(utils.planets)
                    if self.planet != "Nexus Harbor":
                        self.has_dis = True
                        if loop > 1 and not event_occurred:
                            self.event_occurred = "go ahead"
                else:
                    self.planet = "Nexus Harbor"

            case 2:
                if self.loop > 2 and not event_occurred:
                    self.event_occurred = "go ahead"

            case 5:
                if self.loop > 2 and not event_occurred:
                    self.f_name = "Robert"
                    self.l_name = "Grant"
                    self.planet = "Velorum"
                    self.event_occurred = "go ahead"

            case 6:
                if self.loop > 2 and not event_occurred:
                    self.event_occurred = "go ahead"