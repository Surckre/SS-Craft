from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
blocksound = Audio("bb.wav", loop=False, autoplay=False)
skytx = load_texture("sky.jpg")
music = Audio("music.wav", loop=True,autoplay=True )
Sky(texture=skytx)
player = FirstPersonController()
tx = load_texture("block_texture.png")
boxes = []

def add_box(position):
   boxes.append(
        Button(
        parent=scene,
        model='cube',
        origin=0.1,
        color=color.random_color(),
        position=position,
        texture=tx
    )
    )


for x in range(10):
    for y in range(10):
        add_box((x,0,y))

def input(key):
    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                add_box(box.position + mouse.normal)
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)
                blocksound.play()
            if key == "n":
                quit()
app.run()