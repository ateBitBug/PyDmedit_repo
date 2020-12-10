import subprocess
from sys import platform


'''
kiwis,4, a2
bananas,3,d2
apples, 4,e1
pears,1, c1
pears,1, c2
kiwis,4, a1
pears,1, c3
bananas,3,d3
pears,1, c4
oranges,2,b1
oranges,2,b2
bananas,3,d1
kiwis,4, a3
bananas,3,d4
'''


# https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
# https://thispointer.com/python-read-a-csv-file-line-by-line-with-or-without-header/
# https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/

# status = subprocess.call(['ls', '-l','/home/woof', '>', '/home/woof/ls.txt'])
# print("status: {}".format(status))
#

# https://queirozf.com/entries/python-3-subprocess-examples

if platform == "linux" or platform == "linux2":
  src = "/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/fruit.txt"
  des = "/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/output.txt"
elif platform == "win32":
  src = "d:/compilers/githubRepos/pydmedit-repos/data/fruit.txt"
  des = "d:/compilers/githubRepos/pydmedit-repos/data/output.txt"
else:
  src = "/Volumes/macExFat/compilers/gitRepo/pydmedit-repos/data/fruit.txt"
  des = "/Volumes/macExFat/compilers/gitRepo/pydmedit-repos/data/output.txt"


# status = subprocess.call(["sort","--field-separator=,", "--key=2,3", "-o", des, src])
# status = subprocess.call(["sort","--field-separator=,", "-k2,2", "-r", "-k3,3", "-o", des, src])
# status = subprocess.call(["sort","--field-separator=,", "-k2,2", "-k3,3", "-o", des, src])
# status = subprocess.call(["sort","--field-separator=,", "-k1,1", "-k2,2", "-s", "-o", des, src])
# status = subprocess.call(["sort", "-s", "--field-separator=,", "-k1,1", "-k2,2", "-o", des, src])
# status = subprocess.call(["sort", "-s", "--field-separator=,", "-k1,1", "-k2,2", src, "-o", des])


# status = subprocess.call(["sort", src, "-o", des, "-s", "--field-separator=,", "-k1,1", "-k2,2r"])
# status = subprocess.run(["sort", src, "-o", des, "-s", "--field-separator=,", "-k1,1", "-k2,2r"])

# status = subprocess.Popen(["sort", src, "-o", des, "--field-separator=,", "-k1,1", "-k2,2r"])
status = subprocess.Popen(["sort", src, "-o", des, "-s", "--field-separator=,", "-k1,1", "-k2,2r"])
r = status.wait()
print(f"you are not from repo test: {r}")

# p = subprocess.Popen(['ls', '-la'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# out, err = p.communicate()
# print(type(out))
# print(repr(out))
# l = out.split('\n')
# print(l)