# The comic page class, this class defines images based on their specific file extension and white space count.
# The purpose of this class is to allow the main function to be able to determine how many spaces need to be filled in
# and where they are. Basically, it executes the background transformations dictated by the Markov chain.


# Comic page class
class ComicPage:

    # image constructor, takes in the file's file extension (address), white spaces to be filled, and an array of the
    # pixel coordinates of the whitespaces which need to be filled.
    def __init__(self, file_ext, white_spaces, pixel_coordinates=[(0, 0), (0, 1), (0, 2), (0, 3)]):
        self.white_spaces = white_spaces
        self.file_ext = file_ext
        self.pixel_coordinates = pixel_coordinates









