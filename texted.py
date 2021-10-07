#! /usr/bin/env python

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100)) # Show() here
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, "text ed")
app.MainLoop()

