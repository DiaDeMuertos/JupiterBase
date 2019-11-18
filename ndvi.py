from glob import glob
from json import dumps
from os.path import join, basename
from os import system

if __name__ == "__main__":

    # ***********************************************************
    path_in = r"/home/diademuertos/Downloads/sentinel_2/cortes"
    path_out = r"/home/diademuertos/Downloads/sentinel_2/temp"
    pattern_4 = "*04.tif"
    pattern_8 = "*08.tif"
    # ***********************************************************

    images_4 = glob(join(path_in, pattern_4))
    images_8 = glob(join(path_in, pattern_8))

    print('IMAGENES 4')
    for image in images_4:
        image_name = basename(image)
        print(image_name)

    print('IMAGENES 8')
    for image in images_8:
        image_name = basename(image)
        print(image_name)

    if len(images_4) == len(images_8):
        NDVI = '(B-A)/(B+A)'
        calcTemplate = 'gdal_calc.py -A % s -B % s --calc="%s" --outfile %s'
        for i in range(len(images_4)):
            imagen_name = basename(images_4[i])
            fecha = imagen_name.split('_')[2]
            out_name = '%s.tif' % (fecha[:8])

            A = images_4[i]
            B = images_8[i]
            C = join(path_out, out_name)

        calc = calcTemplate % (A, B, NDVI, C)
        system(calc)

    else:
        print('FALTAN IMAGENES')
