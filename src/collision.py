import adafruit_imageload
import displayio


def detect_collision(dino, obstacle):
  c1 = (dino.x, dino.y, dino.x + dino.tile_width, dino.y + dino.tile_height)
  c2 = (obstacle.x, obstacle.y, obstacle.x + obstacle.tile_width, obstacle.y + obstacle.tile_height)

  check_area = (max(c1[0], c2[0]), max(c1[1], c2[1]), min(c1[2], c2[2]), min(c1[3], c2[3]))

  if check_area[0] > check_area[2] or check_area[1] > check_area[3]:
    return False

  dino_bitmap = dino.bitmap
  obstacle_bitmap = obstacle.bitmap


  dino_sprite_offset_x = dino[0] * dino.tile_width
  for x in range(check_area[0], check_area[2]):
    for y in range(check_area[1], check_area[3]):
      if dino_bitmap[x - dino.x + dino_sprite_offset_x, y - dino.y] != 250 and obstacle_bitmap[x - obstacle.x, y - obstacle.y] != 0:
        return True


  return False

