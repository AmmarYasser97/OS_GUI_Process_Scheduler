import plotly.figure_factory as ff
import plotly.offline
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
# from gui import new_schedule
# import gui
import bs4


def gantt(df, parent_window):
    fig = ff.create_gantt(df[0], index_col='Resource',
                          group_tasks=True, showgrid_x=True, showgrid_y=True, show_colorbar=True)
    fig['layout']['xaxis'].update({'type': '-'})
    plotly.offline.plot(fig, filename='schedule.html', auto_open=False)

    # load the file
    with open("schedule.html") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt, "lxml")

    # create new h3
    h3 = soup.new_tag(
        "h3", style="font-family:Courier New; width:50%; margin:auto;")
    h3.string = u'Average Waiting Time = ' + str(df[1])
    # insert it into the document
    soup.body.append(h3)

    # save the file again
    with open("schedule.html", "w") as outf:
        outf.write(str(soup))

    web = GanttView(parent_window)
    web.resize(1000, 700)
    file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "schedule.html"))
    web.load(QUrl.fromLocalFile(file_path))

    return web


class GanttView(QWebEngineView):
    def __init__(self, main):
        super(GanttView, self).__init__()
        self.main_window = main

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Message', "New Scheduling?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.main_window.new_schedule()

        event.accept()
            
