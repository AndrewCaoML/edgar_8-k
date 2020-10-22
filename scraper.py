import requests
import re
import gspread
from bs4 import BeautifulSoup as bs
from oauth2client.service_account import ServiceAccountCredentials
from colorama import init
from colorama import Fore, Back, Style

init()

sheet = client.open('Database').worksheet("BIOTECHs")
all_comps = sheet.col_values(1)
all_comps.remove('Active Biotechs')

imported_companies = client.open('Trial Database').worksheet("Historical")
imports = imported_companies.col_values(1)

imported_trials = client.open('Trial Database').worksheet("Drugs/Conditions")
trial_comps = imported_trials.col_values(1)
trial_conds = imported_trials.col_values(3)
trial_drugs = imported_trials.col_values(4)

already_removed = []
final_comps = all_comps.copy()

letters = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print(Fore.GREEN + "STARTING...")
print(Style.RESET_ALL)
