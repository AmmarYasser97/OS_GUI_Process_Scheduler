import plotly.figure_factory as ff
import plotly.offline

import sys
import os

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication


def gantt(df):
    fig = ff.create_gantt(df, group_tasks=True)
    fig['layout']['xaxis'].update({'type': '-'})
    plotly.offline.plot(fig, filename='schedule.html', auto_open=False)

    web = QWebEngineView()
    web.resize
    web.resize(web.minimumSizeHint())
    file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "schedule.html"))
    web.load(QUrl.fromLocalFile(file_path))
    return web
