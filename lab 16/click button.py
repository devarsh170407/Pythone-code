from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SimpleApp(App):
    
    def build(self):
        # Create a vertical box layout to hold the widgets
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create a label and a button
        self.label = Label(text="Hello Devarsh Press the bellow button!")
        button = Button(text="Click Me!")

        # Bind the button's 'on_press' event to the on_button_press method
        button.bind(on_press=self.on_button_press)

        # Add the widgets to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        """
        Function to handle the button click event.
        It updates the text of the label.
        """
        self.label.text = "Button Clicked!"

if __name__ == '__main__':
    SimpleApp().run()
