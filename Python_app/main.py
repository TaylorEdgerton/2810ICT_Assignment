import wx
import wx.adv
from getData import *

Page="Home"
class MainWindow(wx.Frame):
    page = ""
    """ We simply derive a new class of Frame. """
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
        self.panelOption1.SetSizer(mainSizerOption1)
        self.panelOption1.Hide()



        # --------------------------------OPTION2 PAGE --------------------------------------------


        self.panelOption2 = wx.Panel(self)



        mainSizerOption2 = wx.BoxSizer(wx.VERTICAL)
        datePickSizerOption2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerTitle3 = wx.BoxSizer(wx.HORIZONTAL)
        sizerDescriptionOption2 = wx.BoxSizer(wx.HORIZONTAL)
        descriptionTextOption2= "Select a date period to view details on all accidents that occured during that period"
        textTitle2 = wx.StaticText(self.panelOption2, label=Title)
        textTitle2.SetFont(font)
        textDescriptionOption2 = wx.StaticText(self.panelOption2, label= descriptionTextOption2)
        textDescriptionOption2.SetFont(font)
        sizerTitle2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerTitle2.Add(textTitle2, flag = wx.ALL, border = 40)
        sizerDescriptionOption2.Add(textDescriptionOption2, flag=wx.ALIGN_CENTRE)
        BackButton = wx.Button(self.panelOption2, label="Back")
        BackButton.SetFont(font)
        BackButton.Bind(wx.EVT_BUTTON, self.BackFromOption)


        datePickFromText = wx.StaticText(self.panelOption2, label="Date From")
        datePickToText = wx.StaticText(self.panelOption2, label="Date To")
        datePickFromText.SetFont(font)
        datePickToText.SetFont(font)
        datePickFrom = wx.adv.DatePickerCtrl(self.panelOption2)
        datePickFrom.SetFont(font)
        # datePickFrom.Bind(wx.adv.EVT_DATE_CHANGED)
        datePickTo = wx.adv.DatePickerCtrl(self.panelOption2)
        datePickTo.SetFont(font)
        datePickSizerOption2.Add(datePickFromText, flag= wx.ALL, border=20)
        datePickSizerOption2.Add(datePickFrom, flag= wx.ALL, border=20)
        datePickSizerOption2.Add(datePickToText, flag= wx.ALL, border=20)
        datePickSizerOption2.Add(datePickTo, flag= wx.ALL, border=20)

        mainSizerOption2.Add(sizerTitle2, flag = wx.ALIGN_CENTRE)

        mainSizerOption2.Add(sizerDescriptionOption2,flag=wx.ALIGN_CENTRE)
        # mainSizerOption1.Add(datePickFrom, proportion = 0, flag=wx.ALIGN_CENTRE)
        mainSizerOption2.Add(datePickSizerOption2, proportion = 0, flag=wx.ALIGN_CENTRE)
        self.panelOption2.SetSizer(mainSizerOption2)
        self.panelOption2.Hide()

        # --------------------------------OPTION3 PAGE --------------------------------------------


        self.panelOption3 = wx.Panel(self)

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
        mainSizerOption3.Add(self.option3KeywordInput, flag=wx.ALL, border = 20)
        mainSizerOption3.Add(self.submitOption3Button, flag=wx.ALL, border=20)

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
        y = self.datePickFrom.GetValue()
        # print(x)
        # print(y)
        DateFromFormat = y.Format("%d/%m/%y")
        DateToFormat = x.Format("%d/%m/%y")
        # z = y.getAccidentsByAlcohol(y, x)


        self.GetData.getAccidentsByDate(str(DateFromFormat),str(DateToFormat))

    def submitOption3Keyword(self, event):
        keyword = self.option3KeywordInput.GetLineText
        returnedata = GetData.getAccidentByKeyword(keyword)

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
