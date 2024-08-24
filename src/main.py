import board
import displayio
import rgbmatrix
import framebufferio
import keypad
import asyncio

import render
import collision

key_trigger = keypad.Keys((board.GP27,), value_when_pressed=False, interval=0.005)


def init_display():
    displayio.release_displays()
    display = framebufferio.FramebufferDisplay(
        rgbmatrix.RGBMatrix(
            width=64, bit_depth=4,
            rgb_pins=[board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5],
            addr_pins=[board.GP6, board.GP7, board.GP8, board.GP9],
            clock_pin=board.GP10, latch_pin=board.GP12, output_enable_pin=board.GP13),
        auto_refresh=True)

    render.init_display_assets()

    display.root_group = render.main_group
    display.refresh()


def check_if_button_pressed():
    global key_trigger
    event = key_trigger.events.get()
    return event and event.released


async def run_single_round():
    score = 0

    add_asset_counter = 30
    while True:
        score += 1
        add_asset_counter += 1
        if add_asset_counter > 30 and render.insert_obstacle():
            add_asset_counter = 0

        if check_if_button_pressed():
            render.set_dino_jumping()

        for tile in render.obstacle_assets:
            if tile.hidden == False and collision.detect_collision(render.dino_asset, tile):
                return

        render.progress_obstacles()
        render.progress_dino()
        render.update_score_label(score)

        wait_time = (1000 - score) / 10000
        await asyncio.sleep(wait_time)


async def main():
    init_display()

    while True:
        render.show_restart_indicator(True)
        while not check_if_button_pressed():
            await asyncio.sleep(0)
        render.reset_items()
        render.show_restart_indicator(False)
        await run_single_round()


asyncio.run(main())


