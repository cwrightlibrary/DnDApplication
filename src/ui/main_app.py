import tkinter as tk

import src.models.classes as classes
import src.models.races as races
from src.enums.class_constants import Skill
from src.models.character import Character


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DnD Character Creator")

        self.width: int = 400
        self.height: int = 550

        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()

        x = (s_width // 2) - (self.width // 2)
        y = (s_height // 2) - (self.height // 2)

        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)
        self.focus_force()

        self._setup_mappings()

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

        self.race_selection: tk.StringVar = tk.StringVar(value="Dragonborn")

        self.race_selector: tk.OptionMenu = tk.OptionMenu(frame, self.race_selection, *races.all_races)
        self.race_selector.grid(row=1, column=0, padx=5, pady=5, sticky="new")

    def _create_class_info_widgets(self, frame: tk.LabelFrame) -> None:
        frame.grid_rowconfigure((0, 1), weight=1)
        frame.grid_columnconfigure((0, 1), weight=1)

        class_label: tk.Label = tk.Label(frame, text="Choose Class")
        class_label.grid(row=0, column=0, padx=5, pady=5, sticky="sew")

        self.skill_label: tk.Label = tk.Label(frame, text="Choose 2 Skills")
        self.skill_label.grid(row=0, column=1, padx=5, pady=5, sticky="sew")

        self.skills_map: dict[str, list[str]] = {
            "Barbarian": [s.value for s in classes.Barbarian().skill_options],
            "Bard": [s.value for s in classes.Bard().skill_options],
            "Cleric": [s.value for s in classes.Cleric().skill_options],
            "Druid": [s.value for s in classes.Druid().skill_options],
            # "Fighter": [s.value for s in classes.Fighter().skill_options],
            "Monk": [],
            "Paladin": [s.value for s in classes.Paladin().skill_options],
            "Ranger": [s.value for s in classes.Ranger().skill_options],
            "Rogue": [s.value for s in classes.Rogue().skill_options],
            "Sorcerer": [s.value for s in classes.Sorcerer().skill_options],
            "Warlock": [s.value for s in classes.Warlock().skill_options],
            "Wizard": [s.value for s in classes.Wizard().skill_options],
        }
        self.amount_of_skills_map: dict[str, int] = {
            "Barbarian": classes.Barbarian().choose_skills,
            "Bard": classes.Bard().choose_skills,
            "Cleric": classes.Cleric().choose_skills,
            "Druid": classes.Druid().choose_skills,
            # "Fighter": classes.Fighter().choose_skills,
            "Monk": 0,
            "Paladin": classes.Paladin().choose_skills,
            "Ranger": classes.Ranger().choose_skills,
            "Rogue": classes.Rogue().choose_skills,
            "Sorcerer": classes.Sorcerer().choose_skills,
            "Warlock": classes.Warlock().choose_skills,
            "Wizard": classes.Wizard().choose_skills,
        }

        self.class_var: tk.StringVar = tk.StringVar(value="Barbarian")
        self.skill_var: tk.StringVar = tk.StringVar()

        self.class_menu = tk.OptionMenu(
            frame,
            self.class_var,
            *self.skills_map.keys(),
            command=self._update_class_options # type:ignore
        )
        self.class_menu.grid(row=1, column=0, padx=5, pady=5, sticky="n")
        self.class_menu.config(width=20)

        self.MAX_SKILLS: int = self.amount_of_skills_map.get(self.class_var.get(), 0)

        self.skill_listbox = tk.Listbox(frame, selectmode="multiple", exportselection=0, height=6)
        self.skill_listbox.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.skill_listbox.bind("<<ListboxSelect>>", self._enforce_max_skills)

        scrollbar: tk.Scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.skill_listbox.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")
        self.skill_listbox.config(yscrollcommand=scrollbar.set)

        self._update_class_options(self.class_var.get())
    
    def _enforce_max_skills(self, event) -> None:
        selected_indices = self.skill_listbox.curselection()

        if len(selected_indices) > self.MAX_SKILLS:
            last_selected = selected_indices[-1]
            self.skill_listbox.selection_clear(last_selected)

    def _update_class_options(self, selection: str) -> None:
        self.MAX_SKILLS = self.amount_of_skills_map.get(self.class_var.get(), 0)
        self.skill_label.config(text=f"Choose {self.MAX_SKILLS} Skills")
        new_choices = self.skills_map.get(selection, [])

        self.skill_listbox.delete(0, tk.END)

        for choice in new_choices:
            self.skill_listbox.insert(tk.END, choice)
    
    def _get_selected_skills(self) -> list[str]:
        indices = self.skill_listbox.curselection()
        return [self.skill_listbox.get(i) for i in indices]
    
    def _setup_mappings(self):
        self.race_factory = {
            "Dragonborn": races.Dragonborn,
            "Dwarf": races.Dwarf,
            "Elf": races.Elf,
            "Gnome": races.Gnome,
            "Half-Elf": races.HalfElf,
            "Half-Orc": races.HalfOrc,
            "Halfling": races.Halfling,
            "Human": races.Human,
            "Tiefling": races.Tiefling,
        }

        self.class_factory = {
            "Barbarian": classes.Barbarian,
            "Bard": classes.Bard,
            "Cleric": classes.Cleric,
            "Druid": classes.Druid,
            "Fighter": classes.Fighter,
            "Monk": classes.Monk,
            "Paladin": classes.Paladin,
            "Ranger": classes.Ranger,
            "Rogue": classes.Rogue,
            "Sorcerer": classes.Sorcerer,
            "Warlock": classes.Warlock,
            "Wizard": classes.Wizard,
        }

    def create_user(self) -> None:
        name: str = self.user_entry.get()
        char: str = self.char_name_entry.get()
        level: str = str(self.level_entry.get())
        race: str = str(self.race_selection.get())
        class_s: str = str(self.class_var.get())
        skills: str = ", ".join(self._get_selected_skills())

        return_str: str = (
            "Created character:\n"
            f" Name: {name}\n"
            f" Character Name: {char}\n"
            f" Level: {level}\n"
            f" Race: {race}\n"
            f" Class: {class_s}\n"
            f" Skills: {skills}\n"
        )

        print(return_str)

        race_str = self.race_selection.get()
        class_str = self.class_var.get()

        RaceClass = self.race_factory.get(race_str, races.Human)
        JobClass = self.class_factory.get(class_str, classes.Barbarian)

        selected_skills = [s for s in Skill if s.value in self._get_selected_skills()]

        selected_race = RaceClass()
        if class_str not in ["Fighter", "Monk"]:
            selected_job = JobClass(chosen_skills=selected_skills)
        elif class_str == "Monk":
            selected_job = JobClass()
        
        character = Character(
            name=name,
            player_name=char,
            level=int(level),
            character_race=selected_race,
            character_class=selected_job,
        )
        character.save_pdf_character_sheet("out/usage_test.pdf")
