# Adding a sagittal dimension to the 13th Century Cistercian monks numerals
# to bring the upper limit from 9,999 to 99,999.

import numpy as np
# import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import randrange


# Cistercian = int(input("Please Input number from 1 to 99,999: "))
Cistercian = randrange(1, 99999)

# print(f"{Cistercian:,}")
List_digits = [0, 0, 0] + [int(x) for x in str(Cistercian)]
# Concatenating [0,0,0] for "padding"

units = List_digits[-1]
tens = List_digits[-2]
hundreds = List_digits[-3]
thousands = List_digits[-4]
man = List_digits[-5]

#"man" is 10,000 in Japanese

# print(man, " = Ten Thousands")
# print(thousands, " = Thousands")
# print(hundreds, " = Hundreds")
# print(tens, " = Tens")
# print(units, " = Units")

# Define the planes and that it is 3D
fig = plt.figure()
ax = Axes3D(fig)

# set initial Elevation and Azimuth view for the 3d graph
ax.view_init(15, -60)

# Set size for xyz space
ax.set_xlim3d(-150, 150)
ax.set_ylim3d(-150, 150)
ax.set_zlim3d(-150, 150)
# ax = fig.add_subplot(111, projection='3d')

# Structure of the matrix to represent Cistercian numbers, e.g. 11 to  2 is a straight line.
# 1  2  3
# 4  5  6
# 7  8  9
# 10 11  12
# + sagittal plane #13 at height #5 and #14 at height #8

P1 = (-40, 0, 120)
P2 = (0, 0, 120)
P3 = (40, 0, 120)
P4 = (-40, 0, 80)
P5 = (0, 0, 80)
P6 = (40, 0, 80)
P7 = (-40, 0, 40)
P8 = (0, 0, 40)
P9 = (40, 0, 40)
P10 = (-40, 0, 0)
P11 = (0, 0, 0)
P12 = (40, 0, 0)
P13 = (0, -40, 80)
P14 = (0, -40, 40)


# Center Points
def p11():
    ax.scatter(0, 0, 0, color='k', lw=1)


def p8():
    ax.scatter(0, 0, 40, color='k', lw=1)


def p5():
    ax.scatter(0, 0, 80, color='k', lw=1)


def p2():
    ax.scatter(0, 0, 120, color='k', lw=1)


p11()
p8()
p5()
p2()


# Sagittal Plane Points
def p13():
    ax.scatter(0, -40, 80, color='steelblue')


def p14():
    ax.scatter(0, -40, 40, color='steelblue')


p13()
p14()


# Thousands Points
def p7():
    ax.scatter(-40, 0, 40, color='slategrey', lw=1)


def p10():
    ax.scatter(-40, 0, 0, color='slategrey', lw=1)


p7()
p10()


# Hundreds Points
def p9():
    ax.scatter(40, 0, 40, color='seagreen', lw=1)


def p12():
    ax.scatter(40, 0, 0, color='seagreen', lw=1)


p9()
p12()


# Tens Points
def p1():
    ax.scatter(-40, 0, 120, color='darkgoldenrod', lw=1)


def p4():
    ax.scatter(-40, 0, 80, color='darkgoldenrod', lw=1)


p1()
p4()


# Units Points
def p3():
    ax.scatter(40, 0, 120, color='darkcyan', lw=1)


def p6():
    ax.scatter(40, 0, 80, color='darkcyan', lw=1)


p3()
p6()

p11()
p10()
# Draw center column
x_valuesCenter = [P11[0], P2[0]]
y_valuesCenter = [P11[1], P2[1]]
z_valuesCenter = [P11[2], P2[2]]
plt.plot(x_valuesCenter, y_valuesCenter, z_valuesCenter, color='k', lw=3)

userguess = Cistercian

# def ContinueTillFailure():
#     while userguess==Cistercian:

if man == 1:
    x_values1m = [P8[0], P14[0]]
    y_values1m = [P8[1], P14[1]]
    z_values1m = [P8[2], P14[2]]
    plt.plot(x_values1m, y_values1m, z_values1m, color='k', lw=3)
