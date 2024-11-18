"""
CP1404 - Practical 08
DO FROM SCRATCH
Estimate: 1.5 hours
Actual:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class ConvertMilesToKilometersApp(App):
    """Convert miles to kilometers is a Kivy app for converting miles to kilometers."""
    km_output = StringProperty()

    def build(self):
        """ Build the kivy app from the kv file"""
        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        try:
            conversion = float(value) * 1.609
            self.root.ids.output_label.text = str(conversion)
        except ValueError:
            pass

    def handle_increment(self, value, increment):
        try:
            result = float(value) + increment
            self.km_output = str(result)
        except ValueError:
            pass




ConvertMilesToKilometersApp().run()