import tkinter as tk

import src.models.classes as classes
import src.models.races as races
from src.enums.class_constants import Skill
from src.models.character import Character


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DnD Character Creator")

        self.width: int = 600
        self.height: int = 400

        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()

        x = (s_width // 2) - (self.width // 2)
        y = (s_height // 2) - (self.height // 2)

        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)
        self.focus_force()

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=1)

        user_info_frame: tk.LabelFrame = tk.LabelFrame(self, text="User Information")
        user_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self._create_user_info_widgets(user_info_frame)

        race_info_frame: tk.LabelFrame = tk.LabelFrame(self, text="Race Information")
        race_info_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self._create_race_info_widgets(race_info_frame)

        class_info_frame: tk.LabelFrame = tk.LabelFrame(self, text="Class Information")
        class_info_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self._create_class_info_widgets(class_info_frame)

        self.submit_btn: tk.Button = tk.Button(
            self, text="Submit", command=self.create_user
        )
        self.submit_btn.grid(row=3, column=0, padx=10, pady=10, sticky="sew")

    def _create_user_info_widgets(self, frame: tk.LabelFrame) -> None:
        frame.grid_rowconfigure((0, 1), weight=1)
        frame.grid_columnconfigure((0, 1, 2), weight=1)

        user_name_label: tk.Label = tk.Label(frame, text="Your Name")
        user_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="sew")

        self.user_entry: tk.Entry = tk.Entry(frame)
        self.user_entry.grid(row=1, column=0, padx=5, pady=5, sticky="new")

        char_name_label: tk.Label = tk.Label(frame, text="Character Name")
        char_name_label.grid(row=0, column=1, padx=5, pady=5, sticky="sew")

        self.char_name_entry: tk.Entry = tk.Entry(frame)
        self.char_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="new")

        level_label: tk.Label = tk.Label(frame, text="Level")
        level_label.grid(row=0, column=2, padx=5, pady=5, sticky="sew")

        self.level_entry: tk.Spinbox = tk.Spinbox(frame, from_=1, to=20, width=5)
        self.level_entry.grid(row=1, column=2, padx=5, pady=5, sticky="new")

    def _create_race_info_widgets(self, frame: tk.LabelFrame) -> None:
        frame.grid_rowconfigure((0, 1), weight=1)
        frame.grid_columnconfigure(0, weight=1)

        race_label: tk.Label = tk.Label(frame, text="Choose Race")
        race_label.grid(row=0, column=0, padx=5, pady=5, sticky="sew")

        self.race_selection: tk.StringVar = tk.StringVar(value="Barbarian")

        self.race_selector: tk.OptionMenu = tk.OptionMenu(frame, self.race_selection, *races.all_races)
        self.race_selector.grid(row=1, column=0, padx=5, pady=5, sticky="new")

    def _create_class_info_widgets(self, frame: tk.LabelFrame) -> None:
        pass

    def create_user(self) -> None:
        name: str = self.user_entry.get()
        char: str = self.char_name_entry.get()
        level: str = str(self.level_entry.get())

        return_str: str = (
            "Created character:\n"
            f" Name: {name}\n"
            f" Character Name: {char}\n"
            f" Level: {level}\n"
        )

        print(return_str)
