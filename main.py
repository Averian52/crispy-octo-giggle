from pdf_stuff import PDF
from main_menu import MainMenu

def import_data():
    sub_menu = MainMenu(options={"1. Import from csv": None, 
                                 "2. Import from .xlsx": None, 
                                 "3. Import from db": None, 
                                 "4. Import other": None, 
                                 "5. Exit": None})
    #user_choice = sub_menu.display_menu()
    # Add code to handle the user's choice here

def reconciliations():
    sub_menu = MainMenu(options={"1. Ledger reconciliations": None, 
                                 "2. Finance reconciliations": None, 
                                 "3. Other reconciliations": None, 
                                 "4. Exit": None})
    user_choice = sub_menu.display_menu()
    # Add code to handle the user's choice here

def pdf_functions(pdf):
    sub_menu = MainMenu(options={"1. Split by Pages": None, 
                                 "2. Convert to csv": None, 
                                 "3. Compress": None, 
                                 "4. Exit": None})
    user_choice = sub_menu.display_menu()
    
    if user_choice == 1:
        split_point = list(input("Enter the page numbers where you want to split the pdf: "))
        pdf.split_pdf(split_point)
    elif user_choice == 2:
        pdf.convert_to_csv()
    elif user_choice == 3:
        pdf.compress()

def object_explorer():
    pass

def PDFmain():
    pdf = PDF("C:\\Users\\R.MARTIN\\OneDrive - BYCN\Documents\\Machine Learning\\Python - Other code\\Test.pdf","Test New")
    main_menu = MainMenu(options_dict={"1. Import Data": import_data, 
                                  "2. Reconcilliations": reconciliations, 
                                  "3. PDF Functions": pdf_functions, 
                                  "4. Object explorer": object_explorer,
                                  "5. Exit": None})
    while True:
        user_choice = main_menu.display_menu()




if __name__ == "__main__":
    PDFmain()


