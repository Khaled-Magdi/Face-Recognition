#import Librarys_______________________________________________
import numpy as np
from tkinter import *
from tkinter import filedialog
from matplotlib import pyplot
import matplotlib.pyplot as plt
import cv2
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from deepface import DeepFace
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import pandas as pd



#btn_clicked_______________________________________________

def btn_clicked():
    print("Button Clicked")


#Select Data_______________________________________________

def selectFile1():
    global filePath1
    filePath1 = filedialog.askopenfilename()
    print(filePath1)
    global Name1
    Name1 = ''
    for i in range(0, len(filePath1)):
        Name1 = Name1 + filePath1[i]
        if (filePath1[i] == '/'):
            Name1 = ''
        print(Name1)

    #handling of data




    #lable Get file
    ResultAccuracy = Label(window, height=1, width=24, fg="red",background ='#ffebea',text=Name1)
    ResultAccuracy.place(x = -269.5+450 , y = -180.0+299)



def selectFile2():
    global filePath2
    filePath2 = filedialog.askopenfilename()
    print(filePath2)
    global Name2
    Name2 = ''
    for i in range(0, len(filePath2)):
        Name2 = Name2 + filePath2[i]
        if (filePath2[i] == '/'):
            Name2 = ''
        print(Name2)

    #handling of data




    #lable Get file
    ResultAccuracy = Label(window, height=1, width=24, fg="red",background ='#ffebea',text=Name2)
    ResultAccuracy.place(x = -269.5+450 , y = -180.0+299+38)

    plotFirstGraph()


def selectFile3():
    global filePath3
    filePath3 = filedialog.askopenfilename()
    print(filePath3)
    global Name3
    Name3 = ''
    for i in range(0, len(filePath3)):
        Name3 = Name3 + filePath3[i]
        if (filePath3[i] == '/'):
            Name3 = ''
        print(Name3)

    #handling of data




    #lable Get file
    ResultAccuracy = Label(window, height=1, width=24, fg="red",background ='#ffebea',text=Name3)
    ResultAccuracy.place(x = -269.5+450+424 , y = -180.0+299+38+11)

    plotSeconedGraph()



def selectPath4():
    global filePath4
    filePath4 = filedialog.askdirectory()
    print(filePath4)
    global Name3
    Name3 = ''
    for i in range(0, len(filePath4)):
        Name3 = Name3 + filePath4[i]
        if (filePath4[i] == '/'):
            Name3 = ''
        print(Name3)

    #handling of data




    #lable Get file
    ResultAccuracy = Label(window, height=1, width=24, fg="red",background ='#ffebea',text=Name3)
    ResultAccuracy.place(x = -269.5+450+424 , y = -180.0+299+38+11+38)



def selectFile5():
    global filePath5
    filePath5 = filedialog.askopenfilename()
    print(filePath5)
    global Name5
    Name5 = ''
    for i in range(0, len(filePath5)):
        Name5 = Name5 + filePath5[i]
        if (filePath5[i] == '/'):
            Name5 = ''
        print(Name5)

    #handling of data




    #lable Get file
    ResultAccuracy = Label(window, height=1, width=24, fg="red",background ='#ffebea',text=Name5)
    ResultAccuracy.place(x = -269.5+450+424+427 , y = -180.0+299+38+11+50)

    plotTheardGraph()



#PlotImages_______________________________________________

def plotFirstGraph():

    i1 = cv2.imread(filePath1)
    img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)
    i2 = cv2.imread(filePath2)
    img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)



    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()




    labelDraw = Canvas(window)
    labelDraw.place(
        x = -269.5+330+6 , y = -180.0+299+38+100,
        width=370.0,
        height=206,
    )
    # win = Tk()

    # # setting the title
    # win.title('Plotting in Tkinter')

    # # dimensions of the main window
    # win.geometry("1000x1000")

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 10),
                 dpi=100)

    # list of squares
    # 	y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(121)
    plot1.axis('off')
    plot2 = fig.add_subplot(122)
    plot2.axis('off')


    # plotting the graph
    plot1.imshow(img1)
    plot2.imshow(img2)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=labelDraw)

    # canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   labelDraw)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def plotFirstGraphWithRecangle():
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


    i1 = cv2.imread(filePath1)
    img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)

    faces = faceCascade.detectMultiScale(img1, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)



    i2 = cv2.imread(filePath2)
    img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)

    faces = faceCascade.detectMultiScale(img2, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)






    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()




    labelDraw = Canvas(window)
    labelDraw.place(
        x = -269.5+330+6 , y = -180.0+299+38+100,
        width=370.0,
        height=206,
    )
    # win = Tk()

    # # setting the title
    # win.title('Plotting in Tkinter')

    # # dimensions of the main window
    # win.geometry("1000x1000")

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 10),
                 dpi=100)

    # list of squares
    # 	y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(121)
    plot1.axis('off')

    plot2 = fig.add_subplot(122)
    plot2.axis('off')


    # plotting the graph
    plot1.imshow(img1)
    plot2.imshow(img2)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=labelDraw)

    # canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   labelDraw)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()





