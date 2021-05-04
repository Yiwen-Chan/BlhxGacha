class Character:
    def __init__(self, name: str):
        self.name = name

    def rare(self) -> str:
        return char_info[self.name]["稀有度"]

    def type_(self) -> str:
        return char_info[self.name]["类型"]


char_info = {
    "尼科洛索·达雷科": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "西北风": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "西南风": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "伯明翰": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "史蒂芬·波特": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "摩尔曼斯克": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "雷鸣": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "佩内洛珀": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "肇和": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "应瑞": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "文琴佐·焦贝蒂": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "朱利奥·凯撒": {
        "稀有度": "SR",
        "类型": "战列"
    },
    "纽伦堡": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "威悉": {
        "稀有度": "SR",
        "类型": "轻航"
    },
    "凪咲": {
        "稀有度": "SR",
        "类型": "战列"
    },
    "莫妮卡": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "勇敢": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "Z2": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "巴尔的摩(μ兵装)": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "大青花鱼(μ兵装)": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "普林斯顿": {
        "稀有度": "SR",
        "类型": "轻航"
    },
    "樫野": {
        "稀有度": "SR",
        "类型": "运输"
    },
    "千岁": {
        "稀有度": "SR",
        "类型": "轻航"
    },
    "千代田": {
        "稀有度": "SR",
        "类型": "轻航"
    },
    "Z26": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "Z36": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "U-556": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "U-73": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "U-110": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "鹰": {
        "稀有度": "SR",
        "类型": "航母"
    },
    "英勇": {
        "稀有度": "SR",
        "类型": "战列"
    },
    "爱斯基摩人": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "沃克兰": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "塔尔图": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "库珀": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "威严": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "水星纪念": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "霞": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "鬼怒": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "希佩尔海军上将(μ兵装)": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "克利夫兰(μ兵装)": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "乌璐露": {
        "稀有度": "SR",
        "类型": "轻航"
    },
    "诺瓦露": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "布兰": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "维托里奥·维内托": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "天鹰": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "阿布鲁齐公爵": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "巴尔的摩": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "艾伦·萨姆纳": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "阿拉巴马": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "苏维埃贝拉罗斯": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "可畏": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "扎拉": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "波拉": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "基洛夫": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "塔林": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "利托里奥": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "彼得·史特拉塞": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "海因里希亲王": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "U-37": {
        "稀有度": "SSR",
        "类型": "潜艇"
    },
    "玛莉萝丝": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "穗香": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "霞DOA": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "海咲": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "塔什干(μ兵装)": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "黛朵(μ兵装)": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "大凤(μ兵装)": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "凉月": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "纪伊": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "U-96": {
        "稀有度": "SSR",
        "类型": "潜艇"
    },
    "俾斯麦": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "英王乔治五世": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "豪": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "英仙座": {
        "稀有度": "SSR",
        "类型": "轻航"
    },
    "圣女贞德": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "黎塞留": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "阿尔及利亚": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "赫敏": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "无畏": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "里诺": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "布莱默顿": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "恰巴耶夫": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "龙凤": {
        "稀有度": "SSR",
        "类型": "轻航"
    },
    "塔什干": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "苏维埃罗西亚": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "能代": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "骏河": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "加斯科涅(μ兵装)": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "赤城(μ兵装)": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "绊爱·Anniversary": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "绊爱·SuperGamer": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "绊爱·Elegant": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "猫音": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "露露缇耶": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "久远": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "圣黑之心": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "翡绿之心": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "绀紫之心": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
     "群白之心": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "艾尔温": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "回声": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "马布尔黑德": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "天城": {
        "稀有度": "SSR",
        "类型": "战巡"
    },
    "土佐": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "加贺BB": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "长波": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "那珂": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "旗风": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "哈尔西·鲍威尔": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "花月": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "黛朵": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "圣地亚哥": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "蒙彼利埃": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "贝尔法斯特": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "天狼星": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "确捷": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "雪风": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "明石": {
        "稀有度": "SSR",
        "类型": "维修"
    },
    "Z46": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "阿芙乐尔": {
        "稀有度": "SSR",
        "类型": "轻巡"
    },
    "凯旋": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "恶毒": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "江风": {
        "稀有度": "SSR",
        "类型": "驱逐"
    },
    "哈曼": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "本森": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "贝利": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "弗莱彻": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "贝奇": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "斯坦利": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "布什": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "斯莫利": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "霍比": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "科尔克": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "康克德": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "孟菲斯": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "布鲁克林": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "菲尼克斯": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "亚特兰大": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "朱诺": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "女将": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "阿卡司塔": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "热心": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "丘比特": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "泽西": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "库拉索": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "杓鹬": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "阿基里斯": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "阿贾克斯": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "南安普顿": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "格拉斯哥": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "牙买加": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "神风": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "松风": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "长月": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "初春": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "若叶": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "初霜": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "有明": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "夕暮": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "大潮": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "浦风": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "矶风": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "谷风": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "Z18": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "Z19": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "清波": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "莱比锡": {
        "稀有度": "R",
        "类型": "轻巡"
    },
    "福尔班": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "文月": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "朝潮": {
        "稀有度": "R",
        "类型": "驱逐"
    },
    "莫里": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "拉菲": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "圣路易斯": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "海伦娜": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "克利夫兰": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "丹佛": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "标枪": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "无敌": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "欧若拉": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "谢菲尔德": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "小贝法": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "黑太子": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "吹雪": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "绫波": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "野分": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "夕张": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "最上": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "三隈": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "Z23": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "Z25": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "Z35": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "长春": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "太原": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "逸仙": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "宁海": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "平海": {
        "稀有度": "SR",
        "类型": "轻巡"
    },
    "鲁莽": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "倔强": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "春月": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "宵月": {
        "稀有度": "SR",
        "类型": "驱逐"
    },
    "卡辛": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "唐斯": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "克雷文": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "麦考尔": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "富特": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "斯彭斯": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "奥利克": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "奥马哈": {
        "稀有度": "N",
        "类型": "轻巡"
    },
    "罗利": {
        "稀有度": "N",
        "类型": "轻巡"
    },
    "小猎兔犬": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "大斗犬": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "彗星": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "新月": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "小天鹅": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "狐提": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "利安得": {
        "稀有度": "N",
        "类型": "轻巡"
    },
    "睦月": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "如月": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "卯月": {
        "稀有度": "N",
        "类型": "驱逐"
    },
    "长良": {
        "稀有度": "N",
        "类型": "轻巡"
    },
    "柯尼斯堡": {
        "稀有度": "N",
        "类型": "轻巡"
    },
    "卡尔斯鲁厄": {
        "稀有度": "N",
        "类型": "轻巡"
    },
    "科隆": {
        "稀有度": "N",
        "类型": "轻巡"
    },
    "彭萨科拉": {
        "稀有度": "N",
        "类型": "重巡"
    },
    "内华达": {
        "稀有度": "N",
        "类型": "战列"
    },
    "俄克拉荷马": {
        "稀有度": "N",
        "类型": "战列"
    },
    "青叶": {
        "稀有度": "N",
        "类型": "重巡"
    },
    "衣笠": {
        "稀有度": "N",
        "类型": "重巡"
    },
    "休斯敦": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "印第安纳波利斯": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "威奇塔": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "亚利桑那": {
        "稀有度": "SR",
        "类型": "战列"
    },
    "科罗拉多": {
        "稀有度": "SR",
        "类型": "战列"
    },
    "马里兰": {
        "稀有度": "SR",
        "类型": "战列"
    },
    "伦敦": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "多塞特郡": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "约克": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "埃克塞特": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "声望": {
        "稀有度": "SR",
        "类型": "战巡"
    },
    "伊丽莎白女王": {
        "稀有度": "SR",
        "类型": "战列"
    },
    "纳尔逊": {
        "稀有度": "SR",
        "类型": "战列"
    },
    "罗德尼": {
        "稀有度": "SR",
        "类型": "战列"
    },
    "黑暗界": {
        "稀有度": "SR",
        "类型": "重炮"
    },
    "恐怖": {
        "稀有度": "SR",
        "类型": "重炮"
    },
    "阿贝克隆比": {
        "稀有度": "SR",
        "类型": "重炮"
    },
    "雾岛": {
        "稀有度": "SR",
        "类型": "战巡"
    },
    "德意志": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "斯佩伯爵海军上将": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "希佩尔海军上将": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "小比叡": {
        "稀有度": "SR",
        "类型": "战巡"
    },
    "敦刻尔克": {
        "稀有度": "SR",
        "类型": "战巡"
    },
    "铃谷": {
        "稀有度": "SR",
        "类型": "重巡"
    },
    "北安普敦": {
        "稀有度": "R",
        "类型": "重巡"
    },
    "芝加哥": {
        "稀有度": "R",
        "类型": "重巡"
    },
    "波特兰": {
        "稀有度": "R",
        "类型": "重巡"
    },
    "宾夕法尼亚": {
        "稀有度": "R",
        "类型": "战列"
    },
    "田纳西": {
        "稀有度": "R",
        "类型": "战列"
    },
    "加利福尼亚": {
        "稀有度": "R",
        "类型": "战列"
    },
    "什罗普郡": {
        "稀有度": "R",
        "类型": "重巡"
    },
    "苏塞克斯": {
        "稀有度": "R",
        "类型": "重巡"
    },
    "肯特": {
        "稀有度": "R",
        "类型": "重巡"
    },
    "萨福克": {
        "稀有度": "R",
        "类型": "重巡"
    },
    "诺福克": {
        "稀有度": "R",
        "类型": "重巡"
    },
    "反击": {
        "稀有度": "R",
        "类型": "战巡"
    },
    "伊势": {
        "稀有度": "R",
        "类型": "战列"
    },
    "日向": {
        "稀有度": "R",
        "类型": "战列"
    },
    "明尼阿波利斯": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "北卡罗来纳": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "华盛顿": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "企业": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "埃塞克斯": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "半人马": {
        "稀有度": "SSR",
        "类型": "轻航"
    },
    "胜利": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "光辉": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "翔鹤": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "瑞鹤": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "大凤": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "博格": {
        "稀有度": "N",
        "类型": "轻航"
    },
    "兰利": {
        "稀有度": "N",
        "类型": "轻航"
    },
    "突击者": {
        "稀有度": "N",
        "类型": "轻航"
    },
    "竞技神": {
        "稀有度": "N",
        "类型": "轻航"
    },
    "列克星敦": {
        "稀有度": "SR",
        "类型": "航母"
    },
    "萨拉托加": {
        "稀有度": "SR",
        "类型": "航母"
    },
    "约克城": {
        "稀有度": "SR",
        "类型": "航母"
    },
    "大黄蜂": {
        "稀有度": "SR",
        "类型": "航母"
    },
    "鲦鱼": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "女灶神": {
        "稀有度": "SR",
        "类型": "维修"
    },
    "独角兽": {
        "稀有度": "SR",
        "类型": "轻航"
    },
    "追赶者": {
        "稀有度": "SR",
        "类型": "轻航"
    },
    "皇家方舟": {
        "稀有度": "SR",
        "类型": "航母"
    },
    "光荣": {
        "稀有度": "SR",
        "类型": "航母"
    },
    "伊26": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "伊58": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "U-557": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "小赤城": {
        "稀有度": "SR",
        "类型": "航母"
    },
    "小齐柏林": {
        "稀有度": "SR",
        "类型": "航母"
    },
    "絮库夫": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "U-522": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "长岛": {
        "稀有度": "R",
        "类型": "轻航"
    },
    "胡德": {
        "稀有度": "SSR",
        "类型": "战巡"
    },
    "厌战": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "威尔士亲王": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "约克公爵": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "高雄": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "爱宕": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "欧根亲王": {
        "稀有度": "SSR",
        "类型": "重巡"
    },
    "提尔比茨": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "让·巴尔": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "马萨诸塞": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "长门": {
        "稀有度": "SSR",
        "类型": "战列"
    },
    "伊19": {
        "稀有度": "SSR",
        "类型": "潜艇"
    },
    "U-81": {
        "稀有度": "SSR",
        "类型": "潜艇"
    },
    "齐柏林伯爵": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "U-47": {
        "稀有度": "SSR",
        "类型": "潜艇"
    },
    "U-101": {
        "稀有度": "SSR",
        "类型": "潜艇"
    },
    "香格里拉": {
        "稀有度": "SSR",
        "类型": "航母"
    },
    "伊13": {
        "稀有度": "SSR",
        "类型": "潜母"
    },
    "伊168": {
        "稀有度": "SSR",
        "类型": "潜艇"
    },
    "伊25": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "伊56": {
        "稀有度": "SR",
        "类型": "潜艇"
    },
    "信浓": {
        "稀有度": "UR",
        "类型": "航母"
    }
}
