transform char_mid:
    zoom 0.5
    xalign 0.5
    yalign 0.1
    yoffset 80
    xoffset 20

transform char_right:
    zoom 0.5
    xalign 1.0
    yalign 0.1
    yoffset 80
    xoffset 80

transform char_left:
    zoom 0.5
    xalign 0.0
    yalign 0.1
    yoffset 80
    xoffset 200

transform char_c:
    zoom 0.75
    xalign 0.5
    yalign 0.1
    yoffset 90

transform cg0:
    zoom 0.5
    xalign 0.5
    yalign 0.5

transform cg1:
    xalign 0.5
    yalign 0.5

transform clue:
    zoom 0.9
    xalign 0.5
    yalign 0.5
    

init python:
    # change punch variable
    hpunch = Move((30, 0), (-30, 0), .50, bounce=True, repeat=True, delay=.275)
    vpunchs = Move((0, 10), (0, -10), 0.3, bounce=True, repeat=True, delay=.275)
    vpunchm = Move((0, 40), (0, -40), 0.2, bounce=True, repeat=True, delay=.275)
    shake = Move((70, 70), (-70, -70), 3, bounce=True, repeat=True, delay=.275)


transform shaking:
    linear 0.1 xoffset -2 yoffset 2 
    linear 0.1 xoffset 3 yoffset -3 
    linear 0.1 xoffset 2 yoffset -2
    linear 0.1 xoffset -3 yoffset 3
    linear 0.1 xoffset 0 yoffset 0
    repeat