import requests
from bs4 import BeautifulSoup

timetable_urls = {
    0: "http://www.solak-bus.pl/rozklad_jazdy/index/brzesko_tarnow.html",
    1: "http://www.solak-bus.pl/rozklad_jazdy/index/tarnow_brzesko.html",
    2: "https://www.jakubas.com.pl/rozklad-jazdy-2/"
}

timetable_disc = {
    # Brzesko - Tarnów
    0: {
        0: '',
        1: '',
        2: '',
        3: ''
    },
    # Tarnów - Brzesko
    1: {
        0: '',
        1: '',
        2: '',
        3: ''
    },
}


def get_timetable_solak():
    for y in range(2):
        content_solak = requests.get(timetable_urls[y])
        soup = BeautifulSoup(content_solak.text, 'html.parser')
        timetable_solak = soup.find_all("table")
        for x in range(len(timetable_solak)):
            timetable_row = timetable_solak[x].find_all('tr')
            timetable_data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in timetable_row]

            data = [[u"".join(d).strip() for d in l] for l in timetable_data]
            flat_data = list(filter(None, [item for sublist in data for item in sublist]))
            timetable_disc[y][x] = flat_data
    return timetable_disc


def get_val():
    return None
