import os
import pandas as pd

fpath = '/home/lyrax/Downloads/Kenya Integrated Household Budget Survey/'
for i in os.listdir(fpath):
	dta_format = pd.io.stata.read_stata(fpath + '{}'.format(i))
	df = dta_format.to_csv('/home/lyrax/Documents/Kenya Integrated Household Budget Survey/{}{}'.format(i, '.csv'))
