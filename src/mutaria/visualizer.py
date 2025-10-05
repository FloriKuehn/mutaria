"""
visualizer.py

Defines the Visualizer class, which handles the graphical representation
of the simulation using pillow and imageio.
"""

import numpy as np
from PIL import Image, ImageDraw
import imageio


class Visualizer:
    """
    Handles the graphical representation of the simulation.
    """

    def __init__(
            self,
            video_out_path: str,
            cell_size: int = 8,
            fps: int = 10
            ):
        """
        Initializes the visualizer.

        Args:
            video_out_path (str): Path to save the output video.
            cell_size (int): Size of each cell in pixels.
            fps (int): Frames per second for the output video.
        """
        self.writer = imageio.get_writer(video_out_path, fps=fps)
        self.cell_size = cell_size

    def render_step(self, world, generation: int = 0, step: int = 0):
        """
        Renders the current state of the world and adds it to the video.

        Args:
            world: The world object containing the grid and agents.
        """
        img_width = world.width * self.cell_size
        img_height = world.height * self.cell_size
        image = Image.new("RGB", (img_width, img_height), "white")
        draw = ImageDraw.Draw(image)

        for y in range(world.height):
            for x in range(world.width):
                top_left = (x * self.cell_size,
                            y * self.cell_size)
                bottom_right = ((x + 1) * self.cell_size,
                                (y + 1) * self.cell_size)
                draw.rectangle([top_left, bottom_right], outline="black")

                agent = world.grid[y, x]
                if agent is not None:
                    agent_color = (0, 0, 255)  # Blue for agents
                    draw.ellipse([top_left, bottom_right], fill=agent_color)

        draw.text((10, 10), f"Gen: {generation} Step: {step}", fill="black")

        self.writer.append_data(np.array(image))

    def close(self):
        """
        Finalizes and saves the video file.
        """
        self.writer.close()
