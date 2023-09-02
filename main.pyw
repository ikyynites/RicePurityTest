from pathlib import Path
from json import load
from tkinter import *
import customtkinter as ctk

# initialise paths
icon_path: Path = Path("assets/favicon.ico")
header_path: Path = Path("assets/thresher_official.png")
owl_path: Path = Path("assets/owl.png")
texts_path: Path = Path("assets/text.json")
question_path: Path = Path("questions.db")

# initialise texts
with open(texts_path, "r") as texts_io:
    __texts: dict[str, str] = load(texts_io)

    description: str = str(__texts.get("description"))
    disclaimer: str = str(__texts.get("disclaimer"))
    instructions: str = str(__texts.get("instructions"))

    del __texts

class Question:
    def __init__(self, completed: bool, index: int, question: str):
        self.completed: bool = completed
        self.index: int = index
        self.question: question = question

    def __repr__(self):
        # 4 + 128 chars < --------- sign bit --------- >< ----------------- index bits --------------- >
        header: str = f"{'1' if self.completed else '0'}{str(self.index).rjust(3, '0')}"
        footer: str = self.question.ljust(128, "\0")

        # exactly 132 chars
        return f"{header}{footer}"

def load_questions() -> list[Question]:
    questions: list[Question] = []

    with open(question_path, "r") as questions_io:
        while question_raw := questions_io.read(132):
            completed: bool = bool(int(question_raw[0:1]))
            index: int = int(question_raw[1:4])
            question: str = str(question_raw[4:]).strip("\0")

            questions.append(Question(completed, index, question))

    return questions

def save_questions(questions: list[Question]) -> None:
    with open(question_path, "w") as questions_io:
        for question in questions:
            questions_io.write(repr(question))

