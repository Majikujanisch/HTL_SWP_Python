import random
import GlobalVars
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

import files
import game

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Play'
            on_press: root.manager.current = 'play'
        Button:
            text: 'Options'
            on_press: root.manager.current = 'options'
        Button:
            text: 'Quit'
            on_press: app.stop()

<PlayScreen>:
    BoxLayout:
        Button:
            text: 'Alleine'
            on_press: root.manager.current = "palone"
        Button:
            text: 'Lokaler Multiplayer (not implemented)'
        Button:
            text: 'Zurück'
            on_press: root.manager.current = 'menu'
<OptionsScreen>:
    BoxLayout:
        Button:
            text: 'Ausgabe gesammelter Daten'
            on_press: root.manager.current = "data"
        Button:
            text: 'Zurück zum Hauptmenü'
            on_press: root.manager.current = 'menu'
            
<OptionsDataView>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "Wins: " + str(root.data1)
        Label:
            text: "Loses: " + str(root.data2)
        Label:
            text: "Draws: " + str(root.data3)
        Label:
            text: "Schere: " + str(root.data4)
        Label:
            text: "Stein: " + str(root.data5)
        Label:
            text: "Papier: " + str(root.data6)
        Label:
            text: "Echse: " + str(root.data7)
        Label:
            text: "Spock: " + str(root.data8)
            
        Button:
            text: "Zurück"
            on_press: root.manager.current = "options"
        
<PlayAloneMenu>:
    BoxLayout:
        Button:
            text:"leicht (mit flask möglich)"
        Button:
            text:"mittel"
            on_press: root.manager.current = "mGame"
        Button:
            text:"schwer (mit flask möglich)"
        Button: 
            text:"zurück"
            on_press:root.manager.current="play"

<SpielMittel>:
    BoxLayout:
        Button:
            text: "Stein"
            on_press:root.setIndex(0)
            on_press:root.manager.current="leer"
            
        Button:
            text: "Papier"
            on_press:root.setIndex(1)
        Button:
            text: "Schere"
            on_press:root.setIndex(2)
        Button:
            text: "Spock"
            on_press:root.setIndex(3)
        Button:
            text: "Echse"
            on_press:root.setIndex(4)
        Button:
            text: "zurück"
            on_press:root.manager.current="palone"
<AusgabeScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: str(root.ausgabe)
        Button:
            text: "Nochmal"
        Button: 
            text: "Zurück zu Schwierigkeitsauswahl"
<LeerScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: "Zum ergebniss:"
            on_press:root.manager.current="ausgabe"

        
            
""")

class MenuScreen(Screen):
    pass

class PlayScreen(Screen):
    pass

class OptionsScreen(Screen):
    pass
class OptionsDataView(Screen):
    bigdata1, bigdata2 = files.dataAuswertung()
    data1, data2, data3 = bigdata1
    data4, data5, data6, data7, data8 = bigdata2

class PlayAloneMenu(Screen):
    pass

class SpielMittel(Screen):
    def setIndex(self, value):
        userinput = value
        compinput = random.randint(0, 4)
        GlobalVars.winstat = game.decidelogic(int(userinput), compinput)

class LeerScreen(Screen):
    def refresh(self):
        pass

class AusgabeScreen(Screen):
    ausgabe = GlobalVars.winstat
    print(ausgabe)
    def on_enter(self, *args):
        self.ausgabe = GlobalVars.winstat

class Sm (ScreenManager):
    def __init__(self):
        pass
class SSP(App):
    scm = ScreenManager()
    def build(self):
        # Create the screen manager

        SSP.scm.add_widget(MenuScreen(name='menu'))
        SSP.scm.add_widget(PlayScreen(name='play'))
        SSP.scm.add_widget(OptionsScreen(name="options"))
        SSP.scm.add_widget(OptionsDataView(name="data"))
        SSP.scm.add_widget(PlayAloneMenu(name="palone"))
        SSP.scm.add_widget(SpielMittel(name="mGame"))
        SSP.scm.add_widget(AusgabeScreen(name="ausgabe"))
        SSP.scm.add_widget(LeerScreen(name="leer"))
        return SSP.scm
    def refreshh(self):
        pass
