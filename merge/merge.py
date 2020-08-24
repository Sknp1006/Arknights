import glob
import sys
import os
from PIL import Image
from pathlib import Path
from pre_load import ThreadedCopy


def merge(name, img, mas):  # 合成图片
    pixdata_img = img.load()
    pixdata_mas = mas.load()
    print(name)
    try:
        for y in range(mas.size[1]):
            for x in range(mas.size[0]):
                pixdata_img[x, y] = (pixdata_img[x, y][0], pixdata_img[x, y][1], pixdata_img[x, y][2], pixdata_mas[x, y][2])
        img.save("{}\save\{}.png".format(workspace, name))
    except:
        pass



if __name__ == '__main__':
    try:
        Texture2D_path = sys.argv[1]
    except IndexError:
        # Texture2D_path = input("请输入Texture2D文件夹路径: ")
        Texture2D_path = r"C:\Users\SKNP\Documents\GitHub\Arknights\Texture2D"
    # src_path = Texture2D_path
    # if not os.path.exists(src_path):
    #     raise ValueError
    # ThreadedCopy(src_path)

    workspace = "\\".join([Texture2D_path, "workspace"])
    if not os.path.exists(workspace + "\\save"):
        os.mkdir(workspace + "\\save")

    alpha_png = glob.glob('\\'.join([workspace, 'char_*alpha*.png']))  # alpha文件
    all_png = glob.glob('\\'.join([workspace, 'char_*_*.png']))  # 所有图片
    origin_png = [file for file in all_png if file not in alpha_png]  # 除alpha以外的图片

    origin_png_name_list = [png.split("\\")[-1].split(".")[0] for png in origin_png]
    for name in origin_png_name_list:
        image = workspace + "\\" + name + '.png'
        mask = workspace + "\\" + name + '[alpha].png'
        if mask in alpha_png:
            alpha_png.remove(mask)  # 从alpha里移除mask，剩下的是无法匹配的
            img = Image.open(image)
            mas = Image.open(mask)
            merge(name, img, mas)
        else:
            print(mask)
