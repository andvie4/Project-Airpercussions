
import customtkinter


def create_button(root, command, text):
    if text == "Quit":
        button = customtkinter.CTkButton(master=root, text=text, command=command,
                                         text_color="black", fg_color="#F77e6a", hover_color="red",
                                         text_font="Papyrus",corner_radius=30,bg_color="#fbfafb")
    else:
        button = customtkinter.CTkButton(master=root, text=text, command=command,
                                         text_color="black", fg_color="#f4f0e1", hover_color="#C99df7",
                                         text_font="Papyrus",corner_radius=30,bg_color="#fbfafb")

    return button
