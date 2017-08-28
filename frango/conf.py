
import os
import importlib

ENVIRONMENT_VARIABLE = 'FRANGO_SETTINGS_MODULE'

class Settings():
    def __init__(self, settings_module):
        #settings_module = os.environ.get(ENVIRONMENT_VARIABLE)
        if not settings_module:
            desc = ("setting %s" % name) if name else "settings"
            raise ImproperlyConfigured(
                "Requested %s, but settings are not configured. "
                "You must either define the environment variable %s "
                "or call settings.configure() before accessing settings."
                % (desc, ENVIRONMENT_VARIABLE))

        # store the settings module in case someone later cares
        self.SETTINGS_MODULE = settings_module

        mod = importlib.import_module(self.SETTINGS_MODULE)

        tuple_settings = (
            "INSTALLED_APPS",
        )
        self._explicit_settings = set()
        for setting in dir(mod):
            #print "lendo setting ", setting
            if setting.isupper():
                setting_value = getattr(mod, setting)

                if (setting in tuple_settings and
                        not isinstance(setting_value, (list, tuple))):
                    raise ImproperlyConfigured("The %s setting must be a list or a tuple. " % setting)
                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)


    def is_overridden(self, setting):
        return setting in self._explicit_settings

    def __repr__(self):
        return '<%(cls)s "%(settings_module)s">' % {
            'cls': self.__class__.__name__,
            'settings_module': self.SETTINGS_MODULE,
        }


settings = Settings(os.environ.get(ENVIRONMENT_VARIABLE))
