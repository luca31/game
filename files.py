def get_data(name):
  f = open("data/{}.txt".format(name), "r")
  d = f.read()
  f.close()
  return d

def put_data(name, d=""):
  f = open("data/{}.txt".format(name), "w")
  d = f.write(str(d))
  f.close()