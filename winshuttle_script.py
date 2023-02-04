import win32com.client as win32

def excel():
    return win32.gencache.EnsureDispatch('Excel.Application')   # Get the Excel application object
    
    




xl = excel()
addin = xl.Workbooks.Open('C://Program Files//Winshuttle//Studio//adxloader64.dll')
xl.Visible = True   # Make Excel visible
#xl.RegisterDLL('C://Program Files//Winshuttle//Studio//adxloader64.dll')
winshuttleAddIn = xl.COMAddIns('WinshuttleStudioAddin')    # Get the Winshuttle add-in
#WinshuttleStudioMacros
#obj = winshuttleAddIn.Object    
#obj.RunScript('FBL3N_OPEN_ITEMS_BYUK')    # Run the Winshuttle script   


wb = xl.Workbooks.Open('Test.xlsx')