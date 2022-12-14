import wx
import wx.adv
from getData import *
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
Page="Home"
class MainWindow(wx.Frame):
    page = ""

    def __init__(self, parent, title):

        self.GetData = GetData()
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)
        Title = "Victorian Crash Stats App"
# --------------------------------HOME PAGE --------------------------------------------
        wx.Frame.__init__(self, parent, title=title, size=(1080,800))
        self.panelHome = wx.Panel(self)

        mainSizerHome = wx.BoxSizer(wx.VERTICAL)
        sizerTitle = wx.BoxSizer(wx.HORIZONTAL)
        sizerDescription = wx.BoxSizer(wx.HORIZONTAL)
        descriptionText= "This app will show you data representations of road accident statistics in Victoria"
        textTitle = wx.StaticText(self.panelHome, label=Title)
        textTitle.SetFont(font)
        textDescription = wx.StaticText(self.panelHome, label= descriptionText)
        textDescription.SetFont(font)

        sizerTitle.Add(textTitle, flag=wx.ALL, border=80)
        sizerDescription.Add(textDescription, flag=wx.ALL, border=150)
        Button1 = wx.Button(self.panelHome, label="Enter")
        Button1.Bind(wx.EVT_BUTTON, self.HomeToMenu)

       
        mainSizerHome.Add(sizerTitle, flag=wx.ALIGN_CENTRE)
        mainSizerHome.Add(sizerDescription, flag=wx.ALIGN_CENTRE)
        mainSizerHome.Add(Button1, proportion = 0, flag=wx.ALIGN_CENTRE)

        self.panelHome.SetSizer(mainSizerHome)
        self.Centre()
        self.Show()


# --------------------------------Menu PAGE --------------------------------------------


        self.panelMenu = wx.Panel(self)

        mainSizerMenu = wx.BoxSizer(wx.VERTICAL)
        sizerTitle2 = wx.BoxSizer(wx.HORIZONTAL)

        BackButton = wx.Button(self.panelMenu, label="Back")
        BackButton.Bind(wx.EVT_BUTTON, self.BackFromMenu)
        Option1 = wx.Button(self.panelMenu, label="Menu Option 1")
        Option1.Bind(wx.EVT_BUTTON, self.Option1)
        Option2 = wx.Button(self.panelMenu, label="Menu Option 2")
        Option2.Bind(wx.EVT_BUTTON, self.Option2)
        Option3 = wx.Button(self.panelMenu, label="Menu Option 3")
        Option3.Bind(wx.EVT_BUTTON, self.Option3)
        Option4 = wx.Button(self.panelMenu, label="Menu Option 4")
        Option4.Bind(wx.EVT_BUTTON, self.Option4)
        Option1.SetFont(font)
        Option2.SetFont(font)
        Option3.SetFont(font)
        Option4.SetFont(font)

        textTitle2 = wx.StaticText(self.panelMenu, label=Title)
        sizerTitle2.Add(textTitle2, flag=wx.ALL, border=150)
        textTitle2.SetFont(font)
        mainSizerMenu.Add(sizerTitle2, flag=wx.ALIGN_CENTRE | wx.ALL, border=20)
        mainSizerMenu.Add(Option1, flag=wx.ALIGN_CENTRE | wx.ALL, border=20)
        mainSizerMenu.Add(Option2, flag=wx.ALIGN_CENTRE | wx.ALL, border=20)
        mainSizerMenu.Add(Option3, flag=wx.ALIGN_CENTRE | wx.ALL, border=20)
        mainSizerMenu.Add(Option4, flag=wx.ALIGN_CENTRE | wx.ALL, border=20)

        self.panelMenu.SetSizer(mainSizerMenu)
        self.panelMenu.Hide()



