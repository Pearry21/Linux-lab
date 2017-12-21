import click
import requests
import sys

from PIL import Image
try:
    from StringIO import StringIO
except: # when using python3.x
    from io import BytesIO, StringIO
from bs4 import BeautifulSoup

@click.command()
@click.argument('src', nargs=-1)
#@click.argument('dst', nargs=1)
def main(src):
    	"""Get Poster Movie"""
	name=""	
	for fn in src:
        	name+='%s' % (fn)+" "
	#name+='%s'%(dst)
	url='https://www.vojkudee.net/{}'.format(name.replace(" ",""))
	html=requests.get(url)
	beau=BeautifulSoup(html.content,'html.parser')
	poster=beau.find_all('div',{'class':'image-featured'})[0].img['data-lazy-src']
 	
	req=requests.get(poster)
	img=Image.open(StringIO(req.content))
	img.show()
