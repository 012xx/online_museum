from PIL import Image,ImageDraw,ImageFont
import uuid,unicodedata

def flyer(num,image,title,user):
    if num == 1:
        return flyer1(image,title,user)
    elif num == 2:
        return flyer2(image,title,user)
    elif num == 3:
        return flyer3(image,title,user)
    elif num == 4:
        return flyer4(image,title,user)

def len_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

def ZEN_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 1
    return count

def flyer1(image,title,user):
    #ユーザ名10文字、タイトル10文字
    image = Image.open(image)#ユーザの画像
    #origin = Image.open('origin.png')#static画像
    origin = Image.new('RGBA',(500,705),'white') #で同じことが可能

    image_copy = image.copy()

    WIDTH = 500
    HEIGHT = 428

    width,height = image_copy.size#リサイズ＆切り取り
    if(HEIGHT/height > WIDTH/width):#縦を基準に
        mag = HEIGHT / height
        image_copy = image_copy.resize((int(mag * width),int(mag * height)),Image.LANCZOS)
        dif = int((mag * width - WIDTH) / 2)#はみ出し測定
        image_copy = image_copy.crop((dif,0,WIDTH + dif,HEIGHT))
    else:
        mag = WIDTH / width
        image_copy = image_copy.resize((int(mag * width),int(mag * height)),Image.LANCZOS)
        dif = int((mag * height - HEIGHT) / 2)#はみ出し測定
        image_copy = image_copy.crop((0,dif,WIDTH,HEIGHT + dif))

    origin.paste(image_copy,(0,0))#貼り付け

    draw = ImageDraw.Draw(origin)
    #もしタイトルが奇数だったら9埋めにしてずらす
    #偶数の場合今まで通り10埋め
    font = ImageFont.truetype("msgothic.ttc",50)
    if len_count(title) % 2 == 0:
        draw.text((0,500),title.center(20 - ZEN_count(title),' '),fill='black',font = font)
    else:
        draw.text((12,500),title.center(19 - ZEN_count(title),' '),fill='black',font = font)
    font = ImageFont.truetype("msgothic.ttc",30)
    draw.text((0,650),user.rjust(32,' '),fill='black',font = font)

    name = "medias/flyers/{}.png".format(str(uuid.uuid4()))
    origin.save(name,quality = 95)#保存先のパス

    return name[7:]

    #staticから705 * 500の画像を複製
    #開いた画像の短辺を基準にリサイズ(おそらくはみ出す)
    #はみ出した分、作品が真ん中に来るように切り取り
    #static画像に張り付け
    #タイトル、ユーザーを描写

def flyer2(image,title,user):
    #ユーザ名10文字、タイトル10文字
    image = Image.open(image)#ユーザの画像
    #origin = Image.open('origin.png')#static画像
    origin = Image.new('RGBA',(500,705),(188,118,150)) #で同じことが可能

    image_copy = image.copy()

    WIDTH = 325
    HEIGHT = 440

    width,height = image_copy.size#リサイズ＆切り取り
    if(HEIGHT/height > WIDTH/width):#縦を基準に
        mag = HEIGHT / height
        image_copy = image_copy.resize((int(mag * width),int(mag * height)),Image.LANCZOS)
        dif = int((mag * width - WIDTH) / 2)#はみ出し測定
        image_copy = image_copy.crop((dif,0,WIDTH + dif,HEIGHT))
    else:
        mag = WIDTH / width
        image_copy = image_copy.resize((int(mag * width),int(mag * height)),Image.LANCZOS)
        dif = int((mag * height - HEIGHT) / 2)#はみ出し測定
        image_copy = image_copy.crop((0,dif,WIDTH,HEIGHT + dif))

    origin.paste(image_copy,(87,30))#貼り付け

    draw = ImageDraw.Draw(origin)
    #もしタイトルが奇数だったら9埋めにしてずらす
    #偶数の場合今まで通り10埋め
    font = ImageFont.truetype("msgothic.ttc",50)
    if len_count(title) % 2 == 0:
        draw.text((0,500),title.center(20 - ZEN_count(title),' '),fill='black',font = font)
    else:
        draw.text((12,500),title.center(19 - ZEN_count(title),' '),fill='black',font = font)
    font = ImageFont.truetype("msgothic.ttc",30)
    draw.text((0,650),user.rjust(32,' '),fill='black',font = font)

    name = "medias/flyers/{}.png".format(str(uuid.uuid4()))
    origin.save(name,quality = 95)#保存先のパス

    return name[7:]

    #staticから705 * 500の画像を複製
    #開いた画像の短辺を基準にリサイズ(おそらくはみ出す)
    #はみ出した分、作品が真ん中に来るように切り取り
    #static画像に張り付け
    #タイトル、ユーザーを描写

