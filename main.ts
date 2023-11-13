input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Rock = "ROCK"
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # #
        . # # # .
        . . . . .
        `)
    basic.showString(" " + Rock)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Paper = "PAPER"
    basic.showLeds(`
        # # # . .
        # # # # .
        . # # # .
        . # # # .
        . # # # #
        `)
    basic.showString(" " + Paper)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Scissor = "SCISSOR"
    basic.showLeds(`
        . . # . .
        . . # . .
        . # # # .
        # . # . #
        # # # # #
        `)
    basic.showString(" " + Scissor)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
})
let Scissor = ""
let Paper = ""
let Rock = ""
basic.showString("RPS")
