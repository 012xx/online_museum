from PIL import Image,ImageDraw,ImageFont,ImageFilter
import uuid,unicodedata,datetime

def flyer(num,image,title,user):
    if num == 1:
        return flyer1(image,title,user)
    elif num == 2:
        return flyer2(image,title,user)
    elif num == 3:
        return flyer3(image,title,user)
    elif num == 4:
        return flyer4(image,title,user)
    elif num == 5:
        return flyer5(image,title,user)

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
    logo = Image.open('static/picture/logo.png')
    #origin = Image.open('origin.png')#static画像
    origin = Image.new('RGBA',(500,718),(225,225,225))
    new = Image.new('RGBA',(500,718),(225,225,225))
    new.paste(logo,(350,610))
    origin = Image.alpha_composite(origin,new)

    image_copy = image.copy()

    WIDTH = 355
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

    origin.paste(image_copy,(145,0))#貼り付け

    draw = ImageDraw.Draw(origin)
    draw.rectangle((30+2,450-2,310+2,690-2),fill=(225,225,225),outline=(255,255,255))
    draw.line(((30,450),(310,450),(310,690)),fill=(225,225,225),width=3)
    draw.line(((30,450),(30,690),(310,690)),fill=(225,225,225),width=3)
    draw.line(((145,0),(145,480),(500,480)),fill=(0,0,255),width=1)
    draw.line(((145,0),(500-2,0),(500-2,480)),fill=(0,0,255),width=1)
    #もしタイトルが奇数だったら9埋めにしてずらす
    #偶数の場合今まで通り10埋め
    font = ImageFont.truetype("msgothic.ttc",50)
    draw.text((50,520),title[:5],fill='black',font = font)
    if len(title) > 5:
        draw.text((50,570),title[5:10],fill='black',font = font)
    font = ImageFont.truetype("msgothic.ttc",24)
    time = datetime.datetime.now()
    draw.text((0,510),(str(time)[:10] + "～" ).rjust(39,' '),fill='black',font = font)
    draw.text((0,560),user.rjust(40,' '),fill='black',font = font)

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
    logo = Image.open('static/picture/logo.png')
    origin = Image.new('RGBA',(500,718),(38,38,38))
    new = Image.new('RGBA',(500,718),(38,38,38))
    new.paste(logo,(350,610))
    origin = Image.alpha_composite(origin,new)
    image_copy = image.copy()

    WIDTH = 455
    HEIGHT = 405

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

    origin.paste(image_copy,(22,161))#貼り付け

    draw = ImageDraw.Draw(origin)
    draw.line(((22-3,161-3),(22-3,566),(477+1,566)),fill=(255,255,255),width=3)
    draw.line(((22-3,161-3),(477,161-3),(477,566+1)),fill=(255,255,255),width=3)
    #もしタイトルが奇数だったら9埋めにしてずらす
    #偶数の場合今まで通り10埋め
    font = ImageFont.truetype("msgothic.ttc",50)
    #draw.text((100,615),user.center(20,' '),fill=(255,255,255),font = font)
    if len_count(title) % 2 == 0:
        draw.text((0,60),title.center(20 - ZEN_count(title),' '),fill=(255,255,255),font = font)
    else:
        draw.text((12,60),title.center(19 - ZEN_count(title),' '),fill=(255,255,255),font = font)
    font = ImageFont.truetype("msgothic.ttc",30)
    time = datetime.datetime.now()
    draw.text((20,600),str(time)[:10] + "～" ,fill='white',font = font)
    draw.text((20,640),user.ljust(20,' '),fill='white',font = font)

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
    logo = Image.open('static/picture/logo.png')
    origin = Image.new('RGBA',(500,718),(202,235,224))
    circle = Image.new('RGBA',(500,718),(202,235,224))
    circle.paste(logo,(350,610))
    draw = ImageDraw.Draw(circle)
    draw.ellipse((30,86,30+440,86+440),fill = 255)


    image_copy = image.copy()

    WIDTH = 440
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

    origin.paste(image_copy,(30,86))#貼り付け
    origin = Image.alpha_composite(origin,circle)

    draw = ImageDraw.Draw(origin)
    #もしタイトルが奇数だったら9埋めにしてずらす
    #偶数の場合今まで通り10埋め
    font = ImageFont.truetype("msgothic.ttc",50)
    if len_count(title) % 2 == 0:
        draw.text((0,540),title.center(20 - ZEN_count(title),' '),fill=(38,38,38),font = font)
    else:
        draw.text((12,540),title.center(19 - ZEN_count(title),' '),fill=(38,38,38),font = font)
    font = ImageFont.truetype("msgothic.ttc",30)
    time = datetime.datetime.now()
    draw.text((10,620),str(time)[:10] + "～" ,fill=(38,38,38),font = font)
    draw.text((10,660),user.ljust(10,' '),fill=(38,38,38),font = font)

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
    logo = Image.open('static/picture/logo.png')
    origin = Image.new('RGBA',(500,705),'black') #で同じことが可能
    circle = Image.new('L',(480,480),0)
    new = Image.new("RGBA",(500,705),0)
    new.paste(logo,(350,610))
    draw = ImageDraw.Draw(circle)
    draw.ellipse((90,60,500-110,560-200),fill = 255)
    circle = circle.filter(ImageFilter.GaussianBlur(50))

    image = image.convert("L")
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

    origin.paste(image_copy,(10,72),circle)
    new.paste(logo,(350,610))#貼り付け
    origin = Image.alpha_composite(origin,new)

    draw = ImageDraw.Draw(origin)
    #もしタイトルが奇数だったら9埋めにしてずらす
    #偶数の場合今まで通り10埋め
    font = ImageFont.truetype("msgothic.ttc",50)
    if len_count(title) % 2 == 0:
        draw.text((0,545),title.center(20 - ZEN_count(title),' '),fill='white',font = font)
    else:
        draw.text((12,545),title.center(19 - ZEN_count(title),' '),fill='white',font = font)
    font = ImageFont.truetype("msgothic.ttc",30)
    draw.text((15,650),user.ljust(32,' '),fill='white',font = font)

    name = "medias/flyers/{}.png".format(str(uuid.uuid4()))
    origin.save(name,quality = 95)#保存先のパス

    return name[7:]

    #staticから705 * 500の画像を複製
    #開いた画像の短辺を基準にリサイズ(おそらくはみ出す)
    #はみ出した分、作品が真ん中に来るように切り取り
    #static画像に張り付け
    #タイトル、ユーザーを描写

