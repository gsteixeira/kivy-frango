from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os
import json


class MannedScreen(Screen):
    def __init__(self, screen_manager=None, last_window=None, **kwargs):
        self.screen_manager = screen_manager
        self.last_window = last_window
        if self.template:
            Builder.load_file(self.template)
        super(MannedScreen, self).__init__(**kwargs)

    def on_leave (self):
        self.screen_manager.remove_widget(self)
        Builder.unload_file(self.template)
        
    def goto_screen(self, ScreenObject, direction='right'):
        window = ScreenObject(screen_manager=self.screen_manager,
                                last_window=self)
        self.screen_manager.add_widget( window )
        self.screen_manager.transition.direction = direction
        self.screen_manager.current = window.name

class ConfigStorage ():
    _filename = ''
    _data = {}
    def __init__(self,
                 filename='../databases/var/etc/config.conf',
                 default_data={}):
        
        self._default_data = default_data
        self._filename = filename
        self._load()
    
    #def __del__(self):
        #print "destruindo conf"
        #self._dump()
        
    def setdata (self, field, value):
        # retorna se o campo existia ou nao. Pra que? Nao sei!
        e = (field in self._data.keys())
        self._data[field] = value
        self._dump()
        return e
    
    def getdata (self, field):
        if field in self._data.keys():
            return self._data[field]
        else:
            return None
    
    def set_defaults (self):
        self._data = self._default_data
        self._dump()
    
    def _dump (self):
        f = open (self._filename, 'w')
        # TODO: encrypt
        f.write ( json.dumps(self._data, sort_keys=True, indent=4) )
        f.close()
        
    def _load (self):
        directory = '../databases/var/etc/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.isfile(self._filename):
            self.set_defaults()
        f = open (self._filename, 'r')
        txt = f.read()
        f.close()
        # TODO: decrypt
        try:
            self._data = json.loads (txt)
            return True
        except:
            return False
        
        
