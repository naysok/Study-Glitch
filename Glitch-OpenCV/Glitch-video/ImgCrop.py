from PIL import Image

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2, (img_height - crop_height) // 2, (img_width + crop_width) // 2, (img_height + crop_height) // 2))




for i in range(1,1584):

    num = "%05d" % i
    in_path = "src_slicing/image-" + num + ".jpg"
    out_path = "src_cropped/image-" + num + ".jpg"
    img = Image.open(in_path)
    img_new = crop_center(img, 720, 720)
    img_new.save(out_path, quality=100)

    print("cropped", i)

print("Finish!!")