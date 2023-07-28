import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from calculator import Calculator

class CalculatorApp(App):
    def build(self):
        self.operators = ["+", "-", "*", "/"]
        self.last_was_operator = None
        self.last_button = None
        self.calculation = Calculator()

        main_layout = BoxLayout(orientation="vertical")

        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )

        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button_layout = BoxLayout(padding=10)
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    font_size = 25
                )
                if label in self.operators:
                    button.background_color = [253/255, 149/255, 3/255, 1]
                elif label == "." or label == "C":
                    button.background_color = [165/255, 165/255, 165/255, 1]
                else:
                    button.background_color = [51/255, 51/255, 51/255, 1]
                button.background_normal = ''
                button.bind(on_release=self.on_button_press)
                button_layout.add_widget(button)
                h_layout.add_widget(button_layout)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_release=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(text))
            self.solution.text = solution

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
