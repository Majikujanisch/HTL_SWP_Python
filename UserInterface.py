from kivy._event import partial
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty, DictProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
import kivyCode
import game
import files
import kivy
import kivymd
kivy.require("2.0.0")
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import Label
from kivymd.uix.screen import Screen
from kivy.lang import Builder
def playAlonemenu():
    print("Welche Schwierigkeit möchtest du?")
    print("l...leicht[ab flask server]")
    print("m...mittel")
    print("s...Schwer[ab flask server]")
    print("b...Zurück zum Menü")
    uinput = input("Wähle eine Möglichkeit")
    uinput = uinput.lower()
    if(uinput == "l"):
        game.game("l")
    elif(uinput == "m"):
        game.game("m")
    elif(uinput == "s"):
        game.game("s")
    elif(uinput == "b"):
        mainmenu()
    else:
        print("FALSCHE EINGABE!")
        playAlonemenu()
def playmenu():
    print("Wie möchtest du spielen?")
    print("a...Alleine")
    print("m...lokaler Multiplayer")
    print("b...Zurück zum Menü")
    uinput = input("Wähle eine Möglichkeit: ")
    uinput = uinput.lower()
    if(uinput == "a"):
        playAlonemenu()
    elif(uinput == "m"):
        game.playmulti()
    elif(uinput == "b"):
        mainmenu()
    else:
        print("FALSCHE EINGABE!")
        playmenu()
def optionmenu():
    print("w...Ausgabe der gesammelten Daten")
    print("e...mainmenu")
    uinput = input("Wähle eine Möglichkeit")
    uinput = uinput.lower()
    if uinput == "e":
        mainmenu()
    elif uinput == "w":
        files.dataAuswertung()
        optionmenu()
    else:
        print("FALSCHE EINGABE!")
        optionmenu()
def mainmenu():

    print("Willkommen bei Schere-Stein-Papier-Echse-Spock")
    print("p...play")
    print("o...options")
    print("e...exit")
    uinput = input("Wähle eine Möglichkeit: ")
    uinput = uinput.lower()
    if uinput == "e":
        kivyCode.SSP().run()
        print("Aufwiedersehen")
    elif uinput == "p":
        playmenu()
    elif uinput == "o":
        optionmenu()
    else:
        print("FALSCHE EINGABE!")
        mainmenu()

