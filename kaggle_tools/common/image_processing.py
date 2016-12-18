from PIL import Image
from os import listdir
from os.path import isdir
import numpy as np

def get_imagesize(imagePath):
  with Image.open(imagePath) as im:
    width, height = im.size
    arr = np.asarray(im)
    return (width, height, arr.mean(axis=0).mean(axis=0))

def get_dir_imagesize(imageDir):
  if not isdir(imageDir):
    return "%s is not a dir"%(imageDir)
  images = [f for f in listdir(imageDir)]
  widths = []
  heights = []
  R = []
  G = []
  B = []
  for img in images:
    size = get_imagesize(imageDir+"/"+img)
    widths.append(size[0])
    heights.append(size[1])
    RGB = size[2]
    R.append(RGB[0])
    G.append(RGB[1])
    B.append(RGB[2])
  widths = np.asarray(widths)
  heights = np.asarray(heights)
  R = np.asarray(R)
  G = np.asarray(G)
  B = np.asarray(B)
  labels = ["width", "height", "R", "G", "B"]
  txts = ["average:%f\tstd:%f"%(x.mean(), x.std()) for x in [widths, heights, R, G, B]]
  res = "\n\t\t".join([x[0]+"\t"+x[1] for x in zip(labels, txts)])
  return "\n\t\t" + res

def get_2dir_imagesize(imageDir):
  if not isdir(imageDir):
    return "%s is not a dir"%(imageDir)
  dirs = [f for f in listdir(imageDir) if isdir(imageDir+"/"+f)]
  for imgDir in dirs:
    print "class:%s\n%s"%(imgDir, get_dir_imagesize(imageDir+"/"+imgDir))
  

if __name__ == "__main__":
  print get_dir_imagesize("/root/competition/kaggle/fish/data/test_stg1")
#  print get_2dir_imagesize("/root/competition/kaggle/fish/data/train")
