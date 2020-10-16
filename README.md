# GoblinMessenger

This python script is a program that will cipher a text message that you type and provide you a unique seed (key). This was designed after an idea I had as a child that my friend and I developed so we could pass secret notes in class. The general idea works around the idea of a grid that has a 'hole' in it which rotates around a central axis. This hole never matches up with another position that would also have a hole. This process of assigning a hole continues until there is no available grid to put a hole.

Using this method of holes in the grid, we put the user's message in the holes that are available in the grid and then rotate the grid which reveals new empty space in the circles. This process also repeats until all available holes have a letter assigned to them completing the entire grid.

The message is then reconstructed into a linear grid (read: single line sentence) and displayed to the user.
