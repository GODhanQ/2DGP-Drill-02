from pico2d import *

open_canvas()

img_character = load_image('C:\\Users\\user\\Desktop\\2024180014\\2DGP-Drill-02\\Lecture04_2D_Rendering\\Character.png')
img_grass = load_image('C:\\Users\\user\\Desktop\\2024180014\\2DGP-Drill-02\\Lecture04_2D_Rendering\\Grass.png')

isRectMove = True
moving_amount = 5

while True:
    if isRectMove:
        x, y = 50, 90
        for i in range(0, 4):
            if i == 0:
                print(f'x: {x}, y: {y}')
                while x < 750:
                    clear_canvas_now()
                    img_grass.draw_now(400, 30)
                    img_character.draw_now(x, y)
                    x += moving_amount
                    delay(0.01)
            elif i == 1:
                print(f'x: {x}, y: {y}')
                while y < 550:
                    clear_canvas_now()
                    img_grass.draw_now(400, 30)
                    img_character.draw_now(x, y)
                    y += moving_amount
                    delay(0.01)
            elif i == 2:
                print(f'x: {x}, y: {y}')
                while x > 50:
                    clear_canvas_now()
                    img_grass.draw_now(400, 30)
                    img_character.draw_now(x, y)
                    x -= moving_amount
                    delay(0.01)
            else:
                print(f'x: {x}, y: {y}')
                while y > 90:
                    clear_canvas_now()
                    img_grass.draw_now(400, 30)
                    img_character.draw_now(x, y)
                    y -= moving_amount
                    delay(0.01)
        isRectMove = False
    else:
        x, y = 50, 90
        circle_origin_x, circle_origin_y = 400, 300
        circle_radius = (570 / 2) - 80
        angle = 270

        img_character.draw_now(400, 90)

        while True:
            if angle >= 270 + 360:
                break
            print(f'angle: {angle}')
            clear_canvas_now()
            img_grass.draw_now(400, 30)
            img_character.draw_now(circle_origin_x + circle_radius * math.cos(math.radians(angle)), circle_origin_y + circle_radius * math.sin(math.radians(angle)))
            angle += (moving_amount / 100)
        break

# delay(3)
close_canvas()
