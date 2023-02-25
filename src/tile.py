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

from pygame.math import Vector2 as Vector

class Tile(object):
    """ Collideable, non-moveable tile object """
    def __init__(self, spawn_position: Vector):
        self.surface = pygame.Surface(100, 100)
        self.surface.fill((0, 0, 0, 255))
        self.rect = pygame.Rect(100, 100, spawn_position.x, spawn_position.y)

    def draw(self, surface):
        """ Draws tile to surface at rect position """
        surface.blit(self.surface, self.rect)
