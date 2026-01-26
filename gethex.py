def findhex(filepath):
    """
    Return the hex of first 512 bytes of a file as a string.
    """
    NUMBER_OF_BYTES_TO_READ = 512

    with open(filepath, 'rb') as file:
        file_binary = file.read(NUMBER_OF_BYTES_TO_READ)

    file_hex = file_binary.hex()

    return file_hex