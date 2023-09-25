import matplotlib.pyplot as plt
import matplotlib.image as img
import pandas as pd
import os
import os.path
from os import path
from IPython.core.display import display, HTML
import codecs

def selected_option(message):
    # reading png image file
    im = img.imread("../notebooks/solutions/"+ message + ".png")
    # show image
    #plt.imshow(im,  aspect='auto')
    fig, ax = plt.subplots(figsize=(15, 15))
    plt.axis('off')
    ax.imshow(im)
    #tight_layout()
######################################
def mlu_answer(message):
    # reading csv answer file
    df = pd.read_csv("../notebooks/solutions/"+ message + ".csv")
    return df
######################################
def answer_html(message):
    f=codecs.open("../notebooks/solutions/"+ message + ".html", 'r')
    display(HTML(f.read()))
    return