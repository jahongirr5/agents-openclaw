from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 2200
bg = (248, 250, 252)
card = (255, 255, 255)
text = (15, 23, 42)
muted = (100, 116, 139)
line = (226, 232, 240)
green = (22, 163, 74)
red = (220, 38, 38)
blue = (37, 99, 235)
cyan = (14, 165, 233)
gray = (148, 163, 184)

try:
    font_title = ImageFont.truetype("arial.ttf", 44)
    font_h2 = ImageFont.truetype("arial.ttf", 28)
    font_text = ImageFont.truetype("arial.ttf", 20)
    font_small = ImageFont.truetype("arial.ttf", 16)
    font_bold = ImageFont.truetype("arialbd.ttf", 20)
except:
    font_title = ImageFont.load_default()
    font_h2 = ImageFont.load_default()
    font_text = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_bold = ImageFont.load_default()

img = Image.new("RGB", (W, H), bg)
d = ImageDraw.Draw(img)

def rounded(x1, y1, x2, y2, r=20, fill=card, outline=line):
    d.rounded_rectangle((x1, y1, x2, y2), r, fill=fill, outline=outline, width=2)

def txt(x, y, s, font=font_text, fill=text, anchor=None):
    d.text((x, y), s, font=font, fill=fill, anchor=anchor)

def bar_card(x, y, w, h, title, rows, minv, maxv):
    rounded(x, y, x+w, y+h)
    txt(x+24, y+20, title, font_h2)
    top = y + 70
    left = x + 170
    right = x + w - 80
    zero = left + int((0 - minv) / (maxv - minv) * (right - left))
    d.line((zero, top, zero, y+h-40), fill=gray, width=2)
    txt(zero, top-24, "0%", font_small, muted, anchor="mm")
    row_h = 36
    for i, (name, val) in enumerate(rows):
        yy = top + i * row_h
        txt(x+24, yy, name, font_text)
        px = int(abs(val) / (maxv - minv) * (right - left))
        color = green if val >= 0 else red
        if val >= 0:
            d.rounded_rectangle((zero, yy+4, zero+px, yy+24), 8, fill=color)
            txt(zero+px+10, yy+14, f"{val:.2f}%", font_small, color)
        else:
            d.rounded_rectangle((zero-px, yy+4, zero, yy+24), 8, fill=color)
            txt(zero-px-10, yy+14, f"{val:.2f}%", font_small, color, anchor="rm")

def vbar_card(x, y, w, h, title, rows, color, suffix=""):
    rounded(x, y, x+w, y+h)
    txt(x+24, y+20, title, font_h2)
    chart_x1 = x + 50
    chart_y1 = y + 70
    chart_x2 = x + w - 30
    chart_y2 = y + h - 80
    d.line((chart_x1, chart_y2, chart_x2, chart_y2), fill=gray, width=2)
    maxv = max(v for _, v in rows)
    n = len(rows)
    gap = 10
    bw = max(18, int((chart_x2-chart_x1-gap*(n-1))/n))
    for i, (name, val) in enumerate(rows):
        bx = chart_x1 + i * (bw + gap)
        bh = int((val / maxv) * (chart_y2 - chart_y1 - 20))
        by = chart_y2 - bh
        d.rounded_rectangle((bx, by, bx+bw, chart_y2), 6, fill=color)
        txt(bx+bw/2, by-14, f"{val:.1f}{suffix}", font_small, text, anchor="mm")
        txt(bx+bw/2, chart_y2+10, name, font_small, muted, anchor="ma")

def donut_card(x, y, w, h, title, parts):
    rounded(x, y, x+w, y+h)
    txt(x+24, y+20, title, font_h2)
    cx, cy = x+180, y+180
    bbox = (cx-90, cy-90, cx+90, cy+90)
    total = sum(v for _, v, _ in parts)
    start = -90
    for label, val, color in parts:
        end = start + 360 * val / total
        d.arc(bbox, start, end, fill=color, width=34)
        start = end
    txt(cx, cy-10, str(total), font_h2, text, anchor="mm")
    txt(cx, cy+22, "tickers", font_small, muted, anchor="mm")
    ly = y + 120
    for label, val, color in parts:
        d.rounded_rectangle((x+320, ly, x+338, ly+18), 4, fill=color)
        txt(x+350, ly-1, f"{label}: {val}", font_text)
        ly += 46

