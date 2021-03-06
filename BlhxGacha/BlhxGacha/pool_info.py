import random


class Pool:
    def __init__(self, name: str):
        self.name = name

    def rand_one(self, seed: str):
        p = []
        for key in pool[self.name]:
            for _ in range(key):
                p.append(key)
        random.seed(seed + "rare")
        group = random.choice(p)
        random.seed(seed + "char")
        return random.choice(pool[self.name][group])

    def rand_ten(self, seed: str):
        ret = []
        for i in range(10):
            ret.append(self.rand_one(seed + str(i)))
        return ret


pool = {
    "轻型池": {
        70: [
            "圣地亚哥", "蒙彼利埃", "贝尔法斯特", "天狼星", "确捷", "雪风", "明石", "Z46", "阿芙乐尔",
            "凯旋", "恶毒", "江风", "黛朵"
        ],
        120: [
            "莫里", "拉菲", "圣路易斯", "海伦娜", "克利夫兰", "丹佛", "标枪", "无敌", "欧若拉", "谢菲尔德",
            "小贝法", "黑太子", "吹雪", "绫波", "野分", "夕张", "最上", "三隈", "Z23", "Z25",
            "Z35", "长春", "太原", "逸仙", "宁海", "平海", "鲁莽", "倔强", "春月", "宵月", "长波",
            "花月"
        ],
        260: [
            "哈曼", "本森", "贝利", "弗莱彻", "贝奇", "斯坦利", "布什", "斯莫利", "霍比", "科尔克",
            "康克德", "孟菲斯", "布鲁克林", "菲尼克斯", "亚特兰大", "朱诺", "女将", "阿卡司塔", "热心",
            "丘比特", "泽西", "库拉索", "杓鹬", "阿基里斯", "阿贾克斯", "南安普顿", "格拉斯哥", "牙买加",
            "神风", "松风", "长月", "初春", "若叶", "初霜", "有明", "夕暮", "大潮", "浦风", "矶风",
            "谷风", "Z18", "Z19", "清波", "莱比锡", "福尔班", "文月", "朝潮", "哈尔西·鲍威尔",
            "旗风", "那珂"
        ],
        550: [
            "卡辛", "唐斯", "克雷文", "麦考尔", "富特", "斯彭斯", "奥利克", "奥马哈", "罗利", "小猎兔犬",
            "大斗犬", "彗星", "新月", "小天鹅", "狐提", "利安得", "睦月", "如月", "卯月", "长良",
            "柯尼斯堡", "卡尔斯鲁厄", "科隆"
        ]
    },
    "重型池": {
        70: [
            "明尼阿波利斯", "北卡罗来纳", "华盛顿", "胡德", "厌战", "威尔士亲王", "约克公爵", "高雄", "爱宕",
            "欧根亲王", "提尔比茨", "让·巴尔", "马萨诸塞", "长门", "天城", "土佐", "加贺BB"
        ],
        120: [
            "休斯敦", "印第安纳波利斯", "威奇塔", "亚利桑那", "科罗拉多", "马里兰", "伦敦", "多塞特郡", "约克",
            "埃克塞特", "声望", "伊丽莎白女王", "纳尔逊", "罗德尼", "黑暗界", "恐怖", "阿贝克隆比", "雾岛",
            "德意志", "斯佩伯爵海军上将", "希佩尔海军上将", "小比叡", "敦刻尔克", "铃谷", "足柄"
        ],
        510: [
            "北安普敦", "芝加哥", "波特兰", "宾夕法尼亚", "田纳西", "加利福尼亚", "什罗普郡", "苏塞克斯",
            "肯特", "萨福克", "诺福克", "反击", "伊势", "日向"
        ],
        300: ["彭萨科拉", "内华达", "俄克拉荷马", "青叶", "衣笠"]
    },
    "特型池": {
        70: [
            "企业", "埃塞克斯", "半人马", "胜利", "光辉", "翔鹤", "瑞鹤", "大凤", "伊19", "明石",
            "U-81", "齐柏林伯爵", "U-47", "U-101", "香格里拉", "伊13", "伊168"
        ],
        120: [
            "休斯敦", "印第安纳波利斯", "威奇塔", "列克星敦", "萨拉托加", "约克城", "大黄蜂", "鲦鱼", "女灶神",
            "伦敦", "多塞特郡", "独角兽", "追赶者", "皇家方舟", "光荣", "伊26", "伊58", "U-557",
            "小赤城", "小齐柏林", "絮库夫", "U-522", "伊25", "伊56"
        ],
        510: ["北安普敦", "芝加哥", "波特兰", "长岛", "什罗普郡", "肯特", "萨福克", "诺福克"],
        300: ["彭萨科拉", "博格", "兰利", "突击者", "竞技神"]
    },
    "活动池": {
        30: ["信浓"],
        40: [
            "维托里奥·维内托", "天鹰", "阿布鲁齐公爵", "巴尔的摩", "阿拉巴马", "艾伦·萨姆纳", "苏维埃贝拉罗斯",
            "可畏", "扎拉", "波拉", "基洛夫", "塔林", "利托里奥", "彼得·史特拉塞", "海因里希亲王", "U-37",
            "玛莉萝丝", "穗香", "霞DOA", "海咲", "塔什干(μ兵装)", "黛朵(μ兵装)", "大凤(μ兵装)", "凉月",
            "纪伊", "U-96", "俾斯麦", "英王乔治五世", "豪", "英仙座", "赫敏", "黎塞留", "阿尔及利亚",
            "圣女贞德", "无畏", "里诺", "布莱默顿", "苏维埃罗西亚", "塔什干", "恰巴耶夫", "龙凤", "能代",
            "骏河", "加斯科涅(μ兵装)", "赤城(μ兵装)", "绊爱·Anniversary", "绊爱·SuperGamer",
            "绊爱·Elegant", "猫音", "露露缇耶", "久远", "圣黑之心", "翡绿之心", "绀紫之心", "群白之心",
            "企业", "半人马", "胡德", "威尔士亲王", "高雄", "圣地亚哥", "贝尔法斯特"
        ],
        120: [
            "尼科洛索·达雷科", "西北风", "西南风", "伯明翰", "史蒂芬·波特", "摩尔曼斯克", "雷鸣", "佩内洛珀",
            "应瑞", "肇和", "文琴佐·焦贝蒂", "朱利奥·凯撒", "纽伦堡", "威悉", "凪咲", "莫妮卡", "勇敢",
            "Z2", "巴尔的摩(μ兵装)", "大青花鱼(μ兵装)", "普林斯顿", "樫野", "千岁", "千代田", "Z26",
            "Z36", "U-556", "U-73", "U-110", "鹰", "英勇", "爱斯基摩人", "沃克兰", "塔尔图",
            "库珀", "威严", "水星纪念", "霞", "鬼怒", "希佩尔海军上将(μ兵装)", "克利夫兰(μ兵装)", "乌璐露",
            "诺瓦露", "布兰", "休斯敦", "独角兽", "克利夫兰", "海伦娜", "伊丽莎白女王", "黑暗界"
        ],
        510: [
            "北安普敦", "芝加哥", "波特兰", "长岛", "什罗普郡", "肯特", "萨福克", "诺福克", "艾尔温",
            "回声", "马布尔黑德"
        ],
        300: ["彭萨科拉", "博格", "兰利", "突击者", "竞技神", "内华达", "俄克拉荷马"]
    }
}
