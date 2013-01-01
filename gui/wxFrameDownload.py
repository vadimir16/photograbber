# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Sat Oct 27 14:06:05 2012

import wx

class wxFrameDownload(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxFrameDownload.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_5 = wx.Panel(self, -1)
        self.label_status = wx.StaticText(self.panel_5, -1, "\n\nStatus", style=wx.ALIGN_CENTRE)
        self.button_stop = wx.Button(self.panel_5, -1, "Quit")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxFrameDownload.__set_properties
        self.SetTitle("PhotoGrabber")
        self.SetSize((400, 200))
        self.panel_5.SetMinSize((400, 200))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxFrameDownload.__do_layout
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5_1.Add(self.label_status, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_5_1.Add(self.button_stop, 1, wx.EXPAND, 0)
        self.panel_5.SetSizer(sizer_5_1)
        sizer_5.Add(self.panel_5, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_5)
        sizer_5.SetSizeHints(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    # PhotoGrabber glue

    def Setup(self, state):
        self.state = state
        self.button_stop.Bind(wx.EVT_BUTTON, self.Quit)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def Begin(self):
        # tell the main program to begin downloading
        # provide pointer to Update() function to notify UI of download status
        self.state.beginDownload(self.Update)

    def Update(self, event):
        self.label_status.SetLabel(event.GetValue())
        self.Layout()

    def Quit(self, event):
        self.Close()

    def OnClose(self, event):
        # notify app to hard close
        import os
        os._exit(1)