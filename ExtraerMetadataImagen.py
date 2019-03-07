import argparse
from PIL import Image
from PIL.ExifTags import TAGS

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image',
  required=True, type=str, help='Image')

args = parser.parse_args()
img = Image.open(args.image)
exif = img._getexif()

try:
  for (k,v) in exif.iteritems():
    print '%s = %s'(TAGS.get(k), v)
except:
  print "Metadata not found!"