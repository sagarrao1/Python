import re
# text_to_search='''
# 998-902-7590
# 994.922.6333
#
# 998*902*7590
# 994_922_6333
# ERROR
# '''
pattern = re.compile(r'ERROR')

with open('log.txt', 'r') as rf:
    with open('Write.txt', 'w') as wf:
        chunk_size = 1000
        rf_contents = rf.readline()
        while len(rf_contents) > 0:
            matches= pattern.finditer(rf_contents)
            for match in matches:
                wf.write(rf_contents)
                #print(rf_contents,end='')
            rf_contents = rf.readline()





# str = "The rain in Spain"
# x = re.search(r"\bS\w+", str)
# print()
