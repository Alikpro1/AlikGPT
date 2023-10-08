import customtkinter as ctk

open = True







def updatemenu():
    global open

    def ban():
        global open
        open = True
        root.destroy()

    if open == True:
        open = False
        # Создайте главное окно
        root = ctk.CTk()
        root.title("test")
        root.minsize(800, 375)
        root.resizable(False, False)
        root.protocol("WM_DELETE_WINDOW", ban)

        tab = ctk.CTkTabview(root)
        tab.pack(fill="both", expand=True, padx=1, pady=1)

        def tab_text(tabname, font1, font2):
            add_tab = tab.add(tabname)
            text = ctk.CTkTextbox(tab.tab(add_tab))
            text.configure(font=(font1, font2), state='disabled')
            text.insert("0.0", "Список задач, которые находятся у меня в работе на данный момент.")
            text.pack(fill="both", expand=True, padx=1, pady=1)

        #tab_text('Priority', 'Arial', 21)


        root.mainloop()


