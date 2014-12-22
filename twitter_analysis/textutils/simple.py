#!/usr/bin/env python2
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open(r"C:\Users\Allan\Desktop\PYTHON_TESTING\constitution.txt") as f:
    lines = f.readlines()                                                                            
text = "".join(lines)  

wordcloud = WordCloud().generate(text)
# Open a plot of the generated image.
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