elif man == 2:
    x_values2m = [P5[0], P13[0]]
    y_values2m = [P5[1], P13[1]]
    z_values2m = [P5[2], P13[2]]
    plt.plot(x_values2m, y_values2m, z_values2m, color='k', lw=3)
elif man == 3:
    x_values3m = [P13[0], P8[0]]
    y_values3m = [P13[1], P8[1]]
    z_values3m = [P13[2], P8[2]]
    plt.plot(x_values3m, y_values3m, z_values3m, color='k', lw=3)
elif man == 4:
    x_values4m = [P5[0], P14[0]]
    y_values4m = [P5[1], P14[1]]
    z_values4m = [P5[2], P14[2]]
    plt.plot(x_values4m, y_values4m, z_values4m, color='k', lw=3)
elif man == 5:
    x_values5m = [P5[0], P14[0]]
    y_values5m = [P5[1], P14[1]]
    z_values5m = [P5[2], P14[2]]
    plt.plot(x_values5m, y_values5m, z_values5m, color='k', lw=3)
    x_values5mb = [P14[0], P8[0]]
    y_values5mb = [P14[1], P8[1]]
    z_values5mb = [P14[2], P8[2]]
    plt.plot(x_values5mb, y_values5mb, z_values5mb, color='k', lw=3)
elif man == 6:
    x_values6m = [P13[0], P14[0]]
    y_values6m = [P13[1], P14[1]]
    z_values6m = [P13[2], P14[2]]
    plt.plot(x_values6m, y_values6m, z_values6m, color='k', lw=3)
elif man == 7:
    x_values7m = [P13[0], P14[0]]
    y_values7m = [P13[1], P14[1]]
    z_values7m = [P13[2], P14[2]]
    plt.plot(x_values7m, y_values7m, z_values7m, color='k', lw=3)
    x_values7mb = [P14[0], P8[0]]
    y_values7mb = [P14[1], P8[1]]
    z_values7mb = [P14[2], P8[2]]
    plt.plot(x_values7mb, y_values7mb, z_values7mb, color='k', lw=3)
elif man == 8:
    x_values8m = [P13[0], P14[0]]
    y_values8m = [P13[1], P14[1]]
    z_values8m = [P13[2], P14[2]]
    plt.plot(x_values8m, y_values8m, z_values8m, color='k', lw=3)
    x_values8mb = [P5[0], P13[0]]
    y_values8mb = [P5[1], P13[1]]
    z_values8mb = [P5[2], P13[2]]
    plt.plot(x_values8mb, y_values8mb, z_values8mb, color='k', lw=3)
elif man == 9:
    x_values9m = [P13[0], P14[0]]
    y_values9m = [P13[1], P14[1]]
    z_values9m = [P13[2], P14[2]]
    plt.plot(x_values9m, y_values9m, z_values9m, color='k', lw=3)
    x_values9mb = [P5[0], P13[0]]
    y_values9mb = [P5[1], P13[1]]
    z_values9mb = [P5[2], P13[2]]
    plt.plot(x_values9mb, y_values9mb, z_values9mb, color='k', lw=3)
    x_values9mc = [P14[0], P8[0]]
    y_values9mc = [P14[1], P8[1]]
    z_values9mc = [P14[2], P8[2]]
    plt.plot(x_values9mc, y_values9mc, z_values9mc, color='k', lw=3)
else:
    p13()
# ## Draw corresponding Cistercian coordinates for thousands
if thousands == 1:
    x_values1k = [P11[0], P10[0]]
    y_values1k = [P11[1], P10[1]]
    z_values1k = [P11[2], P10[2]]
    plt.plot(x_values1k, y_values1k, z_values1k, color='k', lw=3)
elif thousands == 2:
    x_values2k = [P8[0], P7[0]]
    y_values2k = [P8[1], P7[1]]
    z_values2k = [P8[2], P7[2]]
    plt.plot(x_values2k, y_values2k, z_values2k, color='k', lw=3)
elif thousands == 3:
    x_values3k = [P11[0], P7[0]]
    y_values3k = [P11[1], P7[1]]
    z_values3k = [P11[2], P7[2]]
    plt.plot(x_values3k, y_values3k, z_values3k, color='k', lw=3)
