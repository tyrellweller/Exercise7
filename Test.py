def make_dictionary(**other):
    dict = {}
    for key , value in other.items():
        dict[key] = value
    return dict

dict = make_dictionary(name=['sian'] , age=[21] , skills = ['boxing' , 'coding'])
for key , value in dict.items():
    print(key)
    for v in value:
        print("\t" + str(v))