def flyer5(image,title,user):
    #ユーザ名10文字、タイトル10文字
    image = Image.open(image)#ユーザの画像
    #origin = Image.open('origin.png')#static画像
    origin = Image.new('RGBA',(500,718),(45,44,44)) #で同じことが可能
    logo = Image.open('static/picture/logo.png')
    new = Image.new('RGBA',(500,718),(45,44,44))
    new.paste(logo,(350,610))
    origin = Image.alpha_composite(origin,new)

    image_copy = image.copy()

    WIDTH = 322
    HEIGHT = 718

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
    draw = ImageDraw.Draw(origin)
    draw.line(((322,0),(322,718)),fill=(0,0,255),width=1)
    #もしタイトルが奇数だったら9埋めにしてずらす
    #偶数の場合今まで通り10埋め
    font = ImageFont.truetype("msgothic.ttc",45)
    
    if len_count(title) % 2 == 0:
        title = title.center(10,' ')
        for i in range(10):
            draw.text((381,i * 50 + 30),title[i],fill=(239,239,239),font = font)
    else:
        title = title.center(9,' ')
        for i in range(9):
            draw.text((381,i * 50 + 30),title[i],fill=(239,239,239),font = font)

    font = ImageFont.truetype("msgothic.ttc",30)
    draw.text((336,560),user.center(10,' '),fill=(239,239,239),font = font)

    name = "medias/flyers/{}.png".format(str(uuid.uuid4()))
    origin.save(name,quality = 95)#保存先のパス

    return name[7:]

    #staticから705 * 500の画像を複製
    #開いた画像の短辺を基準にリサイズ(おそらくはみ出す)
    #はみ出した分、作品が真ん中に来るように切り取り
    #static画像に張り付け
    #タイトル、ユーザーを描写