import os
import re
from bs4 import BeautifulSoup

# 定义 Iconfont.js 文件路径和图片保存路径
iconfont_js_path = r"iconfont.js"
svg_src_path = r"ring80.svg"
svg_save_path = r''

# 定义图片大小
icon_size = (80, 80)

# 读取 Iconfont.js 文件内容
with open(iconfont_js_path, 'r', encoding='utf-8') as f:
    iconfont_js = f.read()

soup = BeautifulSoup(iconfont_js, 'html.parser')
svg_element = soup.find_all('path')

# 遍历每一个svg_element 用其中的字段替换svg_path文件中的path字段,并输出svg文件到svg_save_path路径
with open(svg_src_path, 'r', encoding='utf-8') as f:
    svg_content = f.read()

for index, element in enumerate(svg_element):
    svg_content = re.sub(r'<path.*?</path>', str(element), svg_content)
    with open(os.path.join(svg_save_path, f'new_{index}.svg'), 'w', encoding='utf-8') as f:
        f.write(svg_content)


print(len(svg_element))
