import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
kivy.require('1.9.0')


class TutorialApp(App):

    def build(self):
        global layout
        layout = GridLayout(cols=1,
                            row_force_default=True,
                            row_default_height=40,
                            spacing=10,
                            padding=20
                            )

        labelnbr1 = Label(text="Premier nombre", color='white')
        labelnbr2 = Label(text="Deuxieme nombre", color='white')
        # Adding the text input
        global nbr1
        global nbr2
        nbr1 = TextInput(font_size=15)
        nbr2 = TextInput(font_size=15)

        f = FloatLayout()

        # By this you are able to move the
        # Text on the screen to anywhere you want
        s = Scatter()



        # Binding it with the label
        #t.bind(text=l.setter('text'))


        # use a (r, g, b, a) tuple
        btn = Button(text ="Calculer",
                     font_size ="20sp",
                     background_color =(1, 1, 1, 1),
                     color =(1, 1, 1, 1),
                     size =(32, 32),
                     size_hint =(.2, .2),
                     pos =(300, 250),
                     )
        btnReset = Button(text ="Reset",
                     font_size ="20sp",
                     background_color =(1, 1, 1, 1),
                     color =(1, 1, 1, 1),
                     size =(32, 32),
                     size_hint =(.2, .2),
                     pos =(300, 250))

        # bind() use to bind the button to function callback
        btn.bind(on_press = self.callback)
        btnReset.bind(on_press = self.reset)
        #btnSubmit = Button(text="Calculer")
        #btnSubmit.bind(on_press = self.callback(nbr1,nbr2))
        f.add_widget(s)
        #s.add_widget(labelResult)
        layout.add_widget(labelnbr1)

        layout.add_widget(nbr1)
        layout.add_widget(labelnbr2)
        layout.add_widget(nbr2)
        layout.add_widget(btn)
        layout.add_widget(btnReset)
        layout.add_widget(f)

        return layout

    # callback function tells when button pressed
    def callback(self, event):
        a = int(nbr1.text)
        b = int(nbr2.text)
        result = a + b
        resultstr = str(result)
        print(resultstr)
        labelResult = Label(text=resultstr,
                    font_size=20,color="white")
        layout.add_widget(labelResult)
        return layout

    def reset(self,event):
        print("effacer")
        nbr1.text = ""
        nbr2.text = ""


# Run the App
if __name__ == "__main__":
    TutorialApp().run()