elif thousands == 4:
    x_values4k = [P8[0], P10[0]]
    y_values4k = [P8[1], P10[1]]
    z_values4k = [P8[2], P10[2]]
    plt.plot(x_values4k, y_values4k, z_values4k, color='k', lw=3)
elif thousands == 5:
    x_values5k = [P8[0], P10[0]]
    y_values5k = [P8[1], P10[1]]
    z_values5k = [P8[2], P10[2]]
    plt.plot(x_values5k, y_values5k, z_values5k, color='k', lw=3)
    x_values5kb = [P11[0], P10[0]]
    y_values5kb = [P11[1], P10[1]]
    z_values5kb = [P11[2], P10[2]]
    plt.plot(x_values5kb, y_values5kb, z_values5kb, color='k', lw=3)
elif thousands == 6:
    x_values6k = [P7[0], P10[0]]
    y_values6k = [P7[1], P10[1]]
    z_values6k = [P7[2], P10[2]]
    plt.plot(x_values6k, y_values6k, z_values6k, color='k', lw=3)
elif thousands == 7:
    x_values7k = [P7[0], P10[0]]
    y_values7k = [P7[1], P10[1]]
    z_values7k = [P7[2], P10[2]]
    plt.plot(x_values7k, y_values7k, z_values7k, color='k', lw=3)
    x_values7kb = [P11[0], P10[0]]
    y_values7kb = [P11[1], P10[1]]
    z_values7kb = [P11[2], P10[2]]
    plt.plot(x_values7kb, y_values7kb, z_values7kb, color='k', lw=3)
elif thousands == 8:
    x_values8k = [P7[0], P10[0]]
    y_values8k = [P7[1], P10[1]]
    z_values8k = [P7[2], P10[2]]
    plt.plot(x_values8k, y_values8k, z_values8k, color='k', lw=3)
    x_values8kb = [P7[0], P8[0]]
    y_values8kb = [P7[1], P8[1]]
    z_values8kb = [P7[2], P8[2]]
    plt.plot(x_values8kb, y_values8kb, z_values8kb, color='k', lw=3)
elif thousands == 9:
    x_values9k = [P7[0], P10[0]]
    y_values9k = [P7[1], P10[1]]
    z_values9k = [P7[2], P10[2]]
    plt.plot(x_values9k, y_values9k, z_values9k, color='k', lw=3)
    x_values9kb = [P7[0], P8[0]]
    y_values9kb = [P7[1], P8[1]]
    z_values9kb = [P7[2], P8[2]]
    plt.plot(x_values9kb, y_values9kb, z_values9kb, color='k', lw=3)
    x_values9kc = [P10[0], P11[0]]
    y_values9kc = [P10[1], P11[1]]
    z_values9kc = [P10[2], P11[2]]
    plt.plot(x_values9kc, y_values9kc, z_values9kc, color='k', lw=3)
else:
    p10()

if hundreds == 1:
    x_values1c = [P11[0], P12[0]]
    y_values1c = [P11[1], P12[1]]
    z_values1c = [P11[2], P12[2]]
    plt.plot(x_values1c, y_values1c, z_values1c, color='k', lw=3)
elif hundreds == 2:
    x_values2c = [P8[0], P9[0]]
    y_values2c = [P8[1], P9[1]]
    z_values2c = [P8[2], P9[2]]
    plt.plot(x_values2c, y_values2c, z_values2c, color='k', lw=3)
elif hundreds == 3:
    x_values3c = [P11[0], P9[0]]
    y_values3c = [P11[1], P9[1]]
    z_values3c = [P11[2], P9[2]]
    plt.plot(x_values3c, y_values3c, z_values3c, color='k', lw=3)
elif hundreds == 4:
    x_values4c = [P8[0], P12[0]]
    y_values4c = [P8[1], P12[1]]
    z_values4c = [P8[2], P12[2]]
    plt.plot(x_values4c, y_values4c, z_values4c, color='k', lw=3)
