from PIL import Image,ImageDraw,ImageFont
import uuid

def flyer1(image,title,user):
    #ユーザ名10文字、タイトル10文字
    image = Image.open(image)#ユーザの画像
    #origin = Image.open('origin.png')#static画像
    origin = Image.new('RGBA',(500,705),'white') #で同じことが可能

    image_copy = image.copy()
    origin_copy = origin.copy()

    WIDTH = 500
    HEIGHT = 428

    width,height = image_copy.size#リサイズ＆切り取り
    if(width > height):#横の方がでかい
        mag = HEIGHT / height
        image_copy = image_copy.resize((int(mag * width),int(mag * height)),Image.LANCZOS)
        dif = int((mag * width - WIDTH) / 2)#はみ出し測定
        image_copy = image_copy.crop((dif,0,WIDTH + dif,HEIGHT))
    else:
        mag = WIDTH / height
        image_copy = image_copy.resize((int(mag * width),int(mag * height)),Image.LANCZOS)
        dif = int((mag * width - WIDTH) / 2)#はみ出し測定
        image_copy = image_copy.crop((0,dif,WIDTH,HEIGHT + dif))

    origin_copy.paste(image_copy,(0,0))#貼り付け

    draw = ImageDraw.Draw(origin_copy)
    font = ImageFont.truetype("msgothic.ttc",50)
    draw.text((0,500),title.center(10,'　'),fill='black',font = font)
    font = ImageFont.truetype("msgothic.ttc",30)
    draw.text((20,650),user.rjust(16,'　'),fill='black',font = font)

    name = "medias/flyers/{}.png".format(str(uuid.uuid4()))
    origin_copy.save(name,quality = 95)#保存先のパス

    return name[7:]

    #staticから705 * 500の画像を複製
    #開いた画像の短辺を基準にリサイズ(おそらくはみ出す)
    #はみ出した分、作品が真ん中に来るように切り取り
    #static画像に張り付け
    #タイトル、ユーザーを描写