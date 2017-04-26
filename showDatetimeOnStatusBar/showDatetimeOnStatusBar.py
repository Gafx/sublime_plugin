import sublime
import sublime_plugin
import datetime
import time
import threading


class ShowDatetime(sublime_plugin.EventListener):

    timer = {}

    def __set_timer(self, view):
        self.timer[view.id()] = True
        while self.timer[view.id()]:
            current_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y/%m/%d %H:%M:%S')
            view.set_status('acurrent_time', current_time)
            time.sleep(1)

    def on_activated_async(self, view):
        if not self.timer.get(view.id(), False):
            t = threading.Thread(target=self.__set_timer, name='timer' + str(view.id()), args=(view,))
            t.start()

    def on_deactivated_async(self, view):
        self.timer[view.id()] = False
