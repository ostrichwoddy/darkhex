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

    compression_signatures = {
        ".bz": "42 5A",              # BZ
        ".Z": "1F 9D",               # compress
        ".gz": "1F 8B",              # gzip
        ".zip": "50 4B 03 04",       # PK..
        ".bz2": "42 5A 68",          # bzip2
        ".xz": "FD 37 7A 58 5A 00",  # xz (LZMA2)
        ".lz": "4C 5A 49 50"
    }

    archive_signatures = {
    ".7z":  "37 7A BC AF 27 1C",         # 7-Zip
    ".rar": "52 61 72 21 1A 07",         # RAR (v1.5–4.x)
    ".ar":  "21 3C 61 72 63 68 3E 0A",   # Unix ar
    ".cab": "4D 53 43 46",               # Microsoft Cabinet
    ".iso": "43 44 30 30 31"             # ISO 9660 (offset 32769)
}

    executable_signatures = {
    "windows_executable": "4D 5A",  # MZ - PE format (exe, dll, sys)
    "linux_executable":  "7F 45 4C 46",  # ELF binary (binaries and shared objects)
    "macos_executable_32be": "FE ED FA CE",  # Mach-O 32-bit big endian
    "macos_executable_32le": "CE FA ED FE",  # Mach-O 32-bit little endian
    "macos_executable_64be": "FE ED FA CF",  # Mach-O 64-bit big endian
    "macos_executable_64le": "CF FA ED FE",  # Mach-O 64-bit little endian
    "java_bytecode": "CA FE BA BE"   # Java class file
}


    file_extension = ""

    for key, value in image_signatures.items():
        signature_without_space = "".join(value.split())


        if file_hex.startswith(signature_without_space):
            file_extension = key

    for key, value in compression_signatures.items():
        signature_without_space = "".join(value.split())


        if file_hex.startswith(signature_without_space):
            file_extension = key

    for key, value in archive_signatures.items():
        signature_without_space = "".join(value.split())


        if file_hex.startswith(signature_without_space):
            file_extension = key

    for key, value in executable_signatures.items():
        signature_without_space = "".join(value.split())


        if file_hex.startswith(signature_without_space):
            file_extension = key

    if file_extension == "":
        file_extension = "Unknown type"

    return file_extension

if __name__ == "__main__":
    identify_filetype("black.jpg")