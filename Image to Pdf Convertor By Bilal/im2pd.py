from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import tkinter.messagebox as tmsg
# Python3 program to convert image to pfd
# using img2pdf library

# importing necessary libraries
import img2pdf
from PIL import ImageTk, Image 
import os
import docx 
def conv():
        q = tmsg.askokcancel("Status","Your Image Has Been Converted\n Click Ok to Save")

        if not q:
            pass
        else:
            imgname = os.path.basename(img_path)
            pdf_name = asksaveasfilename(initialfile=f"{imgname}-coverted.pdf",defaultextension = ".pdf")
            pdf_bytes = img2pdf.convert(image.filename)
            with open(pdf_name,"wb") as file:
                file.write(pdf_bytes)

            if(not os.path.exists(pdf_name)):
                with open(pdf_name,'wb') as file:
                    file.write(pdf_bytes)

def convert():
    global img_path
    global image
    img_path = askopenfilename(defaultextension=".jpg",filetypes=[('JPEG',"*.jpg*"),
                                                              ("PNG",".png"),("DOCX",".docx")])
    if not img_path:
        tmsg.showerror("Error","Please Select an Image to convert")
        Frame(root,bg="white",width=500,height=430).pack()
    else:
        tmsg.showinfo('Status',"Image Successfully Loaded")
    # imgdir = os.path.basename
    # img = PhotoImage(file=img_path)
    # limg = Label(root,image=img)
    # limg.pack()
    
    b2 = Button(root,text="Convert Image",font="Roboto 30 bold",borderwidth=5,command=conv)
    b2.pack(padx=20,pady=5)
    # pdf_path = "C:/Users/TALAL/Documents/Virtual Assistant"


    image = Image.open(img_path)
    # if not image:
    #     doc = docx.Document(img_path)
    #     imgname = os.path.basename(img_path)
    #     pdf_name = asksaveasfilename(initialfile=f"{imgname}-coverted.pdf",defaultextension = ".pdf")
    #     pdf_bytes = img2pdf.convert(doc.filename)
    #     with open(pdf_name,"wb") as file:
    #         file.write(pdf_bytes)

    #     if(not os.path.exists(pdf_name)):
    #         with open(pdf_name,'wb') as file:
    #             file.write(pdf_bytes)










    # image.close()

    # file.close()


    print("Successfully made pdf file")
root = Tk()
root.geometry("500x430")
root.title("Image To PDF Convertor")
root.wm_iconbitmap('1.ico')
# root.resizable(False,False)
Label(root,text="Image to PDF Convertor",font="Roboto 30 bold",bg='red',fg='white').pack(side=TOP,fill=X)
b1 = Button(root,text="Choose Image",font="Roboto 30 bold",borderwidth=5,command=convert)
b1.pack(padx=20,pady=80)

root.mainloop()
