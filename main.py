import kivy
from dotenv import dotenv_values
from kivy.app import App
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

from api import Bookworm

kivy.require('2.2.0')


class DepartScreen(MDScreen):
    pass


class FichierScreen(MDScreen):
    def selected(self, filename):
        if filename:
            self.manager.image = filename[0]

            app = App.get_running_app()
            app.root.current = "image"


class ImageScreen(MDScreen):
    def __init__(self, **kwargs):
        super(ImageScreen, self).__init__(**kwargs)
        config = dotenv_values('.env')
        self.bookworm = Bookworm(config["api_url"])

    def get_text(self):
        image_path = self.manager.image
        with open(image_path, mode='rb') as image_file:
            text = self.bookworm.get_text(image_file)
            try:
                texte_extrait = text['description']
                self.manager.texte = texte_extrait
            except:
                self.manager.texte = "\n" + "L'image ne semble pas contenir de texte..."

            app = App.get_running_app()
            app.root.current = "texte"


class TexteScreen(MDScreen):
    def texte_modifie(self):
        self.ids.bouton_copier_texte.text = "Copier le texte"
        self.ids.bouton_copier_texte.icon = "content-copy"

    def bouton_copier(self):
        self.ids.bouton_copier_texte.text = "Le texte a bien été copié"
        self.ids.bouton_copier_texte.icon = "check"


class ImageScreenManager(MDScreenManager):
    image = StringProperty("")
    texte = StringProperty("")

    def ecran_depart(self):
        app = App.get_running_app()
        app.root.current = "depart"


class LocrApp(MDApp):
    def build(self):
        return ImageScreenManager()


if __name__ == '__main__':
    LocrApp().run()
