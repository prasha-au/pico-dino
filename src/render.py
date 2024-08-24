import board
import displayio
import adafruit_imageload
import random
from adafruit_display_text.label import Label
from adafruit_display_shapes.line import Line
import terminalio


score_label = None
dino_asset = None
obstacle_assets = []
main_group = None
restart_asset = None

dino_jump_sequence = None


def init_display_assets():
    global score_label, dino_asset, obstacle_assets, main_group, restart_asset

    main_group = displayio.Group()

    horizon = Line(0, 26, 64, 26, 0xff9600)
    main_group.append(horizon)

    def init_generic_obstacle(filename: str, y: int):
        b, p = adafruit_imageload.load(filename)
        p.make_transparent(0)
        tile = displayio.TileGrid(b, pixel_shader=p)
        tile.x = 60
        tile.y = y
        tile.hidden = True
        obstacle_assets.append(tile)
        main_group.append(tile)

    init_generic_obstacle('cactus.bmp', 20)
    init_generic_obstacle('smallcactus.bmp', 22)
    init_generic_obstacle('rock.bmp', 21)

    score_label = Label(text="0", font=terminalio.FONT, color=0xC59A78, x=58, y=5)
    main_group.append(score_label)

    b, p = adafruit_imageload.load('dino.bmp')
    p.make_transparent(250)
    dino = displayio.TileGrid(b, pixel_shader=p, width = 1, height = 1, tile_width = 16, tile_height = 16)
    dino.x = 1
    dino.y = 15
    dino_asset = dino
    main_group.append(dino)


    b, p = adafruit_imageload.load('restart.bmp')
    p.make_transparent(0)
    restart_asset = displayio.TileGrid(b, pixel_shader=p)
    restart_asset.x = 24
    restart_asset.y = 8
    restart_asset.hidden = True
    main_group.append(restart_asset)



def progress_obstacles():
    global obstacle_assets
    for tile in obstacle_assets:
        if tile.hidden == True:
            continue
        tile.x -= 2

        if tile.x < -tile.tile_width:
            tile.hidden = True


def insert_obstacle():
    global obstacle_assets
    inactive_tiles = list(filter(lambda t: t.hidden == True, obstacle_assets))

    if len(inactive_tiles) == 0:
        return False

    idx = random.randint(0, len(inactive_tiles) - 1)
    tile = inactive_tiles[idx]
    tile.x = 80
    tile.hidden = False

    return True


def update_score_label(score: int):
    global score_label
    score_label.text = str(score)
    score_label.x = 64 - score_label.bounding_box[2]



def set_dino_jumping():
    global dino_jump_sequence
    if dino_jump_sequence is None:
        dino_jump_sequence = [12, 9, 6, 4, 2, 0, 0, 0, 2, 4, 6, 8, 10, 12, 15]


def progress_dino():
    global dino_asset, dino_jump_sequence
    if dino_jump_sequence is None:
        dino_asset[0] = (dino_asset[0] + 1) % 2
        dino_asset.y = 15
    else:
        dino_asset[0] = 2
        dino_asset.y = dino_jump_sequence.pop(0)
        if len(dino_jump_sequence) == 0:
            dino_jump_sequence = None


def reset_items():
    global dino_jump_sequence, obstacle_assets
    dino_jump_sequence = None
    for tile in obstacle_assets:
        tile.hidden = True

def show_restart_indicator(show: bool):
    global restart_asset
    restart_asset.hidden = not show