elif hundreds == 5:
    x_values5c = [P8[0], P12[0]]
    y_values5c = [P8[1], P12[1]]
    z_values5c = [P8[2], P12[2]]
    plt.plot(x_values5c, y_values5c, z_values5c, color='k', lw=3)
    x_values5cb = [P11[0], P12[0]]
    y_values5cb = [P11[1], P12[1]]
    z_values5cb = [P11[2], P12[2]]
    plt.plot(x_values5cb, y_values5cb, z_values5cb, color='k', lw=3)
elif hundreds == 6:
    x_values6c = [P9[0], P12[0]]
    y_values6c = [P9[1], P12[1]]
    z_values6c = [P9[2], P12[2]]
    plt.plot(x_values6c, y_values6c, z_values6c, color='k', lw=3)
elif hundreds == 7:
    x_values7c = [P11[0], P12[0]]
    y_values7c = [P11[1], P12[1]]
    z_values7c = [P11[2], P12[2]]
    plt.plot(x_values7c, y_values7c, z_values7c, color='k', lw=3)
    x_values7cb = [P12[0], P9[0]]
    y_values7cb = [P12[1], P9[1]]
    z_values7cb = [P12[2], P9[2]]
    plt.plot(x_values7cb, y_values7cb, z_values7cb, color='k', lw=3)
elif hundreds == 8:
    x_values8c = [P12[0], P9[0]]
    y_values8c = [P12[1], P9[1]]
    z_values8c = [P12[2], P9[2]]
    plt.plot(x_values8c, y_values8c, z_values8c, color='k', lw=3)
    x_values8cb = [P8[0], P9[0]]
    y_values8cb = [P8[1], P9[1]]
    z_values8cb = [P8[2], P9[2]]
    plt.plot(x_values8cb, y_values8cb, z_values8cb, color='k', lw=3)
elif hundreds == 9:
    x_values9c = [P12[0], P9[0]]
    y_values9c = [P12[1], P9[1]]
    z_values9c = [P12[2], P9[2]]
    plt.plot(x_values9c, y_values9c, z_values9c, color='k', lw=3)
    x_values9cb = [P12[0], P11[0]]
    y_values9cb = [P12[1], P11[1]]
    z_values9cb = [P12[2], P11[2]]
    plt.plot(x_values9cb, y_values9cb, z_values9cb, color='k', lw=3)
    x_values9cc = [P9[0], P8[0]]
    y_values9cc = [P9[1], P8[1]]
    z_values9cc = [P9[2], P8[2]]
    plt.plot(x_values9cc, y_values9cc, z_values9cc, color='k', lw=3)
else:
    p12()

if tens == 1:
    x_values1t = [P1[0], P2[0]]
    y_values1t = [P1[1], P2[1]]
    z_values1t = [P1[2], P2[2]]
    plt.plot(x_values1t, y_values1t, z_values1t, color='k', lw=3)
elif tens == 2:
    x_values2t = [P5[0], P4[0]]
    y_values2t = [P5[1], P4[1]]
    z_values2t = [P5[2], P4[2]]
    plt.plot(x_values2t, y_values2t, z_values2t, color='k', lw=3)
elif tens == 3:
    x_values3t = [P2[0], P4[0]]
    y_values3t = [P2[1], P4[1]]
    z_values3t = [P2[2], P4[2]]
    plt.plot(x_values3t, y_values3t, z_values3t, color='k', lw=3)
elif tens == 4:
    x_values4t = [P1[0], P5[0]]
    y_values4t = [P1[1], P5[1]]
    z_values4t = [P1[2], P5[2]]
    plt.plot(x_values4t, y_values4t, z_values4t, color='k', lw=3)
elif tens == 5:
    x_values5t = [P1[0], P2[0]]
    y_values5t = [P1[1], P2[1]]
    z_values5t = [P1[2], P2[2]]
    plt.plot(x_values5t, y_values5t, z_values5t, color='k', lw=3)
    x_values5tb = [P1[0], P5[0]]
    y_values5tb = [P1[1], P5[1]]
    z_values5tb = [P1[2], P5[2]]
    plt.plot(x_values5tb, y_values5tb, z_values5tb, color='k', lw=3)
