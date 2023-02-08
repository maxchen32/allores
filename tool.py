import os,re

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f.endswith('.txt'):
                fullname = os.path.join(root, f)
                yield fullname

def main():
    #base = './ores/'
    base = './'
    for i in findAllFile(base):
        #farr = re.split(r'\\|\.', i)
        #fpath = '.' + farr[1] + '/init.lua'
        #print(i, fpath)
        #os.rename(i ,fpath)
        #mname = 'allores_' + farr[-2]
        #content = '# textdomain: allores_' + mname + '\n\n' + mname + '=' + '\n'
        #content = 'depends = default\n'
        
        #with open(fpath, 'a', encoding="utf-8") as f:
        #    f.write(content)
        #os.makedirs(fpath)
        #print(fpath, mname, '\n',content)
        #alter(i , "allores(?=( =))", mname)
        #print(mname)
        alter(i, "allores_[A-Za-z0-9_]+", "")
    

def alter(file,old_str,new_str):
    pat = re.compile(old_str)
    with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
    #with open(file, "r", encoding="utf-8") as f1:
        for line in f1:
            raw = re.search(pat, line)
            if raw != None:
                #print(line)
                llow = raw.group().lower()
                #print(llow)
                f2.write(re.sub(pat, llow, line))
            else:
                #pass
                f2.write(line)
    os.remove(file)
    os.rename("%s.bak" % file, file)

def write_data_to_file(file: str, data: str, row: int = 1) -> None:
    """
    读取文件，在某一行插入。
    :param file: 读取文件路径
    :param data: 插入数据
    :param row: 插入行
    :return:
    """
    front_data = ""  # 前半部分存储
    after_data = ""  # 后半部分存储
    with open(file, "r+", encoding="utf-8") as fp:
        # 遍历每行数据进行判断行数,利用 enumerate 辅助计数
        for i, d in enumerate(fp.readlines(), start=1):
            if i >= row:
                after_data += d
            else:
                front_data += d

        fp.seek(0)  # 回到初始点
        fp.write(front_data)
        fp.write(data + "\n")
        fp.write(after_data)



if __name__ == '__main__':
    main()