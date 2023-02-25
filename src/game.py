"""
The MIT License (MIT)

Copyright (c) 2023 Joshua Rose

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the conditions attatched in the license file.
"""

import pygame
from size import Size

pygame.display.init()
_display = Size(800, 800)
display = pygame.display.set_mode(
        (_display.width, _display.height),
        pygame.SHOWN | pygame.DOUBLEBUF, 32)

clock = pygame.time.Clock()
_fps = 59.0
_run = True

while _run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _run = False

    display.fill((255, 255, 255, 255))
    pygame.display.update()
    clock.tick(_fps)

pygame.display.quit()
