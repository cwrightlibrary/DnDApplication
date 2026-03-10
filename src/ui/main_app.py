import customtkinter as ctk
import tkinter as tk

import src.models.classes as classes
import src.models.races as races
from src.enums.class_constants import Skill
from src.models.character import Character


class MainApplication(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.width: int = 800
        self.height: int = 600

        self.title("DnD Character Creator")

        self._center_window()
        self._bring_to_front()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1, 2), weight=1)

        self.player_name: tk.StringVar = tk.StringVar()
        self.character_name: tk.StringVar = tk.StringVar()
        self.level: tk.StringVar = tk.StringVar()
        self.race: tk.StringVar = tk.StringVar()

        self.level_raw: int = 1

        self._create_widgets()
        self.setup_stringvars()

        self.update_display()

    def _center_window(self) -> None:
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (self.width // 2)
        y = (screen_height // 2) - (self.height // 2)

        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def _bring_to_front(self) -> None:
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)
        self.focus_force()
    
    def setup_stringvars(self) -> None:
        self.player_name.trace_add("write", self.update_display)
        self.character_name.trace_add("write", self.update_display)
        self.level.trace_add("write", self.update_display)
        self.race.trace_add("write", self.update_display)
    
    def update_display(self, *args):
        player_name = self.player_name.get()
        character_name = self.character_name.get()
        level = self.level.get()
        race = self.race.get()

        display_text: str = (
            f"Player Name: {player_name}\n"
            f"Character Name: {character_name}\n"
            f"Level: {level}\n"
            f"Race: {race}\n"
            "\nMore..."
        )

        self.preview_textbox.configure(state="normal")
        self.preview_textbox.delete("1.0", "end")
        self.preview_textbox.insert("1.0", display_text)
        self.preview_textbox.configure(state="disabled")

    def _create_widgets(self) -> None:
        # Padding constants
        fpx: int = 20
        fpxh: int = fpx // 2

        fpy: int = 20
        fpyh: int = fpy // 2

        frame_padx_full: int = fpx
        frame_padx_left: tuple[int, int] = (fpx, fpxh)
        frame_padx_right: tuple[int, int] = (fpxh, fpx)

        frame_pady_full: int = fpy
        frame_pady_top: tuple[int, int] = (fpy, fpyh)
        frame_pady_mid: int = fpyh
        frame_pady_bot: tuple[int, int] = (fpyh, fpy)

        cpx: int = 8
        cpxh: int = cpx // 2

        cpy: int = 8
        cpyh: int = cpy // 2

        content_padx_full: int = cpx
        content_padx_left: tuple[int, int] = (cpx, cpxh)
        content_padx_mid: int = cpxh
        content_padx_right: tuple[int, int] = (cpxh, cpx)

        content_pady_full: int = cpy
        content_pady_top: tuple[int, int] = (cpy, cpyh)
        content_pady_mid: int = cpyh
        content_pady_bot: tuple[int, int] = (cpyh, cpy)

        # Fonts
        title_font: ctk.CTkFont = ctk.CTkFont(size=20, weight="bold")
        header_font: ctk.CTkFont = ctk.CTkFont(size=14)

        # Title label
        title_label: ctk.CTkLabel = ctk.CTkLabel(
            self, text="DnD Character Creator", font=title_font
        )
        title_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=frame_padx_full,
            pady=frame_pady_top,
            sticky="nsew",
        )

        # Names/level input
        names_level_input_frame: ctk.CTkFrame = ctk.CTkFrame(self)
        names_level_input_frame.grid(
            row=1,
            column=0,
            padx=frame_padx_left,
            pady=frame_pady_mid,
            sticky="nsew",
        )

        names_level_input_frame.grid_columnconfigure((0, 1, 2), weight=1)
        names_level_input_frame.grid_rowconfigure((0, 1), weight=1)

        player_name_label: ctk.CTkLabel = ctk.CTkLabel(
            names_level_input_frame,
            text="Your name",
            font=header_font,
        )
        player_name_label.grid(
            row=0, column=0, padx=content_padx_left, pady=content_pady_top, sticky="sew"
        )

        self.player_name_entry: ctk.CTkEntry = ctk.CTkEntry(
            names_level_input_frame, textvariable=self.player_name, placeholder_text="Jane Doe"
        )
        self.player_name_entry.grid(
            row=1, column=0, padx=content_padx_left, pady=content_pady_bot, sticky="new"
        )

        character_name_label: ctk.CTkLabel = ctk.CTkLabel(
            names_level_input_frame,
            text="Character name",
            font=header_font,
        )
        character_name_label.grid(
            row=0, column=1, padx=content_padx_mid, pady=content_pady_top, sticky="sew"
        )

        self.character_name_entry: ctk.CTkEntry = ctk.CTkEntry(
            names_level_input_frame, textvariable=self.character_name, placeholder_text="Gimlad"
        )
        self.character_name_entry.grid(
            row=1, column=1, padx=content_padx_mid, pady=content_pady_bot, sticky="new"
        )

        self.level_raw = 1

        self.level_label: ctk.CTkLabel = ctk.CTkLabel(
            names_level_input_frame, text=f"Level {self.level_raw}", font=header_font
        )
        self.level_label.grid(
            row=0,
            column=2,
            padx=content_padx_right,
            pady=content_pady_top,
            sticky="sew",
        )

        self.level_slider: ctk.CTkSlider = ctk.CTkSlider(
            names_level_input_frame,
            from_=1,
            to=20,
            number_of_steps=19,
            command=self.get_slider_content,
        )
        self.level_slider.set(self.level_raw)
        self.level_slider.grid(
            row=1,
            column=2,
            padx=content_padx_right,
            pady=(content_pady_bot[0] + 7, content_pady_bot[1]),
            sticky="new",
        )

        # Race/Class input
        race_class_input_frame: ctk.CTkFrame = ctk.CTkFrame(self)
        race_class_input_frame.grid(
            row=2, column=0, padx=frame_padx_left, pady=frame_pady_bot, sticky="nsew"
        )

        race_class_input_frame.grid_columnconfigure((0, 1), weight=1)
        race_class_input_frame.grid_rowconfigure((0, 1), weight=1)

        race_label: ctk.CTkLabel = ctk.CTkLabel(race_class_input_frame, text="Choose your race", font=header_font)
        race_label.grid(row=0, column=0, padx=content_padx_left, pady=content_pady_top, sticky="sew")

        all_races = [""] + races.all_races
        self.race_dropdown: ctk.CTkOptionMenu = ctk.CTkOptionMenu(race_class_input_frame, values=all_races, command=self.update_race)
        self.race_dropdown.grid(row=1, column=0, padx=content_padx_left, pady=content_pady_bot, sticky="new")

        # Preview panel
        preview_frame: ctk.CTkFrame = ctk.CTkFrame(self)
        preview_frame.grid(
            row=1,
            column=1,
            rowspan=2,
            padx=frame_padx_right,
            pady=(content_pady_top[0], frame_pady_full),
            sticky="nsew",
        )

        preview_frame.grid_columnconfigure(0, weight=1)
        preview_frame.grid_rowconfigure(0, weight=0)
        preview_frame.grid_rowconfigure(1, weight=1)

        # Current info
        preview_title: ctk.CTkLabel = ctk.CTkLabel(
            preview_frame, text="Preview", font=header_font
        )
        preview_title.grid(
            row=0,
            column=0,
            padx=content_padx_full,
            pady=content_pady_top,
            sticky="nsew",
        )

        self.preview_textbox: ctk.CTkTextbox = ctk.CTkTextbox(preview_frame)
        self.preview_textbox.grid(row=1, column=0, padx=content_padx_full, pady=content_pady_bot, sticky="nsew")

    def get_slider_content(self, value) -> None:
        self.level_raw = int(value)
        self.level.set(str(self.level_raw))
        self.level_label.configure(text=f"Level {self.level_raw}")
    
    def update_race(self, value) -> None:
        self.race.set(value)
