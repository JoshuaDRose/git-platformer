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
from pygame.math import Vector2 as Vector
from size import Size

class Player():
    spawn = Vector(400, 400)
    def __init__(self):
        name = "The Dude"
        size = Size(width=50, height=50)

    @staticmethod
    def render_name():
        """ Render name above player
            returns: N/A
        """
        ...

    def draw(self, surface):
        """ Draw player image to surface
            returns: N/A
        """

    def update(self):
        """ Update movement and collision
            returns: N/A
        """
