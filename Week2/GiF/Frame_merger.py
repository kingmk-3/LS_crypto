from PIL import Image,ImageChops
img=Image.open("flag_2.gif")
n=img.n_frames
img.seek(0)
frame=img.copy()
frame.load()
for i in range(n):
    img.seek(i)
    temp=img.copy()
    temp.load()
    temp = temp.convert('1')
    frame = frame.convert('1')
    frame=ImageChops.logical_and(temp,frame)
    #takes logical ands(as 1 is white and 0 is black here) of all frames present in gif
frame.show()