# ran on july 10th 10:32 ET

# ran again on july 20th 9:50 am.

# and again july 24th 10:00pm et.

import subprocess
import time
import os

targets = [
    "hillaryclinton",
    "realdonaldtrump",
    "SenBillNelson",
    "dickdurbin",
    "BillPascrell",
    "DannyDavis",
    "congbillposey",
    "Brady",
    "Rohrabacher",
    "_Hunter",
    "WarrenDavidson",
    "BetoORourke",
    "MikeCapuano",
    "RandPaul",
    "ChrisMurphyCT",
    "JohnCornyn",
    "robportman",
    "tedcruz",
    "CoryBooker",
    "SusanWBrooks",
    "SteveScalise",
    "reppittenger",
    "sethmoulton",
    "cathymcmorris",
    "repSinema",
    "repMikeQuigley",
    "repBrianHiggins",
    "JimLangevin",
    "repKinzinger",
    "repWilson",
    "repSwalwell",
    "claudiatenney",
    "DonaldNorcross",
    "repdinatitus",
    "repMcGovern",
    "justinamash",
    "JoaquinCastrotx",
    "WhipHoyer",
    "repByrne",
    "repDwightEvans",
    "davidcicilline",
    "LaMalfa",
    "ScottPeters"
]

targets = [
    "JoaquinCastrotx",
    "davidcicilline",
    "LaMalfa",
    "Rohrabacher",
    "_Hunter",
    "BetoORourke"
]


wd = os.path.abspath(os.curdir)
for t in targets:
    resp = 1
    i = 1
    d = os.path.join(wd, t)
    try:
        os.mkdir(d)
    except FileExistsError:
        pass
    while resp != 0:
        resp = subprocess.run("cd " + d + ";\npython3 ../scrape.py " + t + ";\npython3 ../get_metadata.py",
                              shell=True).returncode
        if resp != 0:
            print("Failed with user " + t + ". Restarting user for the " + str(i) + "th time.")
            time.sleep(15)
            i += 1
