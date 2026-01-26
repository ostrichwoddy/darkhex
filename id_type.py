def identify_filetype(file_hex):
    """
    Return the extension of the file as a string.
    """
    image_signatures = {
        ".bmp": "42 4d",
        ".fits": "53 49 4d 50 4c 45",
        ".gif": "47 49 46 38",
        ".gks": "47 4b 53 4d",
        ".rgb": "01 da",
        ".itc": "f1 00 40 bb",
        ".jpg": "ff d8 ff e0",
        ".nif": "49 49 4e 31",
        ".pm": "56 49 45 57",
        ".png": "89 50 4e 47",
        ".ps": "25 21",
        ".eps": "25 21",
        ".ras": "59 a6 6a 95",
        #".tga": "xx xx xx",
        ".tif_be": "4d 4d 00 2a",  # Motorola (big endian)
        ".tif_le": "49 49 2a 00",  # Intel (little endian)
        #".xbm": "xx xx",
        ".xcf": "67 69 6d 70 20 78 63 66 20 76",
        ".fig": "23 46 49 47",
        ".xpm": "2f 2a 20 58 50 4d 20 2a 2f"
    }

    file_extension = ""

    for key, value in image_signatures.items():
        signature_without_space = "".join(value.split())


        if file_hex.startswith(signature_without_space):
            file_extension = key

    if file_extension == "":
        file_extension = "Unknown type"

    return file_extension

if __name__ == "__main__":
    identify_filetype("black.jpg")