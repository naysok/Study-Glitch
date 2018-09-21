import sys
from PIL import Image, ImageDraw

args = sys.argv

print(args[1])
img_count = int(args[1])
file_name = args[2]
inner_w = int(args[3])
inner_h = int(args[4])
margin = int(args[5])
bgc = int(args[6])



outer_w = int(inner_w*(img_count) + (margin*(img_count+1)))
outer_h = int(inner_h + (margin*2))


img = Image.new("RGB",(outer_w, outer_h), (bgc,bgc,bgc))





for i in range(img_count):
    num = "%02d" % (i+1)

    in_path = file_name+"-"+num+".jpg";
    in_img = Image.open(in_path)
    print(in_path)

    # in_img_resize = in_img.resize((400,400), Image.LANCZOS)
    in_img_resize = in_img.resize((inner_w, inner_h), Image.LANCZOS)

    # in_img_resize = in_img.resize((400,400), Image.LANCZOS)
    in_img_resize = in_img.resize((inner_w, inner_h), Image.LANCZOS)

    # img.paste(in_img_resize, (100, 100))
    img.paste(in_img_resize, (inner_w*i + margin*(i+1), margin))


img.show()

out_path = file_name+".jpg";
img.save(out_path, quality=100)