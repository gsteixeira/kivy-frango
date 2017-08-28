

TEMPLATE_MAIN = '''# -*- coding: utf-8 -*-
import os
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
kivy.require('1.9.0')
os.environ.setdefault("FRANGO_SETTINGS_MODULE", "settings")
# TODO frango
from frango.conf import settings
from frango.models import create_tables

from {{app_name}}.views import SampleScreen

__version__ = settings.VERSION

class MainApp(App):
    title = settings.TITLE
    def build(self):
        sm = ScreenManager()
        screen = SampleScreen(screen_manager=sm)
        sm.add_widget(screen)
        sm.current = screen.name
        return sm
    
    def on_pause (self):
        return False

if __name__ == '__main__':
    # create databases
    create_tables()
    MainApp().run()
'''

TEMPLATE_VIEWS = '''# -*- coding: utf-8 -*-
# create your views here
from frango.utils import MannedScreen
from kivy.properties import StringProperty

class SampleScreen(MannedScreen):
    # This is just a sample
    template = StringProperty('{{app_name}}/templates/sample.kv')
    name = StringProperty('sample_screen')
    
    def do_something(self):
        self.ids.tx_label.text = 'I said Hello World!'
'''

SAMPLE_KV = '''# -*- coding: utf-8 -*-
<SampleScreen>:
    BoxLayout:
        id: sample_screen
        orientation:'vertical'
        Label:
            id: tx_label
            text: 'Hello World'
        Button:
            id: butt_something
            text: 'Do something'
            on_release: root.do_something()
'''

TEMPLATE_MODELS = '''# -*- coding: utf-8 -*-
# create your models here
import peewee
from frango.models import Model

class Stuff (Model):
    # This is just a sample
    name = peewee.TextField (null=True)
    last_updt = peewee.DateTimeField (null=True)
    
    def save(self, *args, **kwargs):
        self.last_updt = datetime.now()
        return super(Stuff, self).save(*args, **kwargs)
'''

TEMPLATE_SETTINGS = '''VERSION = '0.0.1'
TITLE = '{{app_name}}'

DB_FILE='../databases/var/db/sqlite.db' 

INSTALLED_APPS = (
    u'{{app_name}}',
    )
    
DEBUG = True
'''