def reset_questions() -> None:
    questions: list[Question] = [Question(False, 1, "Held hands romantically?"),
                                 Question(False, 2, "Been on a date?"),
                                 Question(False, 3, "Been in a relationship?"),
                                 Question(False, 4, "Danced without leaving room for Jesus?"),
                                 Question(False, 5, "Kissed a non-family member?"),
                                 Question(False, 6, "Kissed a non-family member on the lips?"),
                                 Question(False, 7, "French kissed?"),
                                 Question(False, 8, "French kissed in public?"),
                                 Question(False, 9, "Kissed on the neck?"),
                                 Question(False, 10, "Kissed horizontally?"),
                                 Question(False, 11, "Given or received a hickey?"),
                                 Question(False, 12, "Kissed or been kissed on the breast?"),
                                 Question(False, 13, "Kissed someone below the belt?"),
                                 Question(False, 14, "Kissed for more than two hours consecutively?"),
                                 Question(False, 15, "Played a game involving stripping?"),
                                 Question(False, 16, "Seen or been seen by another person in a sensual context?"),
                                 Question(False, 17, "Masturbated?"),
                                 Question(False, 18, "Masturbated to a picture or video?"),
                                 Question(False, 19, "Masturbated while someone else was in the room?"),
                                 Question(False, 20, "Been caught masturbating?"),
                                 Question(False, 21, "Masturbated with an inanimate object?"),
                                 Question(False, 22, "Seen or read pornographic material?"),
                                 Question(False, 23, "Massaged or been massaged sensually?"),
                                 Question(False, 24, "Gone through the motions of intercourse while fully dressed?"),
                                 Question(False, 25, "Undressed or been undressed by a MPS (member of the preferred sex)?"),
                                 Question(False, 26, "Showered with a MPS?"),
                                 Question(False, 27, "Fondled or had your butt cheeks fondled?"),
                                 Question(False, 28, "Fondled or had your breasts fondled?"),
                                 Question(False, 29, "Fondled or had your genitals fondled?"),
                                 Question(False, 30, "Had or given \"blue balls\"?"),
                                 Question(False, 31, "Had an orgasm due to someone else’s manipulation?"),
                                 Question(False, 32, "Sent a sexually explicit text or instant message?"),
                                 Question(False, 33, "Sent or received sexually explicit photographs?"),
                                 Question(False, 34, "Engaged in sexually explicit activity over video chat?"),
                                 Question(False, 35, "Cheated on a significant other during a relationship?"),
                                 Question(False, 36, "Purchased contraceptives?"),
                                 Question(False, 37, "Gave oral sex?"),
                                 Question(False, 38, "Received oral sex?"),
                                 Question(False, 39, "Ingested someone else’s genital secretion?"),
                                 Question(False, 40, "Used a sex toy with a partner?"),
                                 Question(False, 41, "Spent the night with a MPS?"),
                                 Question(False, 42, "Been walked in on while engaging in a sexual act?"),
                                 Question(False, 43, "Kicked a roommate out to commit a sexual act?"),
                                 Question(False, 44, "Ingested alcohol in a non-religious context?"),
                                 Question(False, 45, "Played a drinking game?"),
                                 Question(False, 46, "Been drunk?"),
                                 Question(False, 47, "Faked sobriety to parents or teachers?"),
                                 Question(False, 48, "Had severe memory loss due to alcohol?"),
                                 Question(False, 49, "Used tobacco?"),
                                 Question(False, 50, "Used marijuana?"),
                                 Question(False, 51, "Used a drug stronger than marijuana?"),
                                 Question(False, 52, "Used methamphetamine, crack cocaine, PCP, horse tranquilizers or heroin?"),
                                 Question(False, 53, "Been sent to the office of a principal, dean or judicial affairs representative for a disciplinary infraction?"),
                                 Question(False, 54, "Been put on disciplinary probation or suspended?"),
                                 Question(False, 55, "Urinated in public?"),
                                 Question(False, 56, "Gone skinny-dipping?"), Question(False, 57, "Gone streaking?"),
                                 Question(False, 58, "Seen a stripper?"),
                                 Question(False, 59, "Had the police called on you?"),
                                 Question(False, 60, "Run from the police?"),
                                 Question(False, 61, "Had the police question you?"),
                                 Question(False, 62, "Had the police handcuff you?"),
                                 Question(False, 63, "Been arrested?"),
                                 Question(False, 64, "Been convicted of a crime?"),
                                 Question(False, 65, "Been convicted of a felony?"),
                                 Question(False, 66, "Committed an act of vandalism?"),
                                 Question(False, 67, "Had sexual intercourse?"),
                                 Question(False, 68, "Had sexual intercourse three or more times in one night?"),
                                 Question(False, 69, "?"),
                                 Question(False, 70, "Had sexual intercourse 10 or more times?"),
                                 Question(False, 71, "Had sexual intercourse in four or more positions?"),
                                 Question(False, 72, "Had sexual intercourse with a stranger or person you met within 24 hours?"),
                                 Question(False, 73, "Had sexual intercourse in a motor vehicle?"),
                                 Question(False, 74, "Had sexual intercourse outdoors?"),
                                 Question(False, 75, "Had sexual intercourse in public?"),
                                 Question(False, 76, "Had sexual intercourse in a swimming pool or hot tub?"),
                                 Question(False, 77, "Had sexual intercourse in a bed not belonging to you or your partner?"),
                                 Question(False, 78, "Had sexual intercourse while you or your partner’s parents were in the same home?"),
                                 Question(False, 79, "Had sexual intercourse with non-participating third party in the same room?"),
                                 Question(False, 80, "Joined the mile high club?"),
                                 Question(False, 81, "Participated in a \"booty call\" with a partner whom you were not in a relationship with?"),
                                 Question(False, 82, "Traveled 100 or more miles for the primary purpose of sexual intercourse?"),
                                 Question(False, 83, "Had sexual intercourse with a partner with a 3 or more year age difference?"),
                                 Question(False, 84, "Had sexual intercourse with a virgin?"),
                                 Question(False, 85, "Had sexual intercourse without a condom?"),
                                 Question(False, 86, "Had a STI test due to reasonable suspicion?"),
                                 Question(False, 87, "Had a STI?"),
                                 Question(False, 88, "Had a threesome?"),
                                 Question(False, 89, "Attended an orgy?"),
                                 Question(False, 90, "Had two or more distinct acts of sexual intercourse with two or more people within 24 hours?"),
                                 Question(False, 91, "Had sexual intercourse with five or more partners?"),
                                 Question(False, 92, "Been photographed or filmed during sexual intercourse by yourself or others?"),
                                 Question(False, 93, "Had period sex?"),
                                 Question(False, 94, "Had anal sex?"),
                                 Question(False, 95, "Had a pregnancy scare?"),
                                 Question(False, 96, "Impregnated someone or been impregnated?"),
                                 Question(False, 97, "Paid or been paid for a sexual act?"),
                                 Question(False, 98, "Committed an act of voyeurism?"),
                                 Question(False, 99, "Committed an act of incest?"),
                                 Question(False, 100, "Engaged in bestiality?")]

    with open(question_path, "w") as questions_io:
        for question in questions:
            questions_io.write(repr(question))

