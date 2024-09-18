#将该目录下的top6000.txt文件进行md5加密，输出到md5.txt中
import hashlib


def md5_encrypt_each_line(input_file_path, output_file_path):
    # 打开输入文件
    with open(input_file_path, "r", encoding="utf-8") as infile:
        # 打开输出文件
        with open(output_file_path, "w", encoding="utf-8") as outfile:
            # 逐行读取输入文件
            for line in infile:
                # 去除行尾的换行符（如果有的话）
                line = line.rstrip('\n')
                # 创建一个md5 hash对象
                md5_hash = hashlib.md5()
                # 更新hash对象以包含当前行的内容
                md5_hash.update(line.encode('utf-8'))
                # 获取16进制格式的哈希值
                md5_digest = md5_hash.hexdigest()
                # 将哈希值写入到输出文件中，并添加换行符
                outfile.write(md5_digest + '\n')

            # 使用函数


input_file_path = "top6000.txt"
output_file_path = "md5.txt"
md5_encrypt_each_line(input_file_path, output_file_path)