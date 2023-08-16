import tkinter as tk

def show_project_overview():
    project_window = tk.Toplevel(root)
    project_window.title("Projektübersicht")

    label_project_name = tk.Label(project_window, text="Projektname: " + entry_project_name.get())
    label_project_name.pack()

    label_start_date = tk.Label(project_window, text="Startdatum: " + entry_start_date.get())
    label_start_date.pack()

    label_end_date = tk.Label(project_window, text="Enddatum: " + entry_end_date.get())
    label_end_date.pack()

    label_responsible_person = tk.Label(project_window, text="Verantwortliche Person: " + entry_responsible_person.get())
    label_responsible_person.pack()

    # Weitere Knöpfe oder Steuerungsvariablen für die Projektübersicht können hier hinzugefügt werden

def submit():
    project_name = entry_project_name.get()
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()
    responsible_person = entry_responsible_person.get()

    print("Projektname:", project_name)
    print("Startdatum:", start_date)
    print("Enddatum:", end_date)
    print("Verantwortliche Person:", responsible_person)

    show_project_overview()

root = tk.Tk()
root.title("Projektplanungsanwendung")

label_project_name = tk.Label(root, text="Projektname:")
label_project_name.grid(row=0, column=0, padx=10, pady=5)

label_start_date = tk.Label(root, text="Startdatum:")
label_start_date.grid(row=1, column=0, padx=10, pady=5)

label_end_date = tk.Label(root, text="Enddatum:")
label_end_date.grid(row=2, column=0, padx=10, pady=5)

label_responsible_person = tk.Label(root, text="Verantwortliche Person:")
label_responsible_person.grid(row=3, column=0, padx=10, pady=5)

entry_project_name = tk.Entry(root)
entry_project_name.grid(row=0, column=1, padx=10, pady=5)

entry_start_date = tk.Entry(root)
entry_start_date.grid(row=1, column=1, padx=10, pady=5)

entry_end_date = tk.Entry(root)
entry_end_date.grid(row=2, column=1, padx=10, pady=5)

entry_responsible_person = tk.Entry(root)
entry_responsible_person.grid(row=3, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Bestätigen", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
