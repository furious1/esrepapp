# --------------------svdata.py------------------------
# Function helper for saving and printing data to file
# The goal of this function is to add to debuging and design


def svdata(source, svobjf, svprf):
# Test
	import sys # needed for sys.stdout
	sys.stdout = open(svprf,'w')
	#print source[0].entries[0]

# Saving objects
	import pickle # needed for saving objects 
	with open(svobjf,'wb') as output:
        	pickle.dump(source[0], output, pickle.HIGHEST_PROTOCOL)
