import wx



Page="Home"
class MainWindow(wx.Frame):
    page = ""
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):

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

        sizerTitle.Add(textTitle, flag=wx.ALIGN_CENTRE)
        sizerTitle.Add(0,10,0)
        sizerDescription.Add(textDescription, flag=wx.CENTER)
        Button1 = wx.Button(self.panelHome, label="Enter")
        Button1.Bind(wx.EVT_BUTTON, self.HomeToMenu)

        mainSizerHome.Add(flag = wx.EXPAND)
        mainSizerHome.Add(sizerTitle, flag=wx.ALIGN_CENTRE)
        mainSizerHome.Add(sizerDescription, flag=wx.ALIGN_CENTRE)
        mainSizerHome.Add(Button1, proportion = 0, flag=wx.ALIGN_CENTRE)

        self.panelHome.SetSizer(mainSizerHome)
        self.Centre()
        self.Show()


# --------------------------------Menu PAGE --------------------------------------------


        self.panelMenu = wx.Panel(self)

        mainSizerMenu = wx.BoxSizer(wx.VERTICAL)

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
        sizerTitle2 = wx.BoxSizer(wx.HORIZONTAL)
        textTitle2 = wx.StaticText(self.panelMenu, label=Title)
        sizerTitle2.Add(textTitle2, flag=wx.ALIGN_CENTRE)
        mainSizerMenu.Add(sizerTitle2, flag=wx.ALIGN_CENTRE)
        mainSizerMenu.Add(Option1, flag=wx.ALIGN_CENTRE)
        mainSizerMenu.Add(Option2, flag=wx.ALIGN_CENTRE)
        mainSizerMenu.Add(Option3, flag=wx.ALIGN_CENTRE)
        mainSizerMenu.Add(Option4, flag=wx.ALIGN_CENTRE)

        self.panelMenu.SetSizer(mainSizerMenu)
        self.panelMenu.Hide()



# --------------------------------OPTION1 PAGE --------------------------------------------


        self.panelOption1 = wx.Panel(self)

        mainSizerOption1 = wx.BoxSizer(wx.VERTICAL)
        sizerTitle3 = wx.BoxSizer(wx.HORIZONTAL)
        sizerDescriptionOption1 = wx.BoxSizer(wx.HORIZONTAL)
        descriptionTextOption1= "Select a date period to view details on all accidents that occured during that period"
        textTitle2 = wx.StaticText(self.panelOption1, label=Title)
        textDescriptionOption1 = wx.StaticText(self.panelOption1, label= descriptionTextOption1)

        sizerTitle2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerTitle2.Add(textTitle2, flag=wx.ALIGN_CENTRE)  
        sizerDescriptionOption1.Add(textDescriptionOption1, flag=wx.ALIGN_CENTRE)
        BackButton = wx.Button(self.panelOption1, label="Back")
        BackButton.Bind(wx.EVT_BUTTON, self.BackFromOption)

        mainSizerOption1.Add(sizerTitle2, flag=wx.ALIGN_CENTRE)
        mainSizerOption1.Add(sizerDescriptionOption1,flag=wx.ALIGN_CENTRE)

        self.panelOption1.SetSizer(mainSizerOption1)
        self.panelOption1.Hide()



        # --------------------------------OPTION2 PAGE --------------------------------------------



        self.panelOption2 = wx.Panel(self)

        mainSizerOption2 = wx.BoxSizer(wx.VERTICAL)
        sizerTitle2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerDescription2 = wx.BoxSizer(wx.HORIZONTAL)
        # descriptionText2= "Page2"
        textTitle2 = wx.StaticText(self.panelOption2, label=Title)

        sizerTitle2.Add(textTitle2, flag=wx.ALIGN_CENTRE)

        BackButton = wx.Button(self.panelOption2, label="Back")
        BackButton.Bind(wx.EVT_BUTTON, self.BackFromOption)
        mainSizerOption2.Add(sizerTitle2, flag=wx.ALIGN_CENTRE)
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

        mainSizerOption3.Add(sizerTitle2, flag=wx.ALIGN_CENTRE)

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