elif tens == 6:
    x_values6t = [P1[0], P4[0]]
    y_values6t = [P1[1], P4[1]]
    z_values6t = [P1[2], P4[2]]
    plt.plot(x_values6t, y_values6t, z_values6t, color='k', lw=3)
elif tens == 7:
    x_values7t = [P1[0], P2[0]]
    y_values7t = [P1[1], P2[1]]
    z_values7t = [P1[2], P2[2]]
    plt.plot(x_values7t, y_values7t, z_values7t, color='k', lw=3)
    x_values7tb = [P1[0], P4[0]]
    y_values7tb = [P1[1], P4[1]]
    z_values7tb = [P1[2], P4[2]]
    plt.plot(x_values7tb, y_values7tb, z_values7tb, color='k', lw=3)
elif tens == 8:
    x_values8t = [P4[0], P1[0]]
    y_values8t = [P4[1], P1[1]]
    z_values8t = [P4[2], P1[2]]
    plt.plot(x_values8t, y_values8t, z_values8t, color='k', lw=3)
    x_values8tb = [P5[0], P4[0]]
    y_values8tb = [P5[1], P4[1]]
    z_values8tb = [P5[2], P4[2]]
    plt.plot(x_values8tb, y_values8tb, z_values8tb, color='k', lw=3)
elif tens == 9:
    x_values9t = [P4[0], P1[0]]
    y_values9t = [P4[1], P1[1]]
    z_values9t = [P4[2], P1[2]]
    plt.plot(x_values9t, y_values9t, z_values9t, color='k', lw=3)
    x_values9tb = [P5[0], P4[0]]
    y_values9tb = [P5[1], P4[1]]
    z_values9tb = [P5[2], P4[2]]
    plt.plot(x_values9tb, y_values9tb, z_values9tb, color='k', lw=3)
    x_values9tc = [P1[0], P2[0]]
    y_values9tc = [P1[1], P2[1]]
    z_values9tc = [P1[2], P2[2]]
    plt.plot(x_values9tc, y_values9tc, z_values9tc, color='k', lw=3)
else:
    p1()

if units == 1:
    x_values1u = [P3[0], P2[0]]
    y_values1u = [P3[1], P2[1]]
    z_values1u = [P3[2], P2[2]]
    plt.plot(x_values1u, y_values1u, z_values1u, color='k', lw=3)
elif units == 2:
    x_values2u = [P5[0], P6[0]]
    y_values2u = [P5[1], P6[1]]
    z_values2u = [P5[2], P6[2]]
    plt.plot(x_values2u, y_values2u, z_values2u, color='k', lw=3)
elif units == 3:
    x_values3u = [P2[0], P6[0]]
    y_values3u = [P2[1], P6[1]]
    z_values3u = [P2[2], P6[2]]
    plt.plot(x_values3u, y_values3u, z_values3u, color='k', lw=3)
elif units == 4:
    x_values4u = [P3[0], P5[0]]
    y_values4u = [P3[1], P5[1]]
    z_values4u = [P3[2], P5[2]]
    plt.plot(x_values4u, y_values4u, z_values4u, color='k', lw=3)
elif units == 5:
    x_values5u = [P3[0], P2[0]]
    y_values5u = [P3[1], P2[1]]
    z_values5u = [P3[2], P2[2]]
    plt.plot(x_values5u, y_values5u, z_values5u, color='k', lw=3)
    x_values5ub = [P3[0], P5[0]]
    y_values5ub = [P3[1], P5[1]]
    z_values5ub = [P3[2], P5[2]]
    plt.plot(x_values5ub, y_values5ub, z_values5ub, color='k', lw=3)
elif units == 6:
    x_values6u = [P3[0], P6[0]]
    y_values6u = [P3[1], P6[1]]
    z_values6u = [P3[2], P6[2]]
    plt.plot(x_values6u, y_values6u, z_values6u, color='k', lw=3)
elif units == 7:
    x_values7u = [P2[0], P3[0]]
    y_values7u = [P2[1], P3[1]]
    z_values7u = [P2[2], P3[2]]
    plt.plot(x_values7u, y_values7u, z_values7u, color='k', lw=3)
    x_values7ub = [P3[0], P6[0]]
    y_values7ub = [P3[1], P6[1]]
    z_values7ub = [P3[2], P6[2]]
    plt.plot(x_values7ub, y_values7ub, z_values7ub, color='k', lw=3)
