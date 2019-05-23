
def person(name, **data):
    print(name)
    #print(data)

    for k,v in data.items():
        print(k,v)

person('Sagar',age=23,street='nizampet',city='hyd',pin='500090')
