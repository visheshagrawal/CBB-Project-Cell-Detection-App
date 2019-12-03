import combined
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
Builder.load_string('''
<CameraClick>:
    label_widget: label_widget
    orientation: 'vertical'
    Camera:
        id: camera
        # resolution: (640, 480)        
        resolution: (640, 640)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
    Label:
        id: label_widget
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        # camera.export_to_png("IMG_{}.png".format(timestr))
        camera.export_to_png("1.png")
        print("Captured")
        a=combined.process()
        self.label_widget.text = str(a)


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()
