import os, random, csv, random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *

def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels

def is_dog(labels):
    for label in labels:
        if label.description == "Dog":
            return True
    return False

def is_cat(labels):
    for label in labels:
        if label.description == "Cat":
            return True
    return False

def get_dog_pun(data):
    num_dog_puns = 108
    num = random.randint(0,num_dog_puns-1)
    pun = data[num][0]
    nc = 0
    for char in pun:
        if char == ".":
            break
        nc+=1
    pun = pun[nc+2:]
    return pun

def get_cat_pun(data):
    num_cat_puns = 66 # q odd a even up to 65,66
    num = random.randint(0,num_cat_puns-1)
    if num%2 != 0:
        num -= 1
        if num < 0:
            num = 0
    pun = data[num][1]
    nc = 0
    for char in pun:
        if char == ".":
            break
        nc+=1
    pun = pun[nc+2:]
    return [pun, data[num+1][1]]

def display_image(img_path, text):
    font_path = "./fonts/Pacifico.ttf"
    # font_path = None
    pygame.init()
    image = pygame.image.load(img_path)
    screen = pygame.display.set_mode(image.get_rect().size, 0, 32)
    image = image.convert()
    screen.blit(image, (0,0))

    pygame.display.set_caption('Scratching Post')
    ofs = 1
 
    if len(text) != 2:
        font = pygame.font.Font(font_path, 30)
        text1 = font.render(text, 1, (10, 10, 10))
        textw = font.render(text, 1, (250, 250, 250))
        textpos = text1.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textposw = (textpos[0]+ofs, textpos[1]+ofs)
        screen.blit(textw, textposw)
        screen.blit(text1, textpos)
    else:
        font = pygame.font.Font(font_path, 30)
        text1 = font.render(text[0], 1, (10, 10, 10))
        text2 = font.render(text[1], 1, (10, 10, 10))

        text1w = font.render(text[0], 1, (250, 250, 250))
        text2w = font.render(text[1], 1, (250, 250, 250))


        textpos1 = text1.get_rect()
        textpos2 = text2.get_rect()

        textpos1.centerx = screen.get_rect().centerx
        textpos2.midbottom = screen.get_rect().midbottom

        screen.blit(text1, textpos1)
        screen.blit(text2, textpos2)

        textposw1 = (textpos1[0]+ofs, textpos1[1]+ofs)
        textposw2 = (textpos2[0]+ofs, textpos2[1]+ofs)

        screen.blit(text1w, textposw1)
        screen.blit(text2w, textposw2)

    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

def main():
    path = random.choice(os.listdir("./images/images"))
    img_path = "./images/images/" + path
    labels = detect_labels(img_path)
    # labels = detect_labels("cat.jpg") # COMMENT TO FIX RAND
    # for label in labels:
    #     print(label.description)

    pun_path = "minnehack_scraped_data.csv"
    csvDataFile = open(pun_path)
    data=list(csv.reader(csvDataFile))

    if is_cat(labels):
        pun = get_cat_pun(data)
    else:
        pun = get_dog_pun(data)
    display_image(img_path, pun)


if __name__ == '__main__': main()


