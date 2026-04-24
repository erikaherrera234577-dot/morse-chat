radio.onReceivedNumber(function (receivedNumber) {
    radio.setGroup(7)
})
input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    radio.sendNumber(8)
})
basic.clearScreen()
basic.showLeds(`
    # . . . #
    # # . . #
    # . # . #
    # . . # #
    # . . . #
    `)
basic.forever(function () {
    if ((67 as any) < (77 as any)) {
    	
    }
    music.play(music.tonePlayable(247, music.beat(BeatFraction.Double)), music.PlaybackMode.LoopingInBackground)
})
