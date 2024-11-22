"""
CP1404 - PRAC 08
DFS
Estimate: 40 mins
Actual: 25 mins
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """main program- Kivy app to create dynamic labels"""
    label_text = StringProperty

    def __init__(self, **kwargs):
        """Constructor."""
        super().__init__(**kwargs)
        self.names = ["Jessica", "Alfonso", "Blythe", "Finnian"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Labels and add them to the Kivy GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
