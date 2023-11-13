def on_button_pressed_a():
    global Rock
    Rock = "ROCK"
    basic.show_leds("""
        . . . . .
        . # # # .
        # # # # #
        . # # # .
        . . . . .
        """)
    basic.show_string(" " + Rock)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Paper
    Paper = "PAPER"
    basic.show_leds("""
        # # # . .
        # # # # .
        . # # # .
        . # # # .
        . # # # #
        """)
    basic.show_string(" " + Paper)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Scissor
    Scissor = "SCISSOR"
    basic.show_leds("""
        . . # . .
        . . # . .
        . # # # .
        # . # . #
        # # # # #
        """)
    basic.show_string(" " + Scissor)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Scissor = ""
Paper = ""
Rock = ""
basic.show_string("RPS")