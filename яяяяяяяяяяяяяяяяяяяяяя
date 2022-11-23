from PIL import Image, ImageDraw, ImageFont
def aaa(t,x,y,n):
    im = Image.new('RGB', (x,y), color=('#7B911B'))
    font = ImageFont.truetype(
        'C:/Windows/Fonts/times.ttf',
                          size=100)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (30,480),
        t,
        font=font,
        fill=('#1C0606')
        )
    im.save('C:/Users/Pavel/Desktop/Imgs/Image'+str(n)+'.jpg')

t=['Анекдот:',
  'Мама собирает обед',
  'сыну в школу',
  'складывает:',
  'хлеб',
  'колбасу',
  'и гвозди',
  'Сын спрашивает:',
  'Мам, а зачем мне это?',
  'Ну как зачем',
  'берешь хлеб',
  'складываешь колбасу',
  'и ешь',
  'А гвозди?',
  'Так вот же они',
  ]

for i in range(15):
    aaa(t[i],1000,1000,i)
