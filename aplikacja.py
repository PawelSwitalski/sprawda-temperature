import tkinter
import strona

window = tkinter.Tk()



MyTitle = tkinter.Label(window, text = "Mój program", font = "Helvetica 16 bold")
MyTitle.pack()

def przycisk():
    dane_pogodowe = strona.Wyjsciowe()
    tekst_po_Przycisk.configure(text = "Miasto: " + str(dane_pogodowe.Miasto) + "\n" +
                                "dzień i godzina: " + str(dane_pogodowe.Dzien_Godzina) + "\n" +
                                str(dane_pogodowe.Temperatura) + "\n")
    tekst_po_Przycisk.pack()

Przycisk = tkinter.Button(window, text = "sprawdź pogodę", command = przycisk)
Przycisk.pack()

tekst_po_Przycisk = tkinter.Label(window, font="Helvetica 16 bold")
tekst_po_Przycisk.pack()


window.mainloop()
