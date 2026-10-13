from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.core.window import Window

Window.clearcolor = (0.12, 0.12, 0.12, 1)

class DotpixSkinApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        title = Label(
            text='DOTPIX AI SKIN', 
            font_size='24sp', 
            bold=True, 
            color=(0, 0.9, 1, 1),
            size_hint=(1, 0.2)
        )
        layout.add_widget(title)

        self.status = Label(
            text='Ready to Retouch', 
            font_size='16sp', 
            color=(0.8, 0.8, 0.8, 1),
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.status)

        layout.add_widget(Label(text='AI Smoothness', size_hint=(1, 0.1)))
        self.slider = Slider(min=5, max=40, value=15, size_hint=(1, 0.15))
        layout.add_widget(self.slider)

        btn = Button(
            text='Auto AI Skin Retouch', 
            size_hint=(1, 0.25),
            background_color=(0, 0.9, 1, 1),
            color=(0, 0, 0, 1),
            bold=True
        )
        btn.bind(on_press=self.run_retouch)
        layout.add_widget(btn)

        return layout

    def run_retouch(self, instance):
        self.status.text = 'AI Processing Face & Skin...'

if __name__ == '__main__':
    DotpixSkinApp(
      
    ).run()
