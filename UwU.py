import wrap
import wrap as UwU, time, random
from wrap import world, sprite, sprite_text

t = time.time()
UwU.add_sprite_dir("my_sprites")
world.create_world(1000, 1000)
world.set_back_color(10, 50, 66)
n_1 = sprite.add("black_mario", 400, 500, "jump")
n_2 = sprite.add("black_mario", 500, 500, "stand")
n_3 = sprite.add("black_mario", 600, 500, "swim6")
n_4 = sprite.add("black_mario", 700, 500, "walk3")
numbers = [n_1, n_2, n_3, n_4]
mario1 = sprite.add("mario-2-big", sprite.get_x(n_1), sprite.get_y(n_1), "jump", False)
sprite.set_size(mario1, sprite.get_width(n_1), sprite.get_height(n_1))

mario2 = sprite.add("mario-2-big", sprite.get_x(n_2), sprite.get_y(n_2), "stand", False)
sprite.set_size(mario2, sprite.get_width(n_2), sprite.get_height(n_2))

mario3 = sprite.add("mario-2-big", sprite.get_x(n_3), sprite.get_y(n_3), "swim6", False)
sprite.set_size(mario3, sprite.get_width(n_3), sprite.get_height(n_3))

mario4 = sprite.add("mario-2-big", sprite.get_x(n_4), sprite.get_y(n_4), "walk3", False)
sprite.set_size(mario4, sprite.get_width(n_4), sprite.get_height(n_4))

# m = sprite.add("mario-2-big", sprite.get_x(n_1), -75, "jump")
# sprite.set_size(m, sprite.get_width(n_1), sprite.get_height(n_1))
# w = {"number": m, "flight": 5}
#
# m2 = sprite.add("mario-2-big", sprite.get_x(n_4), -75, "walk3")
# sprite.set_size(m2, sprite.get_width(n_4), sprite.get_height(n_4))
# a = {"number": m2, "flight": 6}
#
# m3 = sprite.add("mario-2-big", sprite.get_x(n_3), -75, "swim6")
# sprite.set_size(m3, sprite.get_width(n_3), sprite.get_height(n_3))
# s = {"number": m3, "flight": 2}
mario_list = []

chain = []
a = {"time": random.randint(1, 10), "who": random.choice(numbers)}
chain.append(a)

x = 1
for y in range(50):
    x += random.randint(1, 4)
    a = {"time": x, "who": random.choice(numbers)}
    chain.append(a)


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
    for all in mario_list:
        sprite.move(all["number"], 0, 10)


@wrap.always
def creation():
    for a in chain:
        if int(time.time() - t) >= a["time"]:
            d = sprite.add("mario-2-big", sprite.get_x(a["who"]), -75, sprite.get_costume(a["who"]))
            sprite.set_size(d, sprite.get_width(a["who"]), sprite.get_height(a["who"]))
            w = {"number": d}
            mario_list.append(w)
            chain.remove(a)


text = sprite.add_text("Score:0", 200, 230, font_size=100)
score = 0



def test():
    global score
    for a in mario_list:
        if sprite.is_collide_sprite(mario1, a["number"]) and sprite.is_visible(mario1):
            sprite.remove(a["number"])
            mario_list.remove(a)
            score = score + 5
            sprite_text.set_text(text, 'Score:' + str(score))
        if sprite.is_collide_sprite(mario1, a["number"]) == False and sprite.is_visible(mario1):
            score-=1
            sprite_text.set_text(text, 'Score:' + str(score))

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
# dict={"name":"Egor","age":18,"weight":52}
# klass.append(dict)
# #del dict
# print(klass[1]["age"])
# klass[1]["age"]+=1
# #klass[2]["year"]=2022-klass[2]["age"]
# for name in klass:
#     name["year"]=2022-name["age"]