def plotSeconedGraph():

    i1 = cv2.imread(filePath3)
    img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)
    # i2 = cv2.imread(filePath2)
    # img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)



    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()




    labelDraw = Canvas(window)
    labelDraw.place(
        x = -269.5+330+6+425 , y = -180.0+299+38+100+50,
        width=370.0,
        height=206,
    )
    # win = Tk()

    # # setting the title
    # win.title('Plotting in Tkinter')

    # # dimensions of the main window
    # win.geometry("1000x1000")

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 10),
                 dpi=100)

    # list of squares
    # 	y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.axis('off')
    # plot2 = fig.add_subplot(122)
    # plot2.axis('off')


    # plotting the graph
    plot1.imshow(img1)
    # plot2.imshow(img2)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=labelDraw)

    # canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   labelDraw)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def plotSeconedGraph_1():

    i1 = cv2.imread(filePath3)
    img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)
    i2 = cv2.imread(df.iloc[0].identity)
    img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)



    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()




    labelDraw = Canvas(window)
    labelDraw.place(
        x=-269.5 + 330 + 6 + 425, y=-180.0 + 299 + 38 + 100 + 50,
        width=370.0,
        height=206,
    )
    # win = Tk()

    # # setting the title
    # win.title('Plotting in Tkinter')

    # # dimensions of the main window
    # win.geometry("1000x1000")

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 10),
                 dpi=100)

    # list of squares
    # 	y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(121)
    plot1.axis('off')
    plot2 = fig.add_subplot(122)
    plot2.axis('off')


    # plotting the graph
    plot1.imshow(img1)
    plot2.imshow(img2)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=labelDraw)

    # canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   labelDraw)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def plotSeconedGraph_2():

    i1 = cv2.imread(filePath3)
    img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)
    i2 = cv2.imread(df.iloc[1].identity)
    img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)



    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()




    labelDraw = Canvas(window)
    labelDraw.place(
        x=-269.5 + 330 + 6 + 425, y=-180.0 + 299 + 38 + 100 + 50,
        width=370.0,
        height=206,
    )
    # win = Tk()

    # # setting the title
    # win.title('Plotting in Tkinter')

    # # dimensions of the main window
    # win.geometry("1000x1000")

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 10),
                 dpi=100)

    # list of squares
    # 	y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(121)
    plot1.axis('off')
    plot2 = fig.add_subplot(122)
    plot2.axis('off')


    # plotting the graph
    plot1.imshow(img1)
    plot2.imshow(img2)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=labelDraw)

    # canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   labelDraw)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def plotSeconedGraph_3():

    i1 = cv2.imread(filePath3)
    img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)
    i2 = cv2.imread(df.iloc[2].identity)
    img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)



    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()




    labelDraw = Canvas(window)
    labelDraw.place(
        x=-269.5 + 330 + 6 + 425, y=-180.0 + 299 + 38 + 100 + 50,
        width=370.0,
        height=206,
    )
    # win = Tk()

    # # setting the title
    # win.title('Plotting in Tkinter')

    # # dimensions of the main window
    # win.geometry("1000x1000")

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 10),
                 dpi=100)

    # list of squares
    # 	y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(121)
    plot1.axis('off')
    plot2 = fig.add_subplot(122)
    plot2.axis('off')


    # plotting the graph
    plot1.imshow(img1)
    plot2.imshow(img2)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=labelDraw)

    # canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   labelDraw)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def plotSeconedGraph_4():

    i1 = cv2.imread(filePath3)
    img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)
    i2 = cv2.imread(df.iloc[3].identity)
    img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)



    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()




    labelDraw = Canvas(window)
    labelDraw.place(
        x=-269.5 + 330 + 6 + 425, y=-180.0 + 299 + 38 + 100 + 50,
        width=370.0,
        height=206,
    )
    # win = Tk()

    # # setting the title
    # win.title('Plotting in Tkinter')

    # # dimensions of the main window
    # win.geometry("1000x1000")

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 10),
                 dpi=100)

    # list of squares
    # 	y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(121)
    plot1.axis('off')
    plot2 = fig.add_subplot(122)
    plot2.axis('off')


    # plotting the graph
    plot1.imshow(img1)
    plot2.imshow(img2)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=labelDraw)

    # canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   labelDraw)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def plotSeconedGraph_5():

    i1 = cv2.imread(filePath3)
    img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)
    i2 = cv2.imread(df.iloc[4].identity)
    img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)



    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()




    labelDraw = Canvas(window)
    labelDraw.place(
        x=-269.5 + 330 + 6 + 425, y=-180.0 + 299 + 38 + 100 + 50,
        width=370.0,
        height=206,
    )
    # win = Tk()

    # # setting the title
    # win.title('Plotting in Tkinter')

    # # dimensions of the main window
    # win.geometry("1000x1000")

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 10),
                 dpi=100)

    # list of squares
    # 	y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(121)
    plot1.axis('off')
    plot2 = fig.add_subplot(122)
    plot2.axis('off')


    # plotting the graph
    plot1.imshow(img1)
    plot2.imshow(img2)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=labelDraw)

    # canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   labelDraw)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()




