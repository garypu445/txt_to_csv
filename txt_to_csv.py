import os
import pandas as pd
import re
import string
from collections import namedtuple

folder_path = 'D:/gary_lab/file_txt/V3/Ch-01/'

df = pd.DataFrame(columns=['File Name', 'Text Content', 'Chinese Characters'])

def extract_number(file_name):
    match = re.search(r'(\d+)', file_name)
    if match:
        return int(match.group())
    return -1

def str_count(s):
    '''找出字符串中的中英文、空格、数字、标点符号个数'''
    
    count_en = count_dg = count_sp = count_zh = count_pu = 0
    s_len = len(s)
    for c in s:
        if c in string.ascii_letters:
            count_en += 1
        elif c.isdigit():
            count_dg += 1
        elif c.isspace():
            count_sp += 1
        elif c.isalpha():
            count_zh += 1
        else:
            count_pu += 1
    total_chars = count_zh + count_en + count_sp + count_dg + count_pu
    if total_chars == s_len:
        return namedtuple('Count', ['total', 'zh', 'en', 'space', 'digit', 'punc'])(s_len, count_zh, count_en, count_sp, count_dg, count_pu)
    else:
        print('Something is wrong!')
        return None
    return None

files = sorted(os.listdir(folder_path), key=extract_number)

for filename in files:
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()

        count = str_count(text_content)
        df = pd.concat([df, pd.DataFrame({'File Name': [filename], 'Text Content': [text_content], 'Chinese Characters': [count.zh]})], ignore_index=True)


# 將DataFrame匯出成csv檔案
csv_output_path = 'D:/gary_lab/file_txt/output.csv'
df.to_csv(csv_output_path, index=False, encoding="utf-8-sig")

print(f"CSV檔案已匯出至 {csv_output_path}")
