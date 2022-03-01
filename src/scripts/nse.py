from collections import namedtuple
from datetime import datetime, timedelta, date
import pandas as pd
import re
import requests


def fetch_index(indexType):
    url = "https://www1.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp?"
    headers = {'user-agent': 'Mozilla/5.0'}
    to_date = date.today()
    from_date = to_date - timedelta(days=364)

    Data = namedtuple(
        "Data", ["Date", "Open", "High", "Low", "Close", "Turnover"])
    data = []

    while True:
        params = {
            'indexType': indexType,
            'toDate': to_date.strftime("%d-%m-%Y"),
            'fromDate': from_date.strftime("%d-%m-%Y")
        }

        r = requests.get(url, params=params, headers=headers)
        regex = re.compile("<div id=\\'csvContentDiv.*>(.*):</div>", re.MULTILINE)
        match = regex.findall(r.text)

        if len(match) == 0:
            break

        rows = match[0].replace('"', '').split(":")[1:]

        for row in rows:
            values = [value.strip() for value in row.split(",")]
            dt = datetime.strptime(values[0], "%d-%b-%Y")
            c = float(values[4])
            o = None if values[1] == "-" else float(values[1])
            h = None if values[2] == "-" else float(values[2])
            l = None if values[3] == "-" else float(values[3])
            t = None if values[6] == "-" else float(values[6])
            data.append(Data(Date=dt, Open=o, High=h, Low=l, Close=c, Turnover=t))

        to_date = to_date - timedelta(days=365)
        from_date = from_date - timedelta(days=365)
        
    df = pd.DataFrame(data)
    df = df.sort_values(by='Date').reset_index(drop=True)

    return df