def plotTheardGraph():

    i1 = cv2.imread(filePath5)
    img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)
    # i2 = cv2.imread(filePath2)
    # img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)



    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()




    labelDraw = Canvas(window)
    labelDraw.place(
        x = -269.5+330+6+425+425 , y = -180.0+299+38+100+58,
        width=370.0,
        height=206,
    )
    # win = Tk()

    # # setting the title
    # win.title('Plotting in Tkinter')

    # # dimensions of the main window
    # win.geometry("1000x1000")

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 10),
                 dpi=100)

    # list of squares
    # 	y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.axis('off')
    # plot2 = fig.add_subplot(122)
    # plot2.axis('off')


    # plotting the graph
    plot1.imshow(img1)
    # plot2.imshow(img2)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=labelDraw)

    # canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   labelDraw)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def plotTheardGraphWithRecangle():
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    i1 = cv2.imread(filePath5)
    img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)
    # i2 = cv2.imread(filePath2)
    # img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)
    faces = faceCascade.detectMultiScale(img1, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)



    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()




    labelDraw = Canvas(window)
    labelDraw.place(
        x = -269.5+330+6+425+425 , y = -180.0+299+38+100+58,
        width=370.0,
        height=206,
    )
    # win = Tk()

    # # setting the title
    # win.title('Plotting in Tkinter')

    # # dimensions of the main window
    # win.geometry("1000x1000")

    # the figure that will contain the plot
    fig = Figure(figsize=(10, 10),
                 dpi=100)

    # list of squares
    # 	y = [i**2 for i in range(101)]

    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.axis('off')
    # plot2 = fig.add_subplot(122)
    # plot2.axis('off')


    # plotting the graph
    plot1.imshow(img1)
    # plot2.imshow(img2)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=labelDraw)

    # canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   labelDraw)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()



#CallAlgorithm_______________________________________________


def CompareImaes():

    plotFirstGraphWithRecangle()
    # faceImage1 = DeepFace.detectFace(filePath1) # for sellect face
    # faceImage2 = DeepFace.detectFace(filePath2)

    # 1_VGG - Face, 2_GoogleFaceNet, 3_OpenFace, 4_Facebook DeepFace, 5_DeepID, 6_ArcFace, 7_Dlib.#in GUI
    models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
    model_name = int(entry0.get())-1
    result = DeepFace.verify(img1_path=filePath1, img2_path=filePath2, model_name=models[model_name])

    print(result)


    verified = result['verified']


    if verified :
        verifiedStr = "  ( They are asme )"
    else :
        verifiedStr = "  ( they are not asme )"

    ResultAccuracy = Label(window, height=1, width=20, fg="red",background ='#ffe4e1',text=str(result['verified']) + verifiedStr)
    ResultAccuracy.place(x = -269.5+480 , y = -180.0+299+348)


    ResultAccuracy = Label(window, height=1, width=20, fg="red",background ='#ffe4e1',text=float(result['distance']) )
    ResultAccuracy.place(x = -269.5+480 , y = -180.0+299+348+25)

    ResultAccuracy = Label(window, height=1, width=5, fg="red",background ='#ffe4e1',text=(result['max_threshold_to_verify']) )
    ResultAccuracy.place(x = -269.5+630 , y = -180.0+299+348+25+20)

    ResultAccuracy = Label(window, height=1, width=10, fg="red",background ='#ffe4e1',text=(result['model']) )
    ResultAccuracy.place(x = -269.5+510 , y = -180.0+299+348+25+25+17)




