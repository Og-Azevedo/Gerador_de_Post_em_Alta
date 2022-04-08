from PIL import Image, ImageDraw, ImageFont
from pytrends.request import TrendReq
from dotenv import load_dotenv
import os
import yagmail

load_dotenv()
EMAIL_PASSWORD =os.getenv("EMAIL_PASSWORD")


def send_email(contents):
    try:
        yag = yagmail.SMTP(user='yogopython@gmail.com', password=EMAIL_PASSWORD)
        yag.send(to="yogocosta@gmail.com", subject="Trends",contents=contents, attachments="Trend.png")
        print('Email enviado com sucesso')
    except:
        print('Erro! Aconteceu algo de errado.')


def get_trends():
    pytrend = TrendReq()
    ####---> REQUEST GOOGLE TRENDS
    # realtimeTrends
    try:
        os.remove('bb.jpg')
        os.remove('bb.jpg.REMOVE_ME.REMOVE_ME')
    except:
        pass

    df = pytrend.realtime_trending_searches(pn='US')

    lista_termos = []
    for i, linha in enumerate(df['title'].head(5)):
        primeiro_termo = linha.split(',')[0]
        if len(primeiro_termo) > 13:
            primeiro_termo = primeiro_termo[:13] + '.'
            lista_termos.append(primeiro_termo)
        else:
            lista_termos.append(primeiro_termo)

    return [lista_termos, df]


def make_hash(df):
    ###CRIANDO A STRING DAS HASHTAGS
    lista_hash = ''
    for i, linha in enumerate(df['title'].head(5)):
        primeiro_termo = linha.split(',')[0]

        if lista_hash.count('#') >= 30:
            break

        primeiro_termo = primeiro_termo.replace(' ', ' #')
        lista_hash += ' #' + primeiro_termo

    print(lista_hash)
    return lista_hash


def render_imagem(lista_termos):
    titulo = 'Last hour trends from Google:'
    msg = "1.{}\n2.{}\n3.{}\n4.{}\n5.{}".format(lista_termos[0],lista_termos[1],lista_termos[2],lista_termos[3],lista_termos[4])

    msg_list = msg.splitlines()
    # print(msg_list)

    img = Image.new("RGB",(1080,1080),(23, 43, 68))
    img_w, img_h = (540,540)

    d = ImageDraw.Draw(img)

    fnt = ImageFont.truetype("courbd.ttf",50)
    fnt_titulo = ImageFont.truetype("courbd.ttf",25)

    txt_w, txt_h = d.textsize(msg, font=fnt)
    titulo_w, titulo_h = d.textsize(titulo,font=fnt_titulo)

    align_w = img_w - (txt_w/2)
    align_h = img_h - (txt_h/2)

    d.text((img_w - (titulo_w/2),align_h-50), titulo, font=fnt_titulo, fill=(244, 244, 244))

    distancia_linha = 0
    lista_cores = [(218, 253, 186),(154, 235, 163),(69, 196, 176),(19, 103, 138),(14, 79, 104)]
    for i,linha in enumerate(msg_list):

        d.text((align_w,align_h + distancia_linha), linha, font=fnt, fill=lista_cores[i])
        distancia_linha += 45

    img.save('Trend.png')
    img.show()

    return


lista_termos = get_trends()[0]
df = get_trends()[1]
lista_hash = make_hash(df)
render_imagem(lista_termos)
send_email(contents=lista_hash)







#     # ###---> Postar no Instagram
#     # bot = Bot()
#     #
#     # post = Image.open("Trend.png")
#     # post_jpg = post.convert('RGB')
#     # post_jpg.save('bb.jpg')
#     #
#     # bot.login(username='eyedrop.motion',password='Predatori29!')
#     # bot.upload_photo("bb.jpg", caption=lista_hash)