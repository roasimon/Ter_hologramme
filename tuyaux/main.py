import pickle
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from tuyautemp import getSatVectors
from recadrage import changePerspecAllImages, resizeAllImages

def show_figure(fig):
    # create a dummy figure and use its
    # manager to display "fig"  
    dummy = plt.figure()
    new_manager = dummy.canvas.manager
    new_manager.canvas.figure = fig
    fig.set_canvas(new_manager.canvas)

def show_plt(file: str):
    with open(file, 'rb') as f:
        fig = pickle.load(f)
    show_figure(fig)

if __name__ == '__main__':
    for i in range(1, 51):
        im_dir = os.listdir(f"warped_resize\psp{i}")
        vec_holo, vec_non_holo = getSatVectors(im_dir, "holo_mask_erod", "holo_mask_dilat", 500, 150)