class QuestionContainer(ctk.CTkScrollableFrame):
    def __init__(self, master, values: list[Question]):
        super().__init__(master, fg_color="transparent", scrollbar_fg_color="#F1F1F1", scrollbar_button_color="#C1C1C1")

        # initialise font
        self.font: ctk.CTkFont = ctk.CTkFont(family="Times New Roman", size=16)

        # initialise variables
        self.values: list[Question] = values
        self.labels: list[ctk.CTkLabel] = []
        self.checkboxes: list[ctk.CTkCheckBox] = []

        # initialise and draw labels and checkboxes to frame
        for index, question in enumerate(self.values):
            # initialise and place index label
            label: ctk.CTkLabel = ctk.CTkLabel(self, text=f"{' ' * ((3 - len(str(question.index))) * 2)}{question.index}.",
                                 text_color="black", font=self.font)
            label.place(x=0, y=(index * 24) - 1)

            # add label to list
            self.labels.append(label)

            # initialise and place checkbox
            checkbox: ctk.CTkCheckBox = ctk.CTkCheckBox(self, text=question.question, command=lambda i=index: self.toggle_value(i),
                                                        checkbox_width=17, checkbox_height=17, corner_radius=3,
                                                        border_color="gray", border_width=2, text_color="black", font=self.font)
            checkbox.grid(row=index, column=0, padx=(36, 0), sticky=W)

            # select checkbox if completed
            if question.completed:
                checkbox.select()

            # add checkbox to list
            self.checkboxes.append(checkbox)

    def reset_checkboxes(self) -> None:
        for question in self.values:
            question.completed = False
        for checkbox in self.checkboxes:
            checkbox.deselect()

    def toggle_value(self, index) -> None:
        self.values[index].completed = not self.values[index].completed

    def score(self) -> int:
        purity: int = 100
        for question in self.values:
            if question.completed:
                purity -= 1
        return purity

