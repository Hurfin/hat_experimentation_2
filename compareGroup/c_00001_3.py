import pandas as pd
path1 = r"E:\FengXu\result\compareGroupData\paperID_authorID_affiliationID_paperYear(JQ_Co).txt"
path2 = r"E:\FengXu\result\compareGroupData\tmp\Jieqing_authorID.txt"
pathout = r'E:\FengXu\result\compareGroupData\paperID_authorID_affiliationID_paperYear(Co).txt'
# names1 = ['paperID', 'authorID', 'affiliationID', 'paperYear']
# names2 = ['authorID']
# data1 = pd.read_csv(path1, sep='\t', header=None, names=names1)
# data2 = pd.read_csv(path2, sep='\t', header=None, names=names2)
# data =
jieqing_authorID = set()
# authorID
with open(path2, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        jieqing_authorID.add(line)

fout = open(pathout, 'w', encoding='utf-8')
# paperID_authorID_affiliationID_paperYear(JQ_Co).txt
with open(path1, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split()
        if line[1] in jieqing_authorID:
            continue
        if len(line) != 4:
            continue
        fout.write('\t'.join(line)+'\n')
    pass
fout.close()
