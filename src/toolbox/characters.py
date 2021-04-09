ESCAPE_CHARS = {
    u"colon": u":",  # 冒号
    u"question": u"?",  # 问号
    u"star": u"*",  # 星号
    u"slash": u"/",  # 斜线
    u"backslash": u"\\",  # 反斜线
    u"greater": u">",  # 大于号
    u"less": u"<",  # 小于号
    u"vertical": u"|",  # 竖线
    u"quote": u"\"",  # 双引号
    u"aa": u"A",
    u"bb": u"B",
    u"cc": u"C",
    u"dd": u"D",
    u"ee": u"E",
    u"ff": u"F",
    u"gg": u"G",
    u"hh": u"H",
    u"ii": u"I",
    u"jj": u"J",
    u"kk": u"K",
    u"ll": u"L",
    u"mm": u"M",
    u"nn": u"N",
    u"oo": u"O",
    u"pp": u"P",
    u"qq": u"Q",
    u"rr": u"R",
    u"ss": u"S",
    u"uu": u"U",
    u"vv": u"V",
    u"ww": u"W",
    u"xx": u"X",
    u"yy": u"Y",
    u"zz": u"Z",
}

ESCAPE_SWAP_CHARS = dict(zip(ESCAPE_CHARS.values(), ESCAPE_CHARS.keys()))
