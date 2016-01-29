import numpy
import matplotlib
from matplotlib import pylab, mlab, pyplot
from IPython.core.pylabtools import figsize, getfigs
from pylab import *
from numpy import *
import sys
import urllib
import cStringIO
from PIL import Image
import webbrowser
np = numpy
plt = pyplot

local_data_feed = 'W:/Python/QA_Tool/Data_Feed.csv'
# local_cat_entry_file = 'W:/Python/QA_Tool/CAV_TEST.csv'
# local_cat_entry_file = 'W:/Python/QA_Tool/updatesforkitchen.csv'
# local_cat_entry_file = 'W:/Python/QA_Tool/bathroomforQA_items.csv'
# local_cat_entry_file = 'W:/Archives/Complete Your Bathroom - Add to New Algorithm.csv'
# local_cat_entry_file = 'W:/Python/QA_Tool/Kitchen_Cabinets.csv'
# local_cat_entry_file = 'W:/Python/QA_Tool/Customers_Eventually_Bought.csv'
local_cat_entry_file = 'W:/Python/QA_Tool/lightingforQA_items.csv'

cat_entries = np.genfromtxt(local_data_feed, delimiter=',', dtype='i12', skiprows=1, usecols=[0])
cat2 = np.genfromtxt(local_cat_entry_file, delimiter=',', dtype='i9', skiprows=1, usecols=[0])


def on_pick(event):
    artist = event.artist
    webbrowser.open(artist.get_url())
    
if np.size(sys.argv) > 1:
    for k in range(np.size(sys.argv) - 1):
        condition1 = np.where(cat2 == int(sys.argv[1]))
        print condition1[0][0]
        with open(local_cat_entry_file, 'rb') as g:
            line_get = g.read().split('\n')[condition1[0][0] + 1].split('\n')[0]
            recs_for_host = line_get.split(',')
        
        fig, ax_arr = plt.subplots(np.size(recs_for_host), sharey=True)
        for i in range(np.size(recs_for_host)):
            print '\n' + recs_for_host[i]
            try:
                prod_id = int(recs_for_host[i])
                condition = np.where(cat_entries == prod_id)
                with open(local_data_feed, 'rb') as f:
                    wanted_line_1 = f.read().split('\n')[condition[0]+1].split('\n')[0]
                    
                print wanted_line_1
                prod_name = wanted_line_1.split(',')[1]
                prod_im_url = 'http://' + wanted_line_1.split('http://')[2].split(',')[0]
                prod_url = 'http://' + wanted_line_1.split('http://')[1].split(',')[0]
        
            # LOAD IMAGE FROM SITE
                img = Image.open(cStringIO.StringIO(urllib.urlopen(prod_im_url).read()))
                
            # FIGURE PARAMETERS
                ax_arr[i].imshow(img, picker=True, url=prod_url)
                ax_arr[i].set_title(prod_name)
                ax_arr[i].set_url(prod_url)
                ax_arr[i].axis('off')
            except:
                print str(prod_id) + ' not available.'
                ax_arr[i].axis('off')
        
        #    except:
        #        print sys.argv[i+1]+' was not found.'
        print '\nPress ctrl+C in this terminal to exit.'
        fig.subplots_adjust(hspace=.5)
        fig.canvas.mpl_connect('pick_event', on_pick)
        show()
        
else:
    for k in range(np.size(cat2)):
        condition1 = k
        with open(local_cat_entry_file, 'rb') as g:
            line_get = g.read().split('\n')[condition1+1].split('\n')[0]
            recs_for_host = line_get.split(',')
        
        fig, ax_arr = plt.subplots(np.size(recs_for_host), sharey=True)
        for i in range(np.size(recs_for_host)):
            print '\n'+recs_for_host[i]
            try:
                prod_id = int(recs_for_host[i])
                condition = np.where(cat_entries == prod_id)
                with open(local_data_feed, 'rb') as f:
                    wanted_line_1 = f.read().split('\n')[condition[0]+1].split('\n')[0]
                    
                print wanted_line_1
                prod_name = wanted_line_1.split(',')[1]
                prod_im_url = 'http://'+wanted_line_1.split('http://')[2].split(',')[0]
                prod_url = 'http://'+wanted_line_1.split('http://')[1].split(',')[0]
        
            # LOAD IMAGE FROM SITE
                img = Image.open(cStringIO.StringIO(urllib.urlopen(prod_im_url).read()))
                
            # FIGURE PARAMETERS
                ax_arr[i].imshow(img, picker=True, url=prod_url)
                ax_arr[i].set_title(prod_name)
                ax_arr[i].set_url(prod_url)
                ax_arr[i].axis('off')
            except:
                print str(recs_for_host[i]) + ' not available.'
                ax_arr[i].axis('off')
        
        #    except:
        #        print sys.argv[i+1]+' was not found.'
        print '\nPress ctrl+C in this terminal to exit, or close the image window to continue.'
        fig.subplots_adjust(hspace=.5)
        fig.canvas.mpl_connect('pick_event', on_pick)
        show()
