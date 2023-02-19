fp = None
try:
    with open('myfile.txt') as f:
        for t in fp:
            print(t)
except Exception as e:
    print(e)