class App(ctk.CTk):
    def __init__(self, questions: list[Question]):
        super().__init__(fg_color="#FBEEC8")

        # initialise app constants
        self.width: int = 1600
        self.height: int = 900

        # initialise fonts
        self.font: ctk.CTkFont = ctk.CTkFont(family="Times New Roman", size=16)
        self.italic: ctk.CTkFont = ctk.CTkFont(family="Times New Roman", slant="italic", size=16)
        self.bold: ctk.CTkFont = ctk.CTkFont(family="Times New Roman", weight="bold", size=16)
        self.font_bigger: ctk.CTkFont = ctk.CTkFont(family="Times New Roman", weight="bold", size=24)
        self.font_biggest: ctk.CTkFont = ctk.CTkFont(family="Times New Roman", weight="bold", size=48)

        # initialise window
        self.iconbitmap(icon_path)
        self.title("Rice Thresher Purity Test")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # load images
        self.__owl_image: PhotoImage = PhotoImage(file=owl_path)
        self.__header_image: PhotoImage = PhotoImage(file=header_path)

        # initialise and draw to background
        self.background: ctk.CTkCanvas = ctk.CTkCanvas(self, width=self.width, height=self.height, bg="#FBEEC8")
        for x in range(0, self.width, self.__owl_image.width()):
            for y in range(0, self.height, self.__owl_image.height()):
                self.background.create_image(x, y, anchor=NW, image=self.__owl_image)
        self.background.create_image(self.width / 2, 16, anchor=N, image=self.__header_image)

        # draw background to window
        self.background.place(x=0, y=0)

        # initialise frame
        self.to_hide: ctk.CTkFrame = ctk.CTkFrame(self, width=623, height=142, fg_color="transparent")

        # initialise and draw labels to frame
        self.__label_args: dict[str, str | int] = {"text_color": "black", "padx": 0, "pady": 0}
        self.label_description: ctk.CTkLabel = ctk.CTkLabel(self.to_hide, text=description, font=self.italic, **self.__label_args)
        self.label_description.place(x=623 / 2, y=0, anchor=N)
        self.label_disclaimer: ctk.CTkLabel = ctk.CTkLabel(self.to_hide, text=disclaimer, font=self.bold, **self.__label_args)
        self.label_disclaimer.place(x=623 / 2, y=68, anchor=N)
        self.label_instructions: ctk.CTkLabel = ctk.CTkLabel(self.to_hide, text=instructions, font=self.font, **self.__label_args)
        self.label_instructions.place(x=623 / 2, y=120, anchor=N)

        # draw frame to window
        self.to_hide.place(x=self.width / 2, y=146, anchor=N)

        # initialise question frame
        self.question_frame: QuestionContainer = QuestionContainer(self, questions)
        self.question_frame.grid(row=0, column=0, padx=10, pady=(330, 30), sticky=NSEW)

        # initialise and draw buttons
        self.__button_args: dict[str, str | int | ctk.CTkFont] = {"width": 131, "height": 17, "corner_radius": 10,
                                                                  "border_width": 2, "fg_color": "#D1F3CE", "hover_color": "#D1F3CE",
                                                                  "border_color": "black", "text_color": "black", "font": self.font}
        self.button_calculate: ctk.CTkButton = ctk.CTkButton(self, text="Calculate My Score!", command=self.calculate_score, **self.__button_args)
        self.button_calculate.place(x=10, y=869)
        self.button_reset: ctk.CTkButton = ctk.CTkButton(self, text="Clear checkboxes", command=self.question_frame.reset_checkboxes, **self.__button_args)
        self.button_reset.place(x=161, y=869)
        self.button_save: ctk.CTkButton = ctk.CTkButton(self, text="Save checkboxes", command=self.save, **self.__button_args)
        self.button_save.place(x=298, y=869)


    def save(self) -> None:
        save_questions(self.question_frame.values)

    def calculate_score(self) -> None:
        # save checkboxes and calculate purity
        self.save()
        purity: int = self.question_frame.score()

        # hide the previous ui
        self.to_hide.place_forget()
        self.to_hide.destroy()
        self.question_frame.grid_forget()
        self.question_frame.destroy()
        self.button_calculate.place_forget()
        self.button_calculate.destroy()
        self.button_reset.place_forget()
        self.button_reset.destroy()
        self.button_save.place_forget()
        self.button_save.destroy()

        # initialise and place score labels
        label_score: ctk.CTkLabel = ctk.CTkLabel(self, text="Your Score:", text_color="black", font=self.font_bigger)
        label_score.place(x=self.width / 2, y=150, anchor=N)
        label_purity: ctk.CTkLabel = ctk.CTkLabel(self, text=str(purity), text_color="red", font=self.font_biggest)
        label_purity.place(x=self.width / 2, y=200, anchor=N)

def main() -> None:
    # create questions.db file
    if question_path.is_dir():
        question_path.rename("questions.db.old")
    if not question_path.exists():
        reset_questions()

    # load questions
    questions: list[Question] = load_questions()

    # display window
    app: App = App(questions)
    app.mainloop()

if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    main()