def FindImaes():

    # faceImage1 = DeepFace.detectFace(filePath1) # for sellect face
    # faceImage2 = DeepFace.detectFace(filePath2)

    # 1_VGG - Face, 2_GoogleFaceNet, 3_OpenFace, 4_Facebook DeepFace, 5_DeepID, 6_ArcFace, 7_Dlib.#in GUI
    models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]

    model_name = int(entry1.get())-1
    global df
    df = DeepFace.find(img_path=filePath3, db_path=filePath4, model_name=models[model_name], enforce_detection=False)
    SI = df.iloc[:].identity
    print(df)

    NameS = ''
    XImage = -269.5+510+300+83
    YImage = -180.0+299+348+25+25+8

    for i in range(0, len(SI)):

        imPath = df.iloc[i].identity
        for i in range(0, len(imPath)):
            NameS = NameS + imPath[i]
            if (imPath[i] == '/'):
                NameS = ''
            print(NameS)

        # lable Get file
        ResultAccuracy = Label(window, height=1, width=26, fg="red", background='#ffe4e1', text=NameS)
        ResultAccuracy.place(x=XImage, y=YImage)

        YImage = YImage +28



def AnalyzeImage():
    plotTheardGraphWithRecangle()

    detector_backend = int(entry2.get()) - 1
    backends = ["opencv", "ssd", "dlib", "retinaface"]

    obj = DeepFace.analyze(img_path=filePath5,detector_backend = backends[detector_backend])
    print(obj)

    print(obj["dominant_emotion"], obj["age"], obj["gender"], obj["dominant_race"])






    ResultAccuracy = Label(window, height=1, width=15, fg="red", background='#ffe4e1', text=obj["age"])
    ResultAccuracy.place(x=-269.5+510+300+83+440, y=-180.0+299+348+25+25+9)

    ResultAccuracy = Label(window, height=1, width=15, fg="red", background='#ffe4e1', text=obj["gender"])
    ResultAccuracy.place(x=-269.5 + 510 + 300 + 83+440, y=-180.0 + 299 + 348 + 25 + 25 + 9+22)

    ResultAccuracy = Label(window, height=1, width=15, fg="red", background='#ffe4e1', text=obj["dominant_race"])
    ResultAccuracy.place(x=-269.5 + 510 + 300 + 83+440, y=-180.0 + 299 + 348 + 25 + 25 + 9+44)

    ResultAccuracy = Label(window, height=1, width=15, fg="red", background='#ffe4e1', text=obj["dominant_emotion"])
    ResultAccuracy.place(x=-269.5 + 510 + 300 + 83+440, y=-180.0 + 299 + 348 + 25 + 25 + 9+66)



