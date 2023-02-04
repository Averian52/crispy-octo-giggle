import tkinter as tk
from tkinter import filedialog
import pandas as pd

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.quit = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit.grid(row=6, column=0)

        self.option1 = tk.Button(self, text="Import Data", command=self.handle_option1)
        self.option1.grid(row=0, column=0)

        self.option2 = tk.Button(self, text="Option 2")
        self.option2.grid(row=1, column=0)

        self.option3 = tk.Button(self, text="Option 3")
        self.option3.grid(row=2, column=0)

        self.option4 = tk.Button(self, text="Option 4")
        self.option4.grid(row=3, column=0)

        self.option5 = tk.Button(self, text="Option 5")
        self.option5.grid(row=4, column=0)
        
    def handle_option1(self):
        filepath = filedialog.askopenfilename()
        self.data = pd.read_excel(filepath)
        print(self.data)
        
        
    def update_database(self):
        for column in self.data.columns:
            table_name = column.lower()  # convert column name to lowercase for table name
            self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, value TEXT)')
            for index, value in self.data[column].iteritems():
                self.cursor.execute(f'INSERT OR IGNORE INTO {table_name} (value) VALUES (?)', (value,))
        self.conn.commit()
        
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()



