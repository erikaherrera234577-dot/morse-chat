def on_received_number(receivedNumber):
    radio.set_group(7)
radio.on_received_number(on_received_number)

def on_logo_long_pressed():
    radio.send_number(8)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

basic.clear_screen()
basic.show_leds("""
    # . . . #
    # # . . #
    # . # . #
    # . . # #
    # . . . #
    """)

def on_forever():
    if (67) < (77):
        pass
    music.play(music.tone_playable(247, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
basic.forever(on_forever)