#Interface mit Kivy:
class MenuButton(ButtonBehavior, BoxLayout):
    text = StringProperty('')                                                           # stores the button text
    action = StringProperty('')                                                         # stores the button release action
    options = DictProperty({})                                                          # stores menu button text and actions

    def __init__(self, **kwargs):
        super(MenuButton,self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.button = Button(text=self.text, size_hint_y=None, height=32)
        self.add_widget(self.button)
        self.height = self.button.height
        self.bind(on_touch_down=self.create_clock, on_touch_up=self.delete_clock)
        self.m = RelativeLayout()
        self.m.size_hint_y = None
        self.m.height = 0
        self.add_widget(self.m)

    def create_clock(self, widget, touch, *args):
        if self.children[1].collide_point(touch.x, touch.y):
            callback = partial(self.menu, touch)
            Clock.schedule_once(callback, .3)
            touch.ud['event'] = callback


    def delete_clock(self, widget, touch, *args):
        if self.children[1].collide_point(touch.x, touch.y):
            if 'event' in touch.ud:   # avoid non-existent key errors
                Clock.unschedule(touch.ud['event'])
            if self.m.children == []:
                eval(self.action)

    def menu(self, touch, *args):
        menu = BoxLayout(orientation='vertical')
        height_calc  = 0   # calculate the total height needed when the menu is opened
        for text, fun_pass in self.options.iteritems():
            but = Button(id=fun_pass, text=text, height=32, size_hint_y=None)
            height_calc += but.height
            but.bind(on_release=partial(self.close_menu, menu))
            but.bind(on_release=self.call_function)
            menu.add_widget(but)
        close = Button(text='close', height=32, size_hint_y=None)
        height_calc += close.height
        close.bind(on_release=partial(self.close_menu, menu))
        menu.add_widget(close)
        self.m.add_widget(menu)

        # adjust position and height of expanded MenuButton
        self.m.height = height_calc
        self.height = self.button.height + self.m.height
        self.pos = (0, self.orig_y - self.m.height)

        # make sure this MenuButton is drawn on top of any other MenuButtons
        app = App.get_running_app()
        app.root.remove_widget(self)
        app.root.add_widget(self)


    def close_menu(self, widget, *args):                                                # clears all menu widgets from the relative layout
        self.m.clear_widgets()

        # reset height and position of MenuButton when not expanded
        self.m.height = 0
        self.height = self.button.height
        self.pos = (0, self.orig_y)

    def call_function(self, widget, *args):                                             # calls function in the app by literally evaluating the string
        eval(widget.id)


class SSP1(App):

    def build(self):
        f = FloatLayout()
        self.mb1 = MenuButton(text='play', action='App.get_running_app().buildGameMenu()', options={ '1': 'App.get_running_app().pp("a")', '2': 'App.get_running_app().pp("b")' } )
        self.mb1.orig_y = f.height - self.mb1.button.height    # save the original y position, so it can be restored later
        self.mb1.pos = (0, self.mb1.orig_y)
        f.add_widget(self.mb1)

        self.mb2 = MenuButton(text='Testing2', action='App.get_running_app().pp("2")', options={ '1': 'App.get_running_app().pp("a")', '2': 'App.get_running_app().pp("b")' } )
        self.mb2.orig_y = f.height - self.mb1.button.height - self.mb2.button.height    # save the original y position, so it can be restored later
        self.mb2.pos = (0, self.mb2.orig_y)
        f.add_widget(self.mb2)

        self.mb3 = MenuButton(text='Testing3', action='App.get_running_app().pp("3")',
                              options={'1': 'App.get_running_app().pp("a")', '2': 'App.get_running_app().pp("b")'})
        self.mb3.orig_y = f.height - self.mb2.button.height - self.mb3.button.height - self.mb1.button.height  # save the original y position, so it can be restored later
        self.mb3.pos = (0, self.mb3.orig_y)
        f.add_widget(self.mb3)

        self.root = f

        f.bind(size=self.sizeChanged)    # handle size adjustments when app is displayed

    def sizeChanged(self, *args):
        # make sure the MenuButtons are always at the top
        self.mb1.orig_y = self.root.height - self.mb1.button.height
        self.mb2.orig_y = self.root.height - self.mb1.button.height - self.mb2.button.height
        self.mb3.orig_y = self.root.height - self.mb2.button.height - self.mb3.button.height - self.mb1.button.height  # save the original y position, so it can be restored later

        self.mb1.pos = (0, self.mb1.orig_y)
        self.mb2.pos = (0, self.mb2.orig_y)
        self.mb3.pos = (0, self.mb3.orig_y)

    def pp(self,text):
        print(text)

    def buildGameMenu(self):
        f = FloatLayout()
        self.mb1 = MenuButton(text='Testing1', action='App.get_running_app().buildGameMenu()',
                              options={'1': 'App.get_running_app().pp("a")', '2': 'App.get_running_app().pp("b")'})
        self.mb1.orig_y = f.height - self.mb1.button.height  # save the original y position, so it can be restored later
        self.mb1.pos = (0, self.mb1.orig_y)
        f.add_widget(self.mb1)

        self.mb2 = MenuButton(text='Testing2', action='App.get_running_app().pp("3")',
                              options={'1': 'App.get_running_app().pp("a")', '2': 'App.get_running_app().pp("b")'})
        self.mb2.orig_y = f.height - self.mb1.button.height - self.mb2.button.height  # save the original y position, so it can be restored later
        self.mb2.pos = (0, self.mb2.orig_y)
        f.add_widget(self.mb2)

        self.mb3 = MenuButton(text='Testing3', action='App.get_running_app().pp("3")',
                              options={'1': 'App.get_running_app().pp("a")', '2': 'App.get_running_app().pp("b")'})
        self.mb3.orig_y = f.height - self.mb2.button.height - self.mb3.button.height - self.mb1.button.height  # save the original y position, so it can be restored later
        self.mb3.pos = (0, self.mb3.orig_y)
        f.add_widget(self.mb3)

        self.root = f

        f.bind(size=self.sizeChanged)


