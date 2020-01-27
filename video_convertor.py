# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 11:39:04 2019

@author: Shiv
"""

from moviepy.editor import *
clip=VideoFileClip() #Enter filename
video=CompositeVideoClip([clip])
video.write_videofile() #Enter Target filename with format extension
clip.close()
clip.reader.close()
clip.audio.reader.close_proc()

