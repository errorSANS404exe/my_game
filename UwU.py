import wrap as UwU
from wrap import world, sprite

UwU.add_sprite_dir("my_sprites")
world.create_world(1000, 1000)
world.set_back_color(10, 50, 66)
sprite.add("black_mario", 400, 500, "jump")
sprite.add("black_mario", 500, 500, "stand")
sprite.add("black_mario", 600, 500, "swim6")
sprite.add("black_mario", 700, 500, "walk3")