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
  src = "/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/hhlds.csv"
  des = "/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/nodup.csv"
elif platform == "win32":
  src = "d:/compilers/githubRepo/pydmedit-repos/data/hhlds.csv"
  des = "d:/compilers/githubRepo/pydmedit-repos/data/nodup.csv"
else:
  src = "/Volumes/macExFat/compilers/gitRepo/pydmedit-repos/data/hhlds.csv"
  des = "/Volumes/macExFat/compilers/gitRepo/pydmedit-repos/data/nodup.csv"


# status = subprocess.call(["sort","--field-separator=,", "--key=2,3", "-o", des, src])
# status = subprocess.call(["sort","--field-separator=,", "-k2,2", "-r", "-k3,3", "-o", des, src])
# status = subprocess.call(["sort","--field-separator=,", "-k2,2", "-k3,3", "-o", des, src])
# status = subprocess.call(["sort","--field-separator=,", "-k1,1", "-k2,2", "-s", "-o", des, src])
# status = subprocess.call(["sort", "-s", "--field-separator=,", "-k1,1", "-k2,2", "-o", des, src])
# status = subprocess.call(["sort", "-s", "--field-separator=,", "-k1,1", "-k2,2", src, "-o", des])


# status = subprocess.call(["sort", src, "-o", des, "-s", "--field-separator=,", "-k1,1", "-k2,2r"])
# status = subprocess.run(["sort", src, "-o", des, "-s", "--field-separator=,", "-k1,1", "-k2,2r"])

# status = subprocess.Popen(["sort", src, "-o", des, "--field-separator=,", "-k1,1", "-k2,2r"])


# Use a list of args instead of a string
'''*
  head -n 1 dup.csv > header.txt
  tail -n +2 dup.csv > body.txt
  cat body.txt >> header.txt
*'''
input_files = ['/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/hhlds.csv']
my_cmd = ['head', '-n', '1'] + input_files
with open('/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/header.txt', "w") as outfile:
    subprocess.run(my_cmd, stdout=outfile)

input_files = ['/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/hhlds.csv']
my_cmd = ['tail', '-n', '+2'] + input_files
with open('/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/body.txt', "w") as outfile:
    subprocess.run(my_cmd, stdout=outfile)

'''*
  to remove duplicate rows from the body
*'''
src = '/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/body.txt'
des = '/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/nodup-body.txt'
status = subprocess.Popen(["sort", src, "-o", des, "-u", "--field-separator=,"])
r = status.wait()
print(f"you are not from repo test: {r}")

'''*
  concatenates header and nodup-body
*'''
input_files = ['/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/nodup-body.txt']
my_cmd = ['cat'] + input_files
with open('/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/header.txt', "a") as outfile:
    subprocess.run(my_cmd, stdout=outfile)
