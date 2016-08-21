from wand.image import Image
from wand.display import display

bg_url = "assets/esakabacknew.jpg"

leftChar = input("Left: ")
midChar = input("Mid: ")
rightChar = input("Right: ")
adjustMid = int(input("adjust Mid: "))

left_char = "iori"
mid_char = "ramon"
right_char = "shunei"

left_url = "assets/charaimg_" + leftChar + ".png"
mid_url = "assets/charaimg_" + midChar + ".png"
right_url = "assets/charaimg_" + rightChar + ".png"

#left_url = "assets/ltg.png"
#mid_url = "assets/ltg.png"
#right_url = "assets/ltg.png"
with Image(filename=bg_url) as img:
    with Image(filename=mid_url) as mid:
        with Image(filename=left_url) as left:
            with Image(filename=right_url) as right:
                print(img.size)
                print(left.size)
                img.composite(left, left=-100, top=250)
                img.composite(right, left=946, top=250)
                img.composite(mid, left=420+adjustMid, top=250)
                img.crop(0, 200, width= 1600, height=670)
                display(img)

    #for r in 1, 2, 3:
     #   with img.clone() as i:
      #      i.resize(int(i.width * r * 0.25), int(i.height * r * 0.25))
       #     i.rotate(90 * r)
        #    i.save(filename='mona-lisa-{0}.png'.format(r))
         #   display(i)
