import DBwork
import tkinter as tk
from tkinter import ttk



class Window(tk.Frame):
    def __init__(self,master = None):
        tk.Frame.__init__(self,master)
        self.master = master

        self.pack(fill = tk.BOTH,expand = 1)

        #Following block is for the selector menu for criteria to Group our data by, and selector to sort our data
        self.sortSelection = ["Genre","Location","Title", "Studio"]

        self.groupLabel = tk.Label(self,text = "Group data by")
        self.groupLabel.place(x=0,y=30)
        self.groupOption = tk.StringVar()
        self.groupOption.set("Sort Options 1")
        self.groupMenu = tk.OptionMenu(self, self.groupOption,*self.sortSelection)
        self.groupMenu.place(x=90,y = 30)

        self.searchLabel = tk.Label(self,text = "Search data by")
        self.searchLabel.place(x=0,y=60)
        self.searchOption = tk.StringVar()
        self.searchOption.set("Sort Options 2")
        self.searchLabel = tk.OptionMenu(self, self.searchOption,*self.sortSelection)
        self.searchLabel.place(x=90,y = 60)
        self.searchOption.trace('w',self.sortMenuCallBack)

        #Block is for the aggregate options menu for our data
        self.agglabel = tk.Label(self,text = "Aggregate Func")
        self.agglabel.place(x=0,y=90)
        self.aggOption= tk.StringVar()    
        self.aggOption.set("Viewer Aggregation Functions")
        self.aggSelection = ["Sum","avg","Max","Min"]
        self.aggMenu = tk.OptionMenu(self,self.aggOption,*self.aggSelection)
        self.aggMenu.place(x =90 ,y = 90)
        

        #Takes user input for search criteria
        self.entry = tk.Entry(self,width = 100)
        self.entry.place(x=0,y=0)
        self.entry.insert(tk.END,"Enter Title, location, genre, or studio based on 2nd option menu option, seperated by commas, space and case sensitive")
        self.entry.bind("<Button-1>", self.entryListCallBack)
        self.enterButton = tk.Button(self,text = "Enter",command = self.getInput)
        self.enterButton.place(x=0,y = 120)

        #Adding a box to view valid search terms
        self.selections= tk.Listbox()
        self.selections.insert(tk.END,"This field will show ")
        self.selections.insert(tk.END,"valid search terms for")
        self.selections.insert(tk.END,"your selection of")
        self.selections.insert(tk.END,"option 2")
        self.selections.place(x=0,y = 150)

        #To view our results
        self.tvMenu = ttk.Treeview(self)
        self.tvMenu['columns'] = ("Title","Studio","Genre","Location","Viewers")
        self.tvMenu.heading("#0", text="")
        self.tvMenu.column("#0", minwidth=0, width=0, stretch=tk.NO)
        for column in self.tvMenu['columns']:
            self.tvMenu.heading(column,text =column)
            self.tvMenu.column(column,minwidth = 80,width = 80,stretch = tk.NO)
        #We can do this while the database is small, not so good of an idea without a limit if it grows big
        for entry in DBwork.executeQuery("Select * from show"):
            self.tvMenu.insert("",'end', values = entry)
        self.tvMenu.pack(side="bottom")
    

    def getInput(*args):
        window = args[0]
        entries = window.entry.get()
        #If atleast one menu option has not been selected
        if window.groupOption.get() not in  window.sortSelection or window.searchOption.get() not in window.sortSelection or window.aggOption.get() not in window.aggSelection:
            window.entry.delete(0,'end')
            window.entry.insert(tk.END,"Must select an option from all menus")
            return
        #Get list of all entries
        entryList = entries.split(',')
        viewerQuery = "SELECT %s,%s(viewers) FROM show" % (window.groupOption.get(), window.aggOption.get())
        # For every entry in our search term, we will add it to our query 
        if entryList:
            viewerQuery += " WHERE %s IN ( " % (window.searchOption.get())
            allEntries = []
            for entry in entryList:
                allEntries.append("'" +entry +"'")
            viewerQuery += ",".join(allEntries) +")"
        viewerQuery += " group by %s" % (window.groupOption.get()) 
        queryResults = (DBwork.executeQuery(viewerQuery))
        window.modifyViewList([window.groupOption.get(),'Viewers'],queryResults)

    #Call back to clear out form entry
    def entryListCallBack(self,event):
        self.entry.delete(0,'end')
        return None

    #Query to return valid search terms on bottom box
    def sortMenuCallBack(*args):
        window = args[0]
        window.selections.delete('0','end')
        if window.searchOption.get() not in window.sortSelection:
            print('Need to enter a search option')
        searchQuery = "SELECT DISTINCT %s FROM show" %(window.searchOption.get())
        queryRes = DBwork.executeQuery(searchQuery)
        for result in queryRes:
            window.selections.insert(tk.END,result)
        

    #When we execute a query, this function will take care of  printing results
    def modifyViewList(self,columns,queryResults):
        self.tvMenu.delete(*self.tvMenu.get_children())
        self.tvMenu['columns'] = columns
        self.tvMenu.column('#0', minwidth=0, stretch=tk.NO)
        self.tvMenu.heading("#0",text = '', anchor = tk.CENTER)
        for newColumn in self.tvMenu['columns']:
            self.tvMenu.column(newColumn,minwidth=60, stretch = tk.NO)
            self.tvMenu.heading(newColumn,text = newColumn)
        for result in queryResults:
            self.tvMenu.insert("",'end',values = result)
        self.tvMenu.pack(side="bottom")


if __name__ == "__main__":

    root = tk.Tk()
    app = Window(root)


    root.wm_title("Show viewer explorer")
    root.geometry("500x600")
    root.mainloop()
