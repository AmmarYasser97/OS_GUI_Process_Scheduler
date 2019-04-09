import plotly.figure_factory as ff
import plotly.offline
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import bs4


def gantt(df):
    fig = ff.create_gantt(df[0], index_col='Task', group_tasks=True, showgrid_x=True, showgrid_y=True)
    fig['layout']['xaxis'].update({'type': '-'})
    plotly.offline.plot(fig, filename='schedule.html', auto_open=False)

    # load the file
    with open("schedule.html") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt, "lxml")

    # create new h3
    h3 = soup.new_tag("h3", style="font-family:Courier New; width:50%; margin:auto;")
    h3.string = u'Average Waiting Time = ' + str(df[1])
    # insert it into the document
    soup.body.append(h3)

    # save the file again
    with open("schedule.html", "w") as outf:
        outf.write(str(soup))

    web = QWebEngineView()
    web.resize(1000, 700)
    file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "schedule.html"))
    web.load(QUrl.fromLocalFile(file_path))

    return web
