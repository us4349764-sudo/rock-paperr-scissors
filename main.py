import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class RockPaperScissorsApp(App):
    def build(self):
        self.title = "Rock Paper Scissors"
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.lbl_title = Label(text="ROCK PAPER SCISSORS", font_size='24sp', bold=True, size_hint_y=0.2)
        main_layout.add_widget(self.lbl_title)
        self.lbl_result = Label(text="Choose your move!", font_size='18sp', halign='center', size_hint_y=0.4)
        main_layout.add_widget(self.lbl_result)
        btn_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.3)
        
        btn_rock = Button(text="ROCK", font_size='16sp', background_color=get_color_from_hex('#e74c3c'), background_normal='')
        btn_rock.bind(on_press=lambda x: self.play("ROCK"))
        btn_paper = Button(text="PAPER", font_size='16sp', background_color=get_color_from_hex('#3498db'), background_normal='')
        btn_paper.bind(on_press=lambda x: self.play("PAPER"))
        btn_scissor = Button(text="SCISSOR", font_size='16sp', background_color=get_color_from_hex('#2ecc71'), background_normal='')
        btn_scissor.bind(on_press=lambda x: self.play("SCISSOR"))
        
        btn_layout.add_widget(btn_rock)
        btn_layout.add_widget(btn_paper)
        btn_layout.add_widget(btn_scissor)
        main_layout.add_widget(btn_layout)
        return main_layout

    def play(self, player_choice):
        choices = ["ROCK", "PAPER", "SCISSOR"]
        comp = random.choice(choices)
        if player_choice == comp:
            msg = "IT'S A TIE!"
        elif (player_choice == "ROCK" and comp == "SCISSOR") or \
             (player_choice == "PAPER" and comp == "ROCK") or \
             (player_choice == "SCISSOR" and comp == "PAPER"):
            msg = "YOU WIN! 🎉"
        else:
            msg = "COMPUTER WINS!"
        self.lbl_result.text = f"YOU: {player_choice}\nCOMPUTER: {comp}\n\n[b]{msg}[/b]"
        self.lbl_result.markup = True

if __name__ == '__main__':
    RockPaperScissorsApp().run()
