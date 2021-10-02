import kivy
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import re
import urllib
import requests
import os

class WidgetsExample(GridLayout):
    my_text = StringProperty("download music")
    def on_button_click(self):
        self.my_text = "processing..."
        # ---------download source code from url-----------#
        theURL = "http://192.168.1.80:8000/"
        def index_data(website_url):
            error = 0
            while error == 0:
                try:
                    response = urllib.request.urlopen(theURL)
                    error = 1
                except:
                    print("did not find server")


            index = response.read()
            index_string = str(index)
            lines = index_string.split("\\n")
            dest_url = r"C:/Users/ricar/Desktop/temp/index.txt"
            fx = open(dest_url, "w")
            for line in lines:
                fx.write(line + "\n")
            fx.close()

        def DownloadFile(url, each):
            local_filename = "C:/Users/ricar/Desktop/temp/" + each
            r = requests.get(url)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
            return None

        index_data(theURL)

        # --------------reading index.txt and regex'ing names of mp3 files-------------#

        nameOfFile = []  ###names of .mp3 files are stored in this variable then exported to file


        fileR = open("C:/Users/ricar/Desktop/temp/index.txt", "r")
        fileW = open("C:/Users/ricar/Desktop/temp/filesNames.txt", "w")

        arr = []

        pattern = r"(>[A-Z,a-z,0-9-\_\;\\!#\[\]'()&.\s]*.mp3)"
        for line in fileR:

            a = (re.findall(pattern, line))
            if len(a) == 0:
                continue
            arr.append(a)
        for each in arr:
            size = len(str(each))
            temp = (each[0][1:size])
            fileW.write(temp+"\n")
            nameOfFile.append(temp)

        fileR.close()
        fileW.close()

        # ---------downloading all files specified with regex---------#
        file_save = "C:/Users/ricar/Desktop/temp/"

        count = 0
        for each in nameOfFile:
            each = each.replace("\\xc3\\xb1", "ñ")
            each = each.replace("\\xc3\\xa1", "á")
            each = each.replace("\\xc3\\xb3", "ó")
            each = each.replace("\\xc3\\xa9", "é")
            each = each.replace("\\xc3\\x91", "Ñ")
            each = each.replace("\\xc3\\x81", "Á")
            each = each.replace("\\xc3\\x9a", "Ú")
            each = each.replace("\\xc3\\xad", "í")
            each = each.replace("\\xc3\\xba", "ú")
            each = each.replace("\\'\\'", "\'\'")
            each = each.replace("\\'", "\'")

            fullPath = str(theURL + each)
            if os.path.isfile(str(file_save + each)):
                print("found it (skipping)")
                continue
            print(fullPath)
            count+=1
            DownloadFile(fullPath, each)
        if count == 0:
            self.my_text = ("[+]everthing is up to date[+]")

        elif count > 0:
            #self.my_text = ("=== "+str(count)+" file(s) downloaded ===")
            pass

        print("button cliked")
        #self.my_text = "you clicked me"

class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        size = dp(100)
        for i in range(0,100):
            b = Button(text=str(i+1), size_hint= (None,None), size = (size,size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()

