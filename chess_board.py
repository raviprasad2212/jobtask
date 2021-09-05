import numpy as np
from PIL import Image
# Open web pages
import webbrowser


def chess_board():
    n = 30 # size of one element, row = 8*n, chessboard = 8*n x 8*n

    segment_black = np.zeros(shape = [n,n])
    segment_white = np.ones(shape = [n,n])*255
    chessboard = np.hstack((segment_black,segment_white))
    for i in range(4):
        chessboard = np.hstack((chessboard,segment_black))
        chessboard = np.hstack((chessboard,segment_white))
    temp = chessboard
    for i in range(7):
        chessboard = np.concatenate((np.fliplr(chessboard),temp))
    img = Image.fromarray(chessboard.astype(np.uint8))
    new_image = img.resize((250, 250))

    # Save given name
    name_of_image = str(input("enter image name to save: "))
    new_image.save('{}.jpg'.format(name_of_image))

    # If you want show image when we run python program, enable it
    # new_image.show()

    # I am saving HTML page, same as image name
    # Save in HTML page
    save_html = open('{}.html'.format(name_of_image), "x")

    try:
        f = open('{}.html'.format(name_of_image),'w')
        image_data = """
        <html>
            <body>
                <img src="{}.jpg" width="250px" height="200px">
            </body>
        </html>
        """.format(name_of_image)
        f.write(image_data)
        f.close()
        webbrowser.open_new_tab('{}.html'.format(name_of_image))

    except FileNotFoundError as err:
        print(str(err))

chess_board()