elif units == 8:
    x_values8u = [P3[0], P6[0]]
    y_values8u = [P3[1], P6[1]]
    z_values8u = [P3[2], P6[2]]
    plt.plot(x_values8u, y_values8u, z_values8u, color='k', lw=3)
    x_values8ub = [P5[0], P6[0]]
    y_values8ub = [P5[1], P6[1]]
    z_values8ub = [P5[2], P6[2]]
    plt.plot(x_values8ub, y_values8ub, z_values8ub, color='k', lw=3)
elif units == 9:
    x_values9u = [P3[0], P6[0]]
    y_values9u = [P3[1], P6[1]]
    z_values9u = [P3[2], P6[2]]
    plt.plot(x_values9u, y_values9u, z_values9u, color='k', lw=3)
    x_values9ub = [P5[0], P6[0]]
    y_values9ub = [P5[1], P6[1]]
    z_values9ub = [P5[2], P6[2]]
    plt.plot(x_values9ub, y_values9ub, z_values9ub, color='k', lw=3)
    x_values9uc = [P3[0], P2[0]]
    y_values9uc = [P3[1], P2[1]]
    z_values9uc = [P3[2], P2[2]]
    plt.plot(x_values9uc, y_values9uc, z_values9uc, color='k', lw=3)
else:
    plt.show()


# Center Points
def p11():
    ax.scatter(0, 0, 0, color='k', lw=1)


def p8():
    ax.scatter(0, 0, 40, color='k', lw=1)


def p5():
    ax.scatter(0, 0, 80, color='k', lw=1)


def p2():
    ax.scatter(0, 0, 120, color='k', lw=1)


p11()
p8()
p5()
p2()


# Sagittal Plane Points
def p13():
    ax.scatter(0, -40, 80, color='steelblue')


def p14():
    ax.scatter(0, -40, 40, color='steelblue')


p13()
p14()


# Thousands Points
def p7():
    ax.scatter(-40, 0, 40, color='slategrey', lw=1)


def p10():
    ax.scatter(-40, 0, 0, color='slategrey', lw=1)


p7()
p10()


# Hundreds Points
def p9():
    ax.scatter(40, 0, 40, color='seagreen', lw=1)


def p12():
    ax.scatter(40, 0, 0, color='seagreen', lw=1)


p9()
p12()


# Tens Points
def p1():
    ax.scatter(-40, 0, 120, color='darkgoldenrod', lw=1)


def p4():
    ax.scatter(-40, 0, 80, color='darkgoldenrod', lw=1)


p1()
p4()

# Units Points


def p3():
    ax.scatter(40, 0, 120, color='darkcyan', lw=1)


def p6():
    ax.scatter(40, 0, 80, color='darkcyan', lw=1)


p3()
p6()

# define two points, create lists of xyz values, and plot a line between them

# ax.set_xlabel("X-Axis")
# ax.set_ylabel("Y-Axis")
# ax.set_zlabel("Z-Axis")

# from pylab import rcParams
# rcParams['figure.figsize'] = 20, 20

#hide axis values by setting them to blank []
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
ax.axes.zaxis.set_ticklabels([])
ax.set_title("3D Cistercian Numerals (Sagittal for 10k)")




plt.show()
plt.savefig('/Users/gfabr/Pictures/HalfFailedIfBlank%s.png')

import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
prompt = simpledialog.askstring(title="Test",
                                  prompt="What's your best guess?:")

# https://matplotlib.org/stable/gallery/color/named_colors.html

# userguess = int(input("Best guess ? :"))
userguess = int(prompt)

print(f"{userguess:,}")
print(f"{Cistercian:,}")

from termcolor import colored
if userguess==Cistercian:
    print(colored("correct", 'green'))
else:
    print(colored("not quite", 'red'))

# to do
# simplify recurring code
# do you want to save ? (y/n)
# save graph to a png file
# dynamically name the save file .png to include the number created
# increment, track how many you got right in a row





