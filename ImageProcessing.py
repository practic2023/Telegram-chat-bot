from skimage.io import imread, imsave, imshow
from skimage import img_as_float, img_as_ubyte
from numpy import clip

save_file = 'Downloaded_file'
save_file_processing = 'Proccessing_file'

def image_processing(img_name):
    img = img_as_float(imread(save_file + '/' + img_name))
    N = img.size / 3
    R = sum(sum(i) for i in img[:, :, 0]) / N
    G = sum(sum(i) for i in img[:, :, 1]) / N
    B = sum(sum(i) for i in img[:, :, 2]) / N
    Avg = (R + G + B) / 3
    rw = R / Avg
    gw = G / Avg
    bw = B / Avg
    del N, R, G, B, Avg
    img[:, :, 0] /= rw
    img[:, :, 1] /= gw
    img[:, :, 2] /= bw
    img = clip(img, 0, 1)
    img = img_as_ubyte(img)
    file_type = img_name[img_name.rindex('.'):]
    if file_type == '.dng':
        img_name = img_name[:img_name.rindex('.')] + '.jpg'
    imsave(save_file_processing + '/' + img_name, img)
    return save_file_processing + '/' + img_name


