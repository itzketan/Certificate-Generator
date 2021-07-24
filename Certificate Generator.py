import pandas as pd
from PIL import Image, ImageDraw, ImageFont

data = pd.read_excel (r'C:\Users\admin\PycharmProjects\pythonProject\Certificate Project\Name.xlsx')
name_list = data["Name"].tolist()
for i in name_list:
    im = Image.open(r'C:\Users\admin\PycharmProjects\pythonProject\Certificate Project\Cert.jpeg')
    d = ImageDraw.Draw(im)
    location = (240, 800)
    text_color = (0, 137, 209)
    font = ImageFont.truetype("arial.ttf", 120)
    d.text(location, i, fill = text_color, font = font)
    im.save("Certificate_" + i + ".pdf")
