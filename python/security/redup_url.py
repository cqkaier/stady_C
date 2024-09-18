lst=[]
with open('C:\\Users\\Kangyl\\Desktop\\新建 文本文档 (2).txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        a=line.split('//')
        # print(a[1])
        lst.append(a[1])
#lst列表去重
def remove_duplicates(lst):
    """
    去除列表中的重复元素，同时保留元素的原始顺序。

    :param lst: 待去重的列表
    :return: 去重后的列表
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# 示例
# original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(lst)
# print(unique_list)  # 输出: [1, 2, 3, 4, 5]
for i in unique_list:
    print('http://'+i)