def flyer3(image,title,user):
    #ユーザ名10文字、タイトル10文字
    image = Image.open(image)#ユーザの画像
    #origin = Image.open('origin.png')#static画像
    origin = Image.new('RGBA',(500,705),(255,204,0)) #で同じことが可能

    image_copy = image.copy()

    WIDTH = 500
    HEIGHT = 385

    width,height = image_copy.size#リサイズ＆切り取り
    if(HEIGHT/height > WIDTH/width):#縦を基準に
        mag = HEIGHT / height
        image_copy = image_copy.resize((int(mag * width),int(mag * height)),Image.LANCZOS)
        dif = int((mag * width - WIDTH) / 2)#はみ出し測定
        image_copy = image_copy.crop((dif,0,WIDTH + dif,HEIGHT))
    else:
        mag = WIDTH / width
        image_copy = image_copy.resize((int(mag * width),int(mag * height)),Image.LANCZOS)
        dif = int((mag * height - HEIGHT) / 2)#はみ出し測定
        image_copy = image_copy.crop((0,dif,WIDTH,HEIGHT + dif))

    origin.paste(image_copy,(0,0))#貼り付け

    draw = ImageDraw.Draw(origin)
    #もしタイトルが奇数だったら9埋めにしてずらす
    #偶数の場合今まで通り10埋め
    font = ImageFont.truetype("msgothic.ttc",50)
    if len_count(title) % 2 == 0:
        draw.text((0,500),title.center(20 - ZEN_count(title),' '),fill='black',font = font)
    else:
        draw.text((12,500),title.center(19 - ZEN_count(title),' '),fill='black',font = font)
    font = ImageFont.truetype("msgothic.ttc",30)
    draw.text((0,650),user.rjust(32,' '),fill='black',font = font)

    name = "medias/flyers/{}.png".format(str(uuid.uuid4()))
    origin.save(name,quality = 95)#保存先のパス

    return name[7:]

    #staticから705 * 500の画像を複製
    #開いた画像の短辺を基準にリサイズ(おそらくはみ出す)
    #はみ出した分、作品が真ん中に来るように切り取り
    #static画像に張り付け
    #タイトル、ユーザーを描写

def flyer4(image,title,user):
    #ユーザ名10文字、タイトル10文字
    image = Image.open(image)#ユーザの画像
    #origin = Image.open('origin.png')#static画像
    origin = Image.new('RGBA',(500,705),'white') #で同じことが可能
    circle = Image.new('RGBA',(500,705),(122,29,100))
    draw = ImageDraw.Draw(circle)
    draw.ellipse((11,73,489,551),fill = 255)

    image_copy = image.copy()

    WIDTH = 480
    HEIGHT = 480

    width,height = image_copy.size#リサイズ＆切り取り
    if(HEIGHT/height > WIDTH/width):#縦を基準に
        mag = HEIGHT / height
        image_copy = image_copy.resize((int(mag * width),int(mag * height)),Image.LANCZOS)
        dif = int((mag * width - WIDTH) / 2)#はみ出し測定
        image_copy = image_copy.crop((dif,0,WIDTH + dif,HEIGHT))
    else:
        mag = WIDTH / width
        image_copy = image_copy.resize((int(mag * width),int(mag * height)),Image.LANCZOS)
        dif = int((mag * height - HEIGHT) / 2)#はみ出し測定
        image_copy = image_copy.crop((0,dif,WIDTH,HEIGHT + dif))

    origin.paste(image_copy,(10,72))#貼り付け
    origin = Image.alpha_composite(origin,circle)

    draw = ImageDraw.Draw(origin)
    #もしタイトルが奇数だったら9埋めにしてずらす
    #偶数の場合今まで通り10埋め
    font = ImageFont.truetype("msgothic.ttc",50)
    if len_count(title) % 2 == 0:
        draw.text((0,580),title.center(20 - ZEN_count(title),' '),fill='black',font = font)
    else:
        draw.text((12,580),title.center(19 - ZEN_count(title),' '),fill='black',font = font)
    font = ImageFont.truetype("msgothic.ttc",30)
    draw.text((0,650),user.rjust(32,' '),fill='black',font = font)

    name = "medias/flyers/{}.png".format(str(uuid.uuid4()))
    origin.save(name,quality = 95)#保存先のパス

    return name[7:]

    #staticから705 * 500の画像を複製
    #開いた画像の短辺を基準にリサイズ(おそらくはみ出す)
    #はみ出した分、作品が真ん中に来るように切り取り
    #static画像に張り付け
    #タイトル、ユーザーを描写