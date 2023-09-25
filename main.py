from models.chooser_frame import ChooserFrame
from models.home_frame import HomeFrame







def main():
    home_frame = HomeFrame()
    if home_frame.viewstks_flag:
        chooser_frame = ChooserFrame()
        chooser_frame.draw()
    exit()
    





if __name__ == "__main__":
    main()
