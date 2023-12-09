import os
import numpy as np
from PIL import Image as im
import matplotlib.pyplot as plt
import sklearn.datasets as datasets

TEMPFILE = "temp.png"

num_peaks = 2
steps = 10
highlight_color =  'gold'
water_color = 'cornflowerblue'
background_color = '#042D59'

def create_standing_wave(title, num_peaks = 3, amplitude = 0.5, sea_floor = -2, highlight_wave = False):

    x = np.arange(0, num_peaks * 2* np.pi, 0.1);
    y = amplitude * np.sin(x - 2*np.pi) 
    bottom = np.ones(len(x)) * sea_floor; 
    
    fig, ax = plt.subplots(facecolor=background_color)
    plt.xlim(0, 1.8*np.pi * num_peaks)
    plt.ylim(sea_floor, amplitude+0.2)
    ax.grid(False)
    ax.axis('off')

    # Wave
    ax.fill_between(x,y,bottom,color = water_color)
    
    # Wave Edge
    if(highlight_wave):
        ax.plot(x, y,color = highlight_color, linewidth=7.0)  
    
    plt.savefig('{0}.png'.format(title),transparent=True)
    plt.close()



def create_transverse_wave(title, num_peaks = 3, steps = 15, amplitude = 0.5, sea_floor = -2, highlight_wave = False):

    images = []
    for n in range(int(steps)):
        frac = n/steps

        x = np.arange(0, num_peaks * 2* np.pi, 0.1);
        y = amplitude * np.sin(x - frac*2*np.pi) 
        bottom = np.ones(len(x)) * sea_floor; 
        
        fig, ax = plt.subplots(facecolor=background_color)
        plt.xlim(0, 1.8*np.pi * num_peaks)
        plt.ylim(sea_floor, amplitude+0.2)
        ax.grid(False)
        ax.axis('off')

        # Wave
        ax.fill_between(x,y,bottom,color = water_color)
        
        # Wave Edge
        if(highlight_wave):
            ax.plot(x, y,color = highlight_color, linewidth=7.0)  
        
        plt.savefig(TEMPFILE)
        plt.close()
        images.append(im.fromarray(np.asarray(im.open(TEMPFILE))))

    images[0].save(
        '{0}.gif'.format(title),
        optimize=False,
        save_all=True,
        append_images=images[1:],
        loop=0,
        duration=100,
    )

    os.remove(TEMPFILE)

def create_longitudinal_wave(title, num_peaks = 3, steps = 15, amplitude = 0.5, sea_floor = -2, highlight_wave = False):

    images = []
    for n in range(int(steps)):
        frac = n/steps

        x = np.arange(0, num_peaks * 2* np.pi, 0.1);
        y = amplitude * np.sin(x - 2*np.pi) 
        bottom = np.ones(len(x)) * sea_floor; 
        
        x = x + np.sin( 2 * np.pi *frac * x/(num_peaks * 2* np.pi))

        fig, ax = plt.subplots(facecolor=background_color)
        plt.xlim(0, 1.8*np.pi * num_peaks)
        plt.ylim(sea_floor, amplitude+0.2)
        # ax = fig.add_axes([0, 0, 1, 1])
        ax.grid(False)
        ax.axis('off')

        # Wave
        ax.fill_between(x,y,bottom,color = water_color)
        
        # Wave Edge
        if(highlight_wave):
            ax.plot(x, y,color = highlight_color, linewidth = '7.0')  
        
        plt.savefig(TEMPFILE)
        plt.close()
        images.append(im.fromarray(np.asarray(im.open(TEMPFILE))))

    images[0].save(
        '{0}.gif'.format(title),
        optimize=False,
        save_all=True,
        append_images=images[1:],
        loop=0,
        duration=100,
    )

    os.remove(TEMPFILE)

create_standing_wave('standing_highlight',highlight_wave=True)
create_standing_wave('standing',highlight_wave=False)

create_transverse_wave('transverse',highlight_wave=False)
create_transverse_wave('transverse_highlight',highlight_wave=True)

create_longitudinal_wave('longitudinal',highlight_wave=False)
create_longitudinal_wave('longitudinal_highlight',highlight_wave=True)

create_standing_wave('standing_shallow',highlight_wave=False, amplitude= 0.05, sea_floor= -1)
create_standing_wave('standing_medium',highlight_wave=False, amplitude= 0.1, sea_floor= -1)