import cv2
import tkinter as tk


def main():

    
    cv2.namedWindow("Camera")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("Camera", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(10)
        if key == 27: # exit on ESC
            break
    cv2.destroyWindow("Camera")

    root.mainloop()

if __name__=="__main__":
    root=tk.Tk()
    main()
