import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

class childApp(BoxLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 50, 50, 50]
        self.spacing = 20
        
        # Set background color
        with self.canvas.before:
            Color(0.95, 0.95, 0.98, 1)  # Light blue-gray background
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        # Title
        title = Label(
            text='Student Information Form',
            font_size='24sp',
            color=(0.2, 0.3, 0.6, 1),
            size_hint_y=None,
            height='60dp',
            bold=True
        )
        self.add_widget(title)
        
        # Create form layout
        form_layout = GridLayout(
            cols=2,
            row_default_height='50dp',
            col_default_width='200dp',
            spacing=[20, 15],
            size_hint_y=None
        )
        form_layout.bind(minimum_height=form_layout.setter('height'))
        
        # Student Name
        name_label = Label(
            text='Student Name:',
            font_size='16sp',
            color=(0.3, 0.3, 0.3, 1),
            halign='right',
            valign='middle'
        )
        name_label.bind(size=name_label.setter('text_size'))
        form_layout.add_widget(name_label)
        
        self.s_name = TextInput(
            multiline=False,
            font_size='16sp',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.2, 0.2, 0.2, 1),
            cursor_color=(0.2, 0.3, 0.6, 1),
            padding=[10, 10, 10, 10]
        )
        form_layout.add_widget(self.s_name)
        
        # Student Marks
        marks_label = Label(
            text='Student Marks:',
            font_size='16sp',
            color=(0.3, 0.3, 0.3, 1),
            halign='right',
            valign='middle'
        )
        marks_label.bind(size=marks_label.setter('text_size'))
        form_layout.add_widget(marks_label)
        
        self.s_marks = TextInput(
            multiline=False,
            font_size='16sp',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.2, 0.2, 0.2, 1),
            cursor_color=(0.2, 0.3, 0.6, 1),
            padding=[10, 10, 10, 10],
            input_filter='int'  # Only allow integers
        )
        form_layout.add_widget(self.s_marks)

        # Student Gender
        gender_label = Label(
            text='Student Gender:',
            font_size='16sp',
            color=(0.3, 0.3, 0.3, 1),
            halign='right',
            valign='middle'
        )
        gender_label.bind(size=gender_label.setter('text_size'))
        form_layout.add_widget(gender_label)
        
        self.s_gender = TextInput(
            multiline=False,
            font_size='16sp',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.2, 0.2, 0.2, 1),
            cursor_color=(0.2, 0.3, 0.6, 1),
            padding=[10, 10, 10, 10]
        )
        form_layout.add_widget(self.s_gender)
        
        self.add_widget(form_layout)
        
        # Add some space
        self.add_widget(Widget(size_hint_y=None, height='30dp'))
        
        # Submit button
        self.press = Button(
            text='Submit Information',
            font_size='18sp',
            size_hint=(None, None),
            size=('250dp', '50dp'),
            pos_hint={'center_x': 0.5},
            background_color=(0.2, 0.6, 0.8, 1),
            color=(1, 1, 1, 1)
        )
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)
        
        # Result display area
        self.result_label = Label(
            text='',
            font_size='14sp',
            color=(0.2, 0.5, 0.2, 1),
            halign='center',
            valign='top',
            text_size=(None, None)
        )
        self.add_widget(self.result_label)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def click_me(self, instance):
        name = self.s_name.text.strip()
        marks = self.s_marks.text.strip()
        gender = self.s_gender.text.strip()
        
        if not name or not marks or not gender:
            self.result_label.text = "Please fill in all fields!"
            self.result_label.color = (0.8, 0.2, 0.2, 1)  # Red color for error
        else:
            result_text = f"""
Student Information Submitted Successfully!

Name: {name}
Marks: {marks}
Gender: {gender}
            """
            self.result_label.text = result_text.strip()
            self.result_label.color = (0.2, 0.5, 0.2, 1)  # Green color for success
            self.result_label.text_size = (400, None)
            
            # Also print to console
            print(f"Name of Student is: {name}")
            print(f"Marks of Student is: {marks}")
            print(f"Gender of Student is: {gender}")
            print("")


class StudentApp(App):
    def build(self):
        self.title = 'Student Information System'
        return childApp()
    
if __name__ == "__main__":
    StudentApp().run()