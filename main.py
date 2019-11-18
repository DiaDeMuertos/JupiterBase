from glob import glob
from json import dumps
from os.path import join, basename

if __name__ == "__main__":

    # ***********************************************************
    path_in = r"/home/diademuertos/Downloads/sentinel_2"
    path_out = r"/home/diademuertos/Downloads/sentinel_2/cortes"
    mask = r"/home/diademuertos/Downloads/sentinel_2/temp/seccion.shp"
    pattern = "*.tif"
    # ***********************************************************

    images = glob(join(path_in, pattern))

    file = open(join(path_in, "batch.json"), "w")

    qgis_configs = []
    for index, image in enumerate(images):
        image_name = basename(image)

        tif_input = join(path_in, image_name)
        tif_output = join(path_out, image_name)

        qgis_config = {
            "OUTPUTS": {
                "OUTPUT": tif_output,
            },
            "PARAMETERS": {
                "MASK": "'{0}|layername=seccion'".format(mask),
                "OPTIONS": "''",
                "NODATA": "None",
                "INPUT": "'{0}'".format(tif_input),
                "ALPHA_BAND": "False",
                "KEEP_RESOLUTION": "True",
                "CROP_TO_CUTLINE": "True",
                "DATA_TYPE": "0"
            }
        }

        qgis_configs.append(qgis_config)

    file.writelines(dumps(qgis_configs))
    file.close()

    # Jose M. Guillen/Carlos Lizarraga
    # 7781 E ROONER DR
    # TUCSON, ARIZONA 85730-1176
    # United States
    # Phone: 520 626 4587
