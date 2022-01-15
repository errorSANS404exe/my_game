import wrap
import wrap as UwU, time, random
from wrap import world, sprite

t = time.time()
UwU.add_sprite_dir("my_sprites")
world.create_world(1000, 1000)
world.set_back_color(10, 50, 66)
n_1 = sprite.add("black_mario", 400, 500, "jump")
n_2 = sprite.add("black_mario", 500, 500, "stand")
n_3 = sprite.add("black_mario", 600, 500, "swim6")
n_4 = sprite.add("black_mario", 700, 500, "walk3")
mario1 = sprite.add("mario-2-big", sprite.get_x(n_1), sprite.get_y(n_1), "jump", False)
sprite.set_size(mario1, sprite.get_width(n_1), sprite.get_height(n_1))

mario2 = sprite.add("mario-2-big", sprite.get_x(n_2), sprite.get_y(n_2), "stand", False)
sprite.set_size(mario2, sprite.get_width(n_2), sprite.get_height(n_2))

mario3 = sprite.add("mario-2-big", sprite.get_x(n_3), sprite.get_y(n_3), "swim6", False)
sprite.set_size(mario3, sprite.get_width(n_3), sprite.get_height(n_3))

mario4 = sprite.add("mario-2-big", sprite.get_x(n_4), sprite.get_y(n_4), "walk3", False)
sprite.set_size(mario4, sprite.get_width(n_4), sprite.get_height(n_4))

m = sprite.add("mario-2-big", sprite.get_x(n_1), 0, "jump")
sprite.set_size(m, sprite.get_width(n_1), sprite.get_height(n_1))

m2 = sprite.add("mario-2-big", sprite.get_x(n_4), 0, "walk3")
sprite.set_size(m2, sprite.get_width(n_4), sprite.get_height(n_4))


@wrap.on_key_down(UwU.K_z, UwU.K_x, UwU.K_PERIOD, UwU.K_COMMA)
def buttons(keys):
    # если кнопка z нажата,
    # марио должен появиться

    if UwU.K_z in keys:
        sprite.show(mario1)
    if UwU.K_x in keys:
        sprite.show(mario2)
    if UwU.K_COMMA in keys:
        sprite.show(mario3)
    if UwU.K_PERIOD in keys:
        sprite.show(mario4)


@wrap.on_key_up(UwU.K_z, UwU.K_x, UwU.K_PERIOD, UwU.K_COMMA)
def key_up(keys):
    if UwU.K_z not in keys:
        sprite.hide(mario1)
    if UwU.K_x not in keys:
        sprite.hide(mario2)
    if UwU.K_COMMA not in keys:
        sprite.hide(mario3)
    if UwU.K_PERIOD not in keys:
        sprite.hide(mario4)


@wrap.always
def move5():
    world.set_title(int(time.time() - t))
    if int(time.time() - t) >= 3:
        sprite.move(m, 0, 10)
    if int(time.time() - t) >= 5:
        sprite.move(m2, 0, 10)


list = []


@wrap.always
def test(keys):
    mario = sprite.add("mario-2-big", random.randint(1, 1000), random.randint(1, 1000), "jump")
    list.append(mario)
    print(list)
    if wrap.K_z in keys:
        for mario in list:
            list.remove(mario)
            sprite.remove(mario)
# n=889
# n2=345
# n3=n
# n+=1
# list=[98,76,678]
# f=[209,876,3673]
# a=list
# f.append(583)
# a.append(786)
# dict={"name":"Peter","age":16,"weight":50}
# print(f[0])
# print(dict["name"])
# f[0]+=1
# dict["weight"]+=3
# klass=[]
# klass.append(dict)
# dict={"name":"Vadim","age":17,"weight":54}
# klass.append(dict)
# dict={"name":"Egor","age":17,"weight":52}
# klass.append(dict)