"""
CP1404 - Practical 08
DO FROM SCRATCH
Estimate: 1.5 hours
Actual:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_RATE = 1.609

class ConvertMilesToKilometersApp(App):
    """Convert miles to kilometers is a Kivy app for converting miles to kilometers."""
    km_output = StringProperty()

    def build(self):
        """Build the kivy app from the kv file."""
        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, input_text):
        """Convert miles to kilometers."""
        conversion = self.convert_to_number(input_text) * CONVERSION_RATE
        self.km_output = str(conversion)

    def handle_increment(self, input_text, increment):
        """Increments input text."""
        result = self.convert_to_number(input_text) + increment
        self.root.ids.input_number.text = str(result)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0

ConvertMilesToKilometersApp().run()