def AnalyzeImageInRealTime():
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']
    classifier = load_model('Emotion_Detection.h5')

    cap = cv2.VideoCapture(0)

    while True:
        # Grab a single frame of video
        ret, frame = cap.read()
        labels = []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                # make a prediction on the ROI, then lookup the class

                preds = classifier.predict(roi)[0]
                print("\nprediction = ", preds)
                label = class_labels[preds.argmax()]
                print("\nprediction max = ", preds.argmax())
                print("\nlabel = ", label)
                label_position = (x, y)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, 'No Face Found', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            print("\n\n")
        cv2.imshow('Emotion Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()




    #-----------------------------BY DeepFace______________________


    # DeepFace.stream("Dataset")





    # faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    #
    # cv2.namedWindow('window_frame')
    # emotion_window = []
    #
    # cap = cv2.VideoCapture(1)
    #
    # if not cap.isOpened():
    #     cap = cv2.VideoCapture(0)
    # if not cap.isOpened():
    #     raise IOError(" cannot open web cam ")
    #
    # while True:
    #     ret, frame = cap.read()
    #     result = DeepFace.analyze(frame, actions=['emotion'])
    #
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    #
    #     for (x, y, w, h) in faces:
    #         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #
    #     cv2.putText(frame,
    #                 result['dominant_emotion'],
    #                 (50, 50),
    #                 font, 3,
    #                 (0, 0, 255),
    #                 2,
    #                 cv2.LINE_4);
    #
    #     cv2.imshow('original video', frame)
    #
    #     if cv2.waitKey(2) & 0xFF == ord('q'):
    #         break
    #
    # cap.release()
    # cv2.destroyAllWindows()









#GUI_________________________________________________________________________________________________________________________________

window = Tk()

window.geometry("1350x720")
window.configure(bg = "#ffc19a")
canvas = Canvas(
    window,
    bg = "#ffc19a",
    height = 720,
    width = 1350,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"GUI/background.png")
background = canvas.create_image(
    153.0+505+20, -31.0+384+10,
    image=background_img)


#Entrys_______________________________________________

entry0_img = PhotoImage(file = f"GUI/img_textBox0.png")
entry0_bg = canvas.create_image(
    -269.5+505+20, -180.0+384+10,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e5cdcb",
    highlightthickness = 0)

entry0.place(
    x = -289.0+505+20, y = -194+384+10,
    width = 39.0,
    height = 26)

entry1_img = PhotoImage(file = f"GUI/img_textBox1.png")
entry1_bg = canvas.create_image(
    154.5+505+20, -131.0+384+10,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e5cdcb",
    highlightthickness = 0)

entry1.place(
    x = 135.0+505+20, y = -145+384+10,
    width = 39.0,
    height = 26)

entry2_img = PhotoImage(file = f"GUI/img_textBox2.png")
entry2_bg = canvas.create_image(
    581.5+505+20, -123.0+384+10,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#e5cdcb",
    highlightthickness = 0)

entry2.place(
    x = 562.0+505+20, y = -137+384+10,
    width = 39.0,
    height = 26)





#Button_______________________________________________

img0 = PhotoImage(file = f"GUI/img0.png")
b0 = Button(

    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = AnalyzeImageInRealTime,
    relief = "flat")

b0.place(
    x = 636+505+20, y = -252+384+10,
    width = 125,
    height = 50)

img1 = PhotoImage(file = f"GUI/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = AnalyzeImage,
    relief = "flat")

b1.place(
    x = 666+505+20, y = -137+384+10,
    width = 66,
    height = 33)

img2 = PhotoImage(file = f"GUI/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = selectFile5,
    relief = "flat")

b2.place(
    x = 696+505+20, y = -175+384+10,
    width = 56,
    height = 28)

img3 = PhotoImage(file = f"GUI/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = FindImaes,
    relief = "flat")

b3.place(
    x = 239+505+20, y = -150+384+10,
    width = 66,
    height = 33)

img4 = PhotoImage(file = f"GUI/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = selectPath4,
    relief = "flat")

b4.place(
    x = 269+505+20, y = -187+384+10,
    width = 56,
    height = 28)

img5 = PhotoImage(file = f"GUI/img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = selectFile3,
    relief = "flat")

b5.place(
    x = 269+505+20, y = -225+384+10,
    width = 56,
    height = 28)

img6 = PhotoImage(file = f"GUI/img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = CompareImaes,
    relief = "flat")

b6.place(
    x = -185+505+20, y = -199+384+10,
    width = 66,
    height = 33)

img7 = PhotoImage(file = f"GUI/img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = selectFile2  ,
    relief = "flat")

b7.place(
    x = -155+505+20, y = -236+384+10,
    width = 56,
    height = 28)

img8 = PhotoImage(file = f"GUI/img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = selectFile1,
    relief = "flat")

b8.place(
    x = -155+505+20, y = -274+384+10,
    width = 56,
    height = 28)


img9 = PhotoImage(file = f"GUI/img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = plotSeconedGraph_5,
    relief = "flat")

b9.place(
    x = 309+505+20, y = 240+384+10,
    width = 25,
    height = 25)

img10 = PhotoImage(file = f"GUI/img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = plotSeconedGraph_4,
    relief = "flat")

b10.place(
    x = 309+505+20, y = 184+384+10,
    width = 25,
    height = 25)

img11 = PhotoImage(file = f"GUI/img11.png")
b11 = Button(
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = plotSeconedGraph_3,
    relief = "flat")

b11.place(
    x = 309+505+20, y = 212+384+10,
    width = 25,
    height = 25)

img12 = PhotoImage(file = f"GUI/img12.png")
b12 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = plotSeconedGraph_2,
    relief = "flat")

b12.place(
    x = 309+505+20, y = 156+384+10,
    width = 25,
    height = 25)

img13 = PhotoImage(file = f"GUI/img13.png")
b13 = Button(
    image = img13,
    borderwidth = 0,
    highlightthickness = 0,
    command = plotSeconedGraph_1,
    relief = "flat")

b13.place(
    x = 309+505+20, y = 128+384+10,
    width = 25,
    height = 25)



#mainloop_______________________________________________

window.resizable(False, False)
window.mainloop()
