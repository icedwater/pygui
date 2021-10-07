#! /usr/bin/env python

import wx
import os

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save", "Save a file")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Leave the program")

        helpmenu = wx.Menu()
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About", "Information about the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        menuBar.Append(helpmenu, "&Help")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "Edit, open, and save.", "About text ed", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnOpen(self, event):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, '', "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            with open(os.path.join(self.dirname, self.filename), 'r') as openfile:
                self.control.SetValue(openfile.read())
        dlg.Destroy()

    def OnSave(self, event):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Save to file", self.dirname, '', "*.*", wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.control.SaveFile(filename=os.path.join(self.dirname, self.filename))
        dlg.Destroy()

    def OnExit(self, event):
        self.Close(True)

app = wx.App(False)
frame = MyFrame(None, "text ed")
app.MainLoop()

