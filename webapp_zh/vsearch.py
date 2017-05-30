
def search4prepositions_zhs(phrase: str) -> set:
    return line.intersection(set(phrase))
phrase= set("廖汉腾","杨正煜","温灵","赵景","李克和","肖贤彬","孟璐","罗曼","方婉祯","梅晓云","黄龄仪","杨珂","罗娟","杨萍","艾民伟")

def search4letters(phrase: str, letters: str) -> set:
    return set(letters).intersection(set(phrase))
letters=set("网页设计与制作","信息可视化设计","摄像基础","矢量图形设计","报纸编辑学","电视摄像艺术","摄像基础","媒介经济学","媒介素养导论","中国古代文学史（三）","古代汉语（上）","基础写作",
"广告文案写作","中外广告赏析","美学与生活","中西文化概论","网络传播学","电视摄像艺术","非线性编辑（上）","广告心理学","深度报道策划与写作","纪录片赏析")