# --------------------------------OPTION1 PAGE --------------------------------------------


        self.panelOption1 = wx.Panel(self)

        self.option1AllAccidents = ()

        self.option1ListControl = wx.ListCtrl(self.panelOption1, size = (400,400), style = wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.option1ListControl.InsertColumn(1, "OBJECTID")
        self.option1ListControl.InsertColumn(2, "ACCIDENT DATE")
        self.option1ListControl.InsertColumn(3, "ACCIDENT TYPE")
        self.option1ListControl.InsertColumn(4, "ROAD GEOMETRY")
        self.option1ListControl.InsertColumn(5, "INJURIES OR FATALITIES")



        mainSizerOption1 = wx.BoxSizer(wx.VERTICAL)
        datePickSizerOption1 = wx.BoxSizer(wx.HORIZONTAL)
        sizerTitle3 = wx.BoxSizer(wx.HORIZONTAL)
        sizerDescriptionOption1 = wx.BoxSizer(wx.HORIZONTAL)
        descriptionTextOption1= "Select a date period to view details on all accidents that occured during that period"
        textTitle2 = wx.StaticText(self.panelOption1, label=Title)
        textTitle2.SetFont(font)
        textDescriptionOption1 = wx.StaticText(self.panelOption1, label= descriptionTextOption1)
        textDescriptionOption1.SetFont(font)   
        sizerTitle2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerTitle2.Add(textTitle2, flag = wx.ALL, border = 40)
        sizerDescriptionOption1.Add(textDescriptionOption1, flag=wx.ALIGN_CENTRE)
        BackButton = wx.Button(self.panelOption1, label="Back")
        BackButton.SetFont(font)
        BackButton.Bind(wx.EVT_BUTTON, self.BackFromOption)


        datePickFromText = wx.StaticText(self.panelOption1, label="Date From")
        datePickToText = wx.StaticText(self.panelOption1, label="Date To")

        # datePickFromText.Bind(wx.adv.EVT_DATE_CHANGED, )



        datePickFromText.SetFont(font)
        datePickToText.SetFont(font)
        self.datePickFrom = wx.adv.DatePickerCtrl(self.panelOption1)


        
        self.datePickFrom.SetFont(font)
        # datePickFrom.Bind(wx.adv.EVT_DATE_CHANGED)
        self.datePickTo = wx.adv.DatePickerCtrl(self.panelOption1)
        self.datePickTo.SetFont(font)

        submitOption1 = wx.Button(self.panelOption1, label="Submit")
        submitOption1.Bind(wx.EVT_BUTTON, self.SubmitOption1Date)

        datePickSizerOption1.Add(datePickFromText, flag= wx.ALL, border=20)
        datePickSizerOption1.Add(self.datePickFrom, flag= wx.ALL, border=20)
        datePickSizerOption1.Add(datePickToText, flag= wx.ALL, border=20)
        datePickSizerOption1.Add(self.datePickTo, flag= wx.ALL, border=20)
        datePickSizerOption1.Add(submitOption1, flag=wx.ALL, border = 20)

        mainSizerOption1.Add(sizerTitle2, flag = wx.ALIGN_CENTRE)

        mainSizerOption1.Add(sizerDescriptionOption1,flag=wx.ALIGN_CENTRE)
        # mainSizerOption1.Add(datePickFrom, proportion = 0, flag=wx.ALIGN_CENTRE)
        mainSizerOption1.Add(datePickSizerOption1, proportion = 0, flag=wx.ALIGN_CENTRE)
        mainSizerOption1.Add(self.option1ListControl, proportion = 0, flag=wx.ALIGN_CENTRE)
        self.panelOption1.SetSizer(mainSizerOption1)
        self.panelOption1.Hide()



        # --------------------------------OPTION2 PAGE --------------------------------------------


        #---------------------------------- MATPLOTLIB ------------------------------------


        self.panelOption2 = wx.Panel(self)
        # Matplotlib data
        alcoholData = self.GetData.accidentAlcoholStat()
        # print(type(alcoholData))

        #Creating matplotlib element in wxpython

        self.figure = Figure()
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.axes = self.figure.add_subplot(1,1,1)
        self.option2Matplotlib = wx.BoxSizer(wx.VERTICAL)
        self.option2Matplotlib.Add(self.canvas, 1, wx.ALL, border=200)
        self.Fit()

        #Creating matplotplib barchart
        data = {'Males':alcoholData[0][0][0], 'Females':alcoholData[1][0][0]}
        gender = list(data.keys())
        values = list(data.values())
        self.axes.bar(gender,values, color ='blue', width = 0.4)
        self.canvas.Show(False)


        mainSizerOption2 = wx.BoxSizer(wx.VERTICAL)
        datePickSizerOption2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerTitle3 = wx.BoxSizer(wx.HORIZONTAL)
        sizerDescriptionOption2 = wx.BoxSizer(wx.HORIZONTAL)
        descriptionTextOption2= "This data represents single vehicle, single occupant accidents that were alcohol related and sorts those accidents by Male and Female Genders"
        textTitle2 = wx.StaticText(self.panelOption2, label=Title)
        textTitle2.SetFont(font)
        textDescriptionOption2 = wx.StaticText(self.panelOption2, label= descriptionTextOption2)
        textDescriptionOption2.SetFont(font)
        sizerTitle2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerTitle2.Add(textTitle2, flag = wx.ALL, border = 40)
        sizerDescriptionOption2.Add(textDescriptionOption2, flag=wx.TOP, border= 500)
        BackButton = wx.Button(self.panelOption2, label="Back")
        BackButton.SetFont(font)
        BackButton.Bind(wx.EVT_BUTTON, self.BackFromOption)

        # datePickFrom.Bind(wx.adv.EVT_DATE_CHANGED)



        mainSizerOption2.Add(sizerTitle2, flag = wx.ALIGN_CENTRE)

        mainSizerOption2.Add(sizerDescriptionOption2,flag=wx.ALIGN_CENTRE)

        self.panelOption2.SetSizer(mainSizerOption2)
        self.panelOption2.Hide()

        # --------------------------------OPTION3 PAGE --------------------------------------------


        self.panelOption3 = wx.Panel(self)

        self.option3ListControl = wx.ListCtrl(self.panelOption3, size=(400, 400), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.option3ListControl.InsertColumn(1, "OBJECTID")
        self.option3ListControl.InsertColumn(2, "ACCIDENT DATE")
        self.option3ListControl.InsertColumn(3, "ACCIDENT TYPE")

        mainSizerOption3 = wx.BoxSizer(wx.VERTICAL)
        sizerTitle2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerDescription2 = wx.BoxSizer(wx.HORIZONTAL)
        # descriptionText2= "Page2"
        textTitle2 = wx.StaticText(self.panelOption3, label=Title)

        sizerTitle2.Add(textTitle2, flag=wx.ALIGN_CENTRE)

        BackButton = wx.Button(self.panelOption3, label="Back")
        BackButton.Bind(wx.EVT_BUTTON, self.BackFromOption)

        self.option3KeywordInput = wx.TextCtrl(self.panelOption3)
        self.submitOption3Button = wx.Button(self.panelOption3, label ='submit')
        self.submitOption3Button.Bind(wx.EVT_BUTTON, self.submitOption3Keyword)

        mainSizerOption3.Add(sizerTitle2, flag=wx.ALIGN_CENTRE)
        mainSizerOption3.Add(self.option3KeywordInput, flag=wx.ALIGN_CENTRE)
        mainSizerOption3.Add(self.submitOption3Button, flag=wx.ALIGN_CENTRE)
        mainSizerOption3.Add(self.option3ListControl, proportion=0, flag=wx.ALIGN_CENTRE)
        self.panelOption3.SetSizer(mainSizerOption3)
        self.panelOption3.Hide()



        # --------------------------------OPTION4 PAGE --------------------------------------------


        self.panelOption4 = wx.Panel(self)

        mainSizerOption4 = wx.BoxSizer(wx.VERTICAL)
        sizerTitle2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerDescription2 = wx.BoxSizer(wx.HORIZONTAL)
        # descriptionText2= "Page2"
        textTitle2 = wx.StaticText(self.panelOption4, label=Title)

        sizerTitle2.Add(textTitle2, flag=wx.ALIGN_CENTRE)

        BackButton = wx.Button(self.panelOption4, label="Back")
        BackButton.Bind(wx.EVT_BUTTON, self.BackFromOption)

        mainSizerOption4.Add(sizerTitle2, flag=wx.ALIGN_CENTRE)
        self.panelOption4.SetSizer(mainSizerOption4)
        self.panelOption4.Hide()


# ------------------------------- Button Event Functions------------------------------------------------

    def SubmitOption1Date(self,event):
        x = self.datePickTo.GetValue()
        print(type(x))
        y = self.datePickFrom.GetValue()
        # print(x)
        # print(y)
        DateFromFormat = y.Format("%d/%m/%y")
        DateToFormat = x.Format("%d/%m/%y")
        # z = y.getAccidentsByAlcohol(y, x)
        print(DateFromFormat)

        option1AllAccidents = self.GetData.getAccidentsByDate(str(DateFromFormat),str(DateToFormat))
        # for i in option1AllAccidents:
        #     index = 0
        #     print(i[0])
        #     self.option1ListControl.InsertItem(0,str(i[0]))
        #     index +=1
        # for i in option1AllAccidents:
        #     index=0
        #     print(i[1])
        #     self.option1ListControl.InsertItem(1,str(i[1]))
        #     index+=1
        # for i in option1AllAccidents:
        #     index=0
        #     print(i[2])
        #     self.option1ListControl.InsertItem(2,str(i[2]))
        #     index+=1
        for item in option1AllAccidents:
            index = self.option1ListControl.InsertItem(self.option1ListControl.GetItemCount(), item[0])
            for col, text in enumerate(item[1:]):
                self.option1ListControl.SetItem(index, col + 1, text)

    def submitOption3Keyword(self, event):
        keyword = str(self.option3KeywordInput.GetLineText(0))
        option3AccidentsByKeyword = self.GetData.getAccidentByKeyword(keyword)
        print(keyword)
        for item in option3AccidentsByKeyword:
            index = self.option3ListControl.InsertItem(self.option3ListControl.GetItemCount(), item[0])
            for col, text in enumerate(item[1:]):
                self.option3ListControl.SetItem(index, col + 1, text)

    def getAccidentsByDate(self, dateFrom, dateTo):
        y = GetData()



    def HomeToMenu(self, event):
        # self.frame.Show()
        self.panelHome.Hide()
        self.panelMenu.Show()
        self.panelMenu.SetSize(1080,800)

    def BackFromMenu(self, event):
        # self.frame.Show()
        self.panelHome.Show()
        self.panelMenu.Hide()
        self.panelHome.SetSize(1080,800)

    def BackFromOption(self, event):
     # self.frame.Show()
     self.panelHome.Hide()
     self.panelOption1.Hide()
     self.panelOption2.Hide()
     self.panelOption3.Hide()
     self.panelOption4.Hide()
     self.panelMenu.Show()
     self.panelHome.SetSize(1080,800)
     self.canvas.Show(False)


    def Option1(self, event):
        # self.frame.Show()
        # y = GetData()
        # x = y.getAccidentsByAlcohol()
        # print(x)
        self.panelOption1.Show()
        self.panelMenu.Hide()
        self.panelOption1.SetSize(1080,800)

    def Option2(self, event):
        # self.frame.Show()
        self.panelOption2.Show()
        self.canvas.Show(True)
        self.panelMenu.Hide()
        self.panelOption2.SetSize(1080,800)

    def Option3(self, event):
        # self.frame.Show()
        self.panelOption3.Show()
        self.panelMenu.Hide()
        self.panelOption3.SetSize(1080,800)

    def Option4(self, event):
        # self.frame.Show()
        self.panelOption4.Show()
        self.panelMenu.Hide()
        self.panelOption4.SetSize(1080,800)


app = wx.App()
frame = MainWindow(None, 'Victoria Crash Stats')

# import wx.lib.inspection
# wx.lib.inspection.InspectionTool().Show()

app.MainLoop()
