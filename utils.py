def find_olymp(stduent_class,level,subject):
    with open('olymps.txt','r',encoding='utf-8') as file:
        search_results = []
        for f in file.readlines():
            temp = f.split(',')
            lower_c = int(temp[3].lstrip().strip().split(' ')[0].split('-')[0])
            upper_c = int(temp[3].lstrip().strip().split(' ')[0].split('-')[1])
            subj = temp[4].strip().lstrip()
            lvl = temp[2]
            if (level in lvl or level=='all') and (lower_c<=int(stduent_class)<=upper_c) and subject==subj:
                search_results.append(' - '.join([temp[0].lstrip('0123456789.- '),(lvl if level=='all' else ''),temp[1]]))
        return search_results
if __name__=='__main__':
    print(find_olymp('11','3','информатика'))