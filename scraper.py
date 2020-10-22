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

