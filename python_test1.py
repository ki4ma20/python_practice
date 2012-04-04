# definition of function "hoge"
def hoge():
    # loop
    for i in xrange(10):
        # print i, auto new line "add ',' not new line"
        print i

# this process is called when use as "python python_test.py"
if __name__=='__main__':
    hoge()
