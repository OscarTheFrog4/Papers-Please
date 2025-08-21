from utils import wait
from pathlib import Path


class Notice:
    def __init__(self, day):
        self.day = day

    def print(self):

        # Header
        base_dir = Path(__file__).parent
        header_template = (base_dir / "notices" / "header.txt").read_text()
        header = header_template.format(date=str(self.day + 5) + ", 2989")
        print(header)

        match self.day:
            case 1:
                print("│ Welcome to your new postion  │")
                print("│ as a document insector. You  │")
                print("│ are to identify any          │")
                print("│ discrepancies in the dialog  │")
                print("│ or documents of applicants   │")
                print("│ as to sift out possible AI   │")
                print("│ androids know as the         │")
                print("│ Khaosynths. Today, deny all  │")
                print("│ passports from other plants  │")
                print("│ who are not from the Nexus   │")
                print("│ Harbor.                      │")
                print("└──────────────────────────────┘")
                input("(Enter anything to continue): ")
                wait(0, 1)
                print("* Evaluating Applicants *")
                print("Applicants will show you their documents and provide information")
                print("through dialog. If you detect any discrepancies between documents")
                print("or dialog, deny the applicant. If the applicant doesn't have any")
                print("inconsistencies at all, accept the applicant. If your verdict is")
                print("incorrect, you will receive a citation.")

            case 2:
                print("│ Congratulations on           │")
                print("│ completing your first day as │")
                print("│ an inspector. Foreign        │")
                print("│ stellapasses have been       │")
                print("│ verified. Accept foreigners  │")
                print("│ so long as there are no      │")
                print("│ discrepancies in the         │")
                print("│ information they present.    │")
                print("└──────────────────────────────┘")


            case 3:
                print("│ Good morning. As a futher    │")
                print("│ security measure, starting    ")
                print("│ today and forever on, all    │")
                print("│ foreigners require a valid   │")
                print("│ astral permit. Native        │")
                print("│ applicants do not require an │")
                print("│ astral permit.               │")
                print("└──────────────────────────────┘")
                input("(Enter anything to continue): ")
                wait(0, 1)
                print("* Astral Permits *")
                print("All foreign applicants need to have a valid Astral Permit. If a")
                print("foreign applicant does not have an Astral Permit, they are to be")
                print("denied.")

            case 4:
                print("│ I deliver this note with     │")
                print("│ great distress. The          │")
                print("│ Khaosynths have developed    │")
                print("│ stellapass forgeries nearly  │")
                print("│ identical to Nexan Harbor    │")
                print("│ issues. Because of this,     │")
                print("│ citizens from the Nexus      │")
                print("│ harbor are now required to   │")
                print("│ show their PDAs upon         │")
                print("│ inspection.                  │")
                print("└──────────────────────────────┘")
                input("(Enter anything to continue): ")
                wait(0, 1)
                print("* PDAs *")
                print("All native applicants need to have a valid PDA. If an applicant")
                print("from the Nexus Harbor does not have an Astral Permit, they are to")
                print("be denied.")

            case 5:
                print("│ Today, an important diplomat │")
                print("│ is coming through the Nexus  │")
                print("│ Harbor to provide important  │")
                print("│ information about the        │")
                print("│ Khaosynths. The name of this │")
                print("│ diplomatic is Robert Grant.  │")
                print("│ Let him through no matter    │")
                print("│ what, even if you receive a  │")
                print("│ citation for doing so.       │")
                print("└──────────────────────────────┘")

            case 6:
                print("│ Rumors from nearby planets   │")
                print("│ say that the Khaosynths are  │")
                print("│ developing strong offensive  │")
                print("│ technologies. It is unknown  │")
                print("│ to us how strong they may    │")
                print("│ be, so remain on your        │")
                print("│ highest guard.               │")
                print("└──────────────────────────────┘")

            case 7:
                print("│ Yesterday's incident has     │")
                print("│ gotten the attention of even │")
                print("│ the Nexus Harbor's planetary │")
                print("│ government. Generously, they │")
                print("│ have assigned you a full on  │")
                print("│ personal Nexan Defender. We  │")
                print("│ are lucky that the Nexan     │")
                print("│ government provided you with │")
                print("│ such a valuable and powerful │")
                print("│ asset. Hence, I expect you   │")
                print("│ hold this gift in the        │")
                print("│ highest level of respect.    │")
                print("└──────────────────────────────┘")

            case 8:
                body = (base_dir / "notices" / "body_8.txt").read_text()
                print(body)
                input("(Enter anything to continue): ")
                wait(0, 1)
                print("* Lacing Passports *")
                print("Applicants who have forged documents or have inconsistencies in")
                print("their dialog can be laced. Applicants with forged documents like")
                print("this can also be denied, but you will recieve a bonus nexa for")
                print("lacing instead. Some applicants can have invalid documents yet are")
                print("not to be laced. Only lace applicants who have lied or forged")
                print("documents; people who are missing papers or have expired documents")
                print("do not necessarily need to be laced.")

            case 9:
                print("│  │")
                print("│  │")
                print("│  │")
                print("│  │")
                print("│  │")
                print("│  │")
                print("│  │")
                print("└──────────────────────────────┘")

            case 10:
                print("│  │")
                print("│  │")
                print("│  │")
                print("│  │")
                print("│  │")
                print("│  │")
                print("│  │")
                print("└──────────────────────────────┘")

        input("(Enter anything to continue): ")
        wait(0, 30)