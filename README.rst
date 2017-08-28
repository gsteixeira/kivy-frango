=====
kivy-frango
=====

A Framework like Django for Kivy

kivy-frango allows you to build kivy apps in a fashion similar to Django Framework.

-----------------------
To create a new project::

        frango-admin startproject myproject
        cd myproject
        python main.py
            
This will create a directory structure much similar to django's.
You'll find Screens in the views.py file
KV templates are stored in a templates/ directory


-----------------------
To create a new app inside project::

        # inside project directory
        frango-admin startapp myapp
            
This will create all the app necessary file structure, with a small sample in it.


-----------------------
kivy-frango uses peewee's orm.
You can declare your models in the file myapp/models.py like this::
            
        import peewee
        from frango.models import Model

        class Stuff (Model):
            # This is just a sample
            name = peewee.TextField (null=True)
            last_updt = peewee.DateTimeField (null=True)

Please check peewee documentation for reference on how to use models.

            
-----------------------
To change between Kivy's Screens:

    Consider the screens::
                
        class SampleScreen(MannedScreen):
            # This is just a sample
            template = StringProperty('myapp/templates/sample.kv')
            name = StringProperty('sample_screen')
            
            def goto_another_screen(self):
                self.goto_screen(AnotherScreen)
            
            
        class AnotherScreen(MannedScreen):
            # This is just a sample
            template = StringProperty('otherapp/templates/otherapp.kv')
            name = StringProperty('sample_screen')
            
            def goto_another_screen(self):
                self.goto_screen(SampleScreen, direction='left')

                
    Frango takes care of managing of Kivy screens and loading or unloading 
    KV files when necessary
    

