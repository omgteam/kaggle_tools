from os import listdir
from os.path import isfile, isdir

def count_samples(dataDir):
  """
  Count number of files in each subdirectory in dataDir.
  """
  assert(isdir(dataDir))
  filenames = [f for f in listdir(dataDir)]
  class_count = {}
  for f in filenames:
    path = dataDir+"/"+f
    if isdir(path):
      class_count[f] = len(listdir(path))

  for k in class_count:
    print "class:%s\tcount:%d"%(k,class_count[k])

def test_count_samples():
  count_samples("/root")

if __name__ == "__main__":
  test_count_samples()
