# ran on july 10th 10:32 ET

import os
import subprocess

targets = [
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
    "hillaryclinton",
    "realdonaldtrump",
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

for t in targets:
    subprocess.run("python3 scrape.py " + t, shell= True)