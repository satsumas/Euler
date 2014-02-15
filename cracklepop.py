#! bin/usr/python

for i in range(101):
    if i % 3 == 0:
        if i % 5 == 0:
            print "Cracklepop"
        else:
            print "Pop"
    else:
        print str(i)