# header
txt(40, 30, "KD Index charts", font_title)
txt(40, 84, "Data date: 2026-09-03", font_text, muted)

# data
daily = [("URTS",15.03),("UZMK",-1.34),("UZTL",1.29),("UZINP",-0.40),("UZMT",4.97),("QZSM",5.06),("KVTS",-2.80),("CBSK",0.31),("HMKB",-0.49),("SQBN",2.01),("IPTB",7.55),("IPKY",1.78),("ALKB",-1.04),("TRSB",-1.40)]
ytd = [("URTS",77.6),("UZMK",133.33),("UZTL",148.63),("UZINP",66.11),("UZMT",9.82),("QZSM",90.79),("KVTS",233.33),("CBSK",22.69),("HMKB",125.58),("SQBN",273.84),("IPTB",137.30),("IPKY",74.36),("ALKB",115.91),("TRSB",17.56)]
vol = [("URTS",62773),("HMKB",245372),("SQBN",38358),("UZTL",33705),("UZMK",10805),("IPTB",4873),("KVTS",4287)]
parts = [("BUY",6,green),("HOLD",5,gray),("SELL",3,red)]

bar_card(40, 130, 1520, 640, "Daily price change, %", daily, -4, 16)
vbar_card(40, 800, 740, 520, "YTD performance, %", ytd, blue, "%")
vbar_card(820, 800, 740, 520, "Annual trading volume, mln UZS", vol, cyan, "")
donut_card(40, 1350, 740, 380, "Recommendation mix", parts)

rounded(820, 1350, 1560, 1730)
txt(844, 1370, "Quick summary", font_h2)
summary = [
    ("Top daily gain", "URTS +15.03%", green),
    ("Biggest drop", "KVTS -2.80%", red),
    ("Best YTD", "SQBN 273.84%", blue),
    ("Top liquidity", "HMKB 245,372 mln UZS", cyan),
    ("Notes", "Built from shared KD index images", muted),
]
y = 1430
for k, v, c in summary:
    txt(850, y, k + ":", font_bold)
    txt(1010, y, v, font_text, c)
    y += 56

rounded(40, 1760, 1520, 2140)
txt(64, 1780, "Tickers and calls", font_h2)
cols = ["Ticker", "Daily", "YTD", "Call"]
colx = [70, 260, 420, 580]
for i, c in enumerate(cols):
    txt(colx[i], 1840, c, font_bold)
rows = [
    ("URTS", "15.03%", "77.60%", "HOLD", gray),
    ("UZMK", "-1.34%", "133.33%", "BUY", green),
    ("UZTL", "1.29%", "148.63%", "HOLD", gray),
    ("UZINP", "-0.40%", "66.11%", "HOLD", gray),
    ("UZMT", "4.97%", "9.82%", "BUY", green),
    ("QZSM", "5.06%", "90.79%", "SELL", red),
    ("KVTS", "-2.80%", "233.33%", "SELL", red),
    ("CBSK", "0.31%", "22.69%", "BUY", green),
    ("HMKB", "-0.49%", "125.58%", "BUY", green),
    ("SQBN", "2.01%", "273.84%", "BUY", green),
    ("IPTB", "7.55%", "137.30%", "BUY", green),
    ("IPKY", "1.78%", "74.36%", "HOLD", gray),
    ("ALKB", "-1.04%", "115.91%", "HOLD", gray),
    ("TRSB", "-1.40%", "17.56%", "SELL", red),
]
start_y = 1882
for i, (a, b, c, e, col) in enumerate(rows):
    yy = start_y + i * 18
    if i < len(rows)-1:
        d.line((60, yy+18, 1500, yy+18), fill=line, width=1)
    txt(70, yy, a, font_small)
    txt(260, yy, b, font_small)
    txt(420, yy, c, font_small)
    txt(580, yy, e, font_small, col)

out = r"C:\Users\johann\Documents\ObsidianVault\Resources\KD Index Charts 2026-09-03.png"
img.save(out, "PNG")
print(out)
