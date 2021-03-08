import io
import random
import math

text = """<svg width="300" height="300" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="background-color: black">"""
count = 1000


def gen_circ(i, angle, offset):
    t = """<circle id=\"c""" + str(i)
    t += """\" r="0" cx="50" cy="50" fill="orange"/>\n"""
    t += """<animate 
    xlink:href=\"#c""" + str(i) + """\"
    attributeName="r"
    from="0"
    to="5" 
    dur="60s"
    begin=\"""" + str(offset) + """s\"
    fill="freeze"
    repeatCount="indefinite" />\n"""
    t += """<animate 
    xlink:href=\"#c""" + str(i) + """\"
    attributeName="cx"
    from="50"
    to=\"""" + str(50 + 1000 * math.cos(angle)) + """\" 
    dur="60s"
    begin=\"""" + str(offset) + """s\"
    fill="freeze"
    repeatCount="indefinite" />\n"""
    t += """<animate 
    xlink:href=\"#c""" + str(i) + """\"
    attributeName="cy"
    from="50"
    to=\"""" + str(50 + 1000 * math.sin(angle)) + """\" 
    dur="60s"
    begin=\"""" + str(offset) + """s\"
    fill="freeze"
    repeatCount="indefinite" />\n"""
    return t


star_angles = [random.uniform(0, 2 * 3.1415) for i in range(count)]
star_offsets = [random.uniform(0, 600) for i in range(count)]

for i in range(count):
    text += gen_circ(i, star_angles[i], star_offsets[i])

text += "</svg>"

with open("produced.svg", 'w') as file:
    file.write(text)
