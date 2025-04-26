from  ScraperScraping import scrapeInternetLink as ss
from tkinter import *
import tkinter as tk
def scrapeInternetLink():
    global text
    text = ss()
def makeWindow():
    #sets up my main tkinter window
    global window
    window = tk.Tk()
    window.geometry("1000x700")
    window.title("Neumont Calender")
#this lets me use the middle mouse wheel to scroll down the frame
def on_configure(event):
    canva.configure(scrollregion = canva.bbox("all"))
def _on_mousewheel(event):
    canva.yview_scroll(int(-1 * (event.delta / 120)), "units")
def structerWindow():
    #sets up the frame inside the frame so that i can scroll around in it, also makes a canvas so that i can scroll inside it
    global window, canva, cornerWindow
    canva = Canvas(window, bg = "gray6")
    scrollBar = Scrollbar(window, orient = "vertical", command = canva.yview)
    canva.configure(yscrollcommand = scrollBar.set)
    scrollBar.pack(side = RIGHT, fill = Y)
    canva.pack(side = LEFT, fill = BOTH, expand = True)
    cornerWindow = Frame(canva, bg = "gray6")
    canva.create_window((0, 0), window = cornerWindow, anchor = "center")
    cornerWindow.bind("<Configure>", on_configure)
    canva.bind_all("<MouseWheel>", _on_mousewheel)
    #sets up the UI for the Frame
    title = Label(cornerWindow,font = ("CourierNew16Bold",30), text = "NEUMONT ACADEMIC CALENDAR", fg = "darkGoldenRod1",bg = "gray6")
    title.pack(anchor = "w", padx = 10, pady = 15)
def scrollToTop():
    global canva
    canva.yview_moveto(0)
#this formates a UI Label
def makeCalenderSection(startDate, seasonTitle):
    global text, cornerWindow
    quarter = ""
    start = text.find(startDate)
    end = text.find("Last Day of Class",start) + len("Last Day of Class")
    if(start != -1 and end != -1 and start < end):
        section = text[start:end]
        quarter = quarter + section
    quarterLabel = Label(cornerWindow, font = ("Courier", 10), text = f"{seasonTitle}\n\n" + quarter,
                    fg = "darkGoldenRod1", bg = "gray21", justify = "center", anchor = "center", wraplength = 900)
    quarterLabel.pack(pady = 10)
#makes the UI
def make2021_2022Calender():
    makeCalenderSection("Jan 6", "Winter 2021")
    makeCalenderSection("Mar 29", "Spring 2021")
    makeCalenderSection("Jun 28", "Summer 2021")
    makeCalenderSection("Sep 27 - Oct 1", "Fall 2021")
    makeCalenderSection("Jan 5", "Winter 2022")
    makeCalenderSection("Mar 28", "Spring 2022")
    makeCalenderSection("Jun 27", "Summer 2022")
    makeCalenderSection("Sep 23 - Sep 30", "Fall 2022")
    #puts you back at the top of the page
    window.after(100, scrollToTop)
def setUpStarterWindow():
    global starterBackground, starterTitle, scrapeButton
    starterBackground = Label(window, bg="gray6")
    starterBackground.pack(fill="both",expand=True)
    starterTitle = Label(window,font = ("CourierNew16Bold",30), text = "Web Scraper for Calender", fg = "darkGoldenRod1",bg = "gray6")
    starterTitle.pack()
    starterTitle.place(x= 10, y= 20)
    scrapeButton = Button(window, text="SCRAPE", command=scrapeNeumontCalender, font=("Helvetica", 40, "bold"), fg = "darkGoldenRod1", bg="gray21")
    scrapeButton.pack()
    scrapeButton.place(y=250 , x= 380)
def scrapeNeumontCalender():
    starterBackground.pack_forget()
    starterTitle.pack_forget()
    scrapeButton.pack_forget()
    scrapeInternetLink()
    structerWindow()
    make2021_2022Calender()
def main():
    makeWindow()
    setUpStarterWindow()
    #runs the GUI
    window.mainloop()
if __name__ == "__main__":
    main()