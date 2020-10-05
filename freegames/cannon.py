"""
翻译，注释：夏沫

Cannon, hitting targets with projectiles.
炮击目标

Exercises
程序练习
1. Keep score by counting target hits.
使用变量进行命中计数。
2. Vary the effect of gravity.
改变重力效果。
3. Apply gravity to the targets.
使目标受到重力效果、
4. Change the speed of the ball.
改变炮弹速度.

"""
# 基本库
from random import randrange
from turtle import *
from freegames import vector

# 二维矢量（速度）,目标数据库声明
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    # Respond to screen tap.
    if not inside(ball):
        ball.x = -199  # 炮弹的xy两轴上的初始坐标和速度，根据发射点和鼠标点击点确定速度
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    # Return True if xy within screen. 判断炮弹是否在屏幕内
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    # Draw ball and targets.
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'red')  # 目标的大小和颜色

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'blue')  # 炮弹的大小和颜色

    update()


def move():
    # Move ball and targets.
    if randrange(40) == 0:
        y = randrange(-150, 150)  # 随机生成靶位
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.2  # 目标从右向左运动速度 0.2

    if inside(ball):
        speed.y -= 0.35  # g值/y轴上炮弹的运动速度 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:  # 生成频率，靶子离开右侧多少像素点后生成新目标
            targets.append(target)  # 生成新目标

    draw()  # 重新绘图

    for target in targets:  # 炮弹碰壁终止游戏
        if not inside(target):
            return

    ontimer(move, 50)  # 在50ms后调用move函数


setup(420, 420, 370, 0)  # 初始化屏幕
hideturtle()  # 隐藏画笔箭头
up()  # 抬起画笔
tracer(False)  # 不显示画图轨迹
onscreenclick(tap)  # 点击屏幕某点时把点击坐标传给tap函数
move()
done()
