from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CalculatorGrid(GridLayout):
    """
    This class defines the layout and behavior of the calculator's grid.
    It handles button presses and updates the display.
    """
    def __init__(self, **kwargs):
        super(CalculatorGrid, self).__init__(**kwargs)
        self.cols = 4  # Grid layout with 4 columns
        self.spacing = 5

        # Buttons for numbers and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+'
        ]

        # Adding buttons to the layout
        for button in buttons:
            btn = Button(text=button, font_size=24)
            btn.bind(on_press=self.on_button_press)
            self.add_widget(btn)

        # Clear button
        clear_btn = Button(text="C", font_size=24)
        clear_btn.bind(on_press=self.clear_result)
        self.add_widget(clear_btn)

    # Function to handle button press events
    def on_button_press(self, instance):
        """
        This method is called every time a button is pressed.
        It updates the display field based on the button's text.
        """
        current_text = self.parent.display_field.text
        button_text = instance.text

        # If the equals sign is pressed, evaluate the expression
        if button_text == "=":
            try:
                # The eval() function is used for simplicity, but is not secure.
                result = str(eval(current_text))
                self.parent.display_field.text = result
            except Exception:
                self.parent.display_field.text = "Error"
        else:
            # Otherwise, append the pressed button's text to the current expression
            if self.parent.display_field.text == "Error":
                self.parent.display_field.text = button_text
            else:
                self.parent.display_field.text += button_text

    # Function to clear the result field
    def clear_result(self, instance):
        self.parent.display_field.text = ""

class CalculatorApp(App):
    """
    This is the main application class.
    It builds the UI by creating a BoxLayout with a display and the calculator grid.
    """
    def build(self):
        # Main layout is a vertical BoxLayout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # The display field is an attribute of the main app, so it's accessible by all widgets
        self.display_field = TextInput(
            font_size=32,
            readonly=True,
            halign="right",
            multiline=False,
            size_hint_y=None,
            height=80,
            text=""
        )
        main_layout.add_widget(self.display_field)
        
        # The calculator grid is a separate widget added to the main layout
        calculator_grid = CalculatorGrid()
        main_layout.add_widget(calculator_grid)
        
        return main_layout

if __name__ == '__main__':
    CalculatorApp().run()
