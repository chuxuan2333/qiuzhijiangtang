# 实现文件的备份
def file_backup():
    path = "./files/"
    suffix = '.txt'
    filename = input("请输入需要备份的文件名:")
    # fp_list = original_file.split('.')
    new_file = filename + '副本' + suffix
    try:
        with open(path+filename+suffix, 'rb') as o_f, open(path+new_file, 'wb') as n_f:
            while True:
                # 一次读取1024字节，防止因文件过大导致内存溢出
                content = o_f.read(10)
                print(content)
                n_f.write(content)
                if len(content) < 10:
                    break
    except Exception as e:
        print(e)


file_backup()