'''
Chinese to Pinyin
'''

from pypinyin import pinyin, lazy_pinyin, Style

def chinese_to_pinyins(chinese, strict=False):
    chinese = chinese.strip()
    phrases = chinese.split()
    words = []
    for phrase in phrases:
        words.extend(pinyin(phrase, style=Style.TONE2, strict=strict))
        words.append([''])
    words = [word[0] for word in words]
    pinyins = ' '.join(words)
    return pinyins


if __name__ == '__main__':
    chinese = "沉舟 侧畔 千帆过"
    print(chinese_to_pinyins(chinese))

