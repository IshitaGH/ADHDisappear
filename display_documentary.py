import cv2
import numpy as np

import pyglet

# SHITS NOT WORKING BECAUSE IDK HOW TO SYNC VIDEO AND AUDIO

from lsl import pause_video

# set up video player
win_width = 640
win_height = 480
title = "Documentary"
window = pyglet.window.Window(win_width, win_height, title)
video_path = "remy_struggling.mp4"
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
media_load = pyglet.media.load(video_path)
player.queue(media_load)
player.play()

@window.event
def on_draw():
    window.clear()

    if player.source and player.source.video_format:
        player.get_texture().blit(0,0)

@window.event
def on_key_press(symbol, modifier):
    if symbol == pyglet.window.key.q:
        window.close()

event_loop = pyglet.app.EventLoop()
event_loop.run()


# OpenCV stuff that doesn't work because OpenCV only does video and not audio
# try:
#     # Creates the VideoCapture object that will display the documentary
#     # TODO: add path of the downloaded documentary here
#     cap = cv2.VideoCapture('remy_struggling.mp4')
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if ret:
#             # if concentration drops and you pause the video, then wait
#             # for person to do the CBT and manually restart the video by
#             # pressing any key
#             if pause_video():
#                 cv2.waitKey(-1)
#             cv2.imshow('Documentary', frame)
#             match cv2.pollKey():
#                 case 0x71:  # PRESS 'q' TO STOP!!
#                     cap.close()
#                     break
# except cv2.error as error:
#     print("[Error]: {}".format(error))

# cap.release()
# cv2.destroyAllWindows()