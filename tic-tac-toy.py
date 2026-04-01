import customtkinter as ctk
from tkinter import messagebox

class TicTacToeUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI Search Playground")
        self.geometry("400x550")

        self.board_array = [0] * 9
        self.game_over = False
        
        self.buttons = []
        self.setup_ui()

    def setup_ui(self):
        self.label = ctk.CTkLabel(self, text="أنت تلعب بـ (O) - ابدأ اللعب", font=("Arial", 16, "bold"))
        self.label.pack(pady=20)

        self.grid_frame = ctk.CTkFrame(self)
        self.grid_frame.pack(pady=10, padx=20)

        for i in range(9):
            btn = ctk.CTkButton(self.grid_frame, text="", width=100, height=100,
                                 font=("Arial", 30, "bold"),
                                 command=lambda i=i: self.on_click(i))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        self.reset_btn = ctk.CTkButton(self, text="إعادة ضبط اللعبة", command=self.reset_board)
        self.reset_btn.pack(pady=20)

    def check_winner(self,state):
        win_states = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]            
        ]

        for j in win_states:
            total = sum(state[i] for i in j)
            if total == 3:
                return "X" 
            if total == -3:
                return "O" 
        
        if 0 not in state:
            return "Draw" 
            
        return None

    def redraw_board(self):
        symbols = {1: "X", -1: "O", 0: ""}
        colors = {1: "#FF5733", -1: "#33FF57", 0: ["#3B8ED0", "#1F6AA5"]}
        
        for i in range(9):
            val = self.board_array[i]
            self.buttons[i].configure(text=symbols[val], fg_color=colors[val])
            if val != 0 or self.game_over:
                self.buttons[i].configure(state="disabled")
            else:
                self.buttons[i].configure(state="normal")

    def on_click(self, i):
        if self.game_over: return

        self.board_array[i] = -1
        self.redraw_board()
        
        winner = self.check_winner(self.board_array)
        if winner:
            self.handle_end_game(winner)
            return

        self.label.configure(text="الخوارزمية تبحث...")
        self.after(500, self.minMaxSearch)
    def generateStates(self,state,role):
        role_val = 1 if role == "X" else -1
        states = list()
        for i in range(9):
            if state[i] == 0:
                new_state = state.copy()
                new_state[i] = role_val
                states.append(new_state)
        return states        
                
        
    def minMaxSearch(self):
        branch = self.generateStates(self.board_array , "X")
        maxu = -101
        index_of_best_state = 0
        for i in branch:
            u=self.min(i , 0)
            if u > maxu:
                maxu = u
                index_of_best_state = i       
        self.board_array=index_of_best_state.copy()    

        self.redraw_board()
        winner = self.check_winner(self.board_array)
        if winner:
            self.handle_end_game(winner)
        else:
            self.label.configure(text="دورك الان")
    def max(self , state , branch):
        utility = self.getUtility(branch , state)
        if utility != -1:
            return utility
        nbranch = self.generateStates(state , "X")
        maxu = -101 #bigger than all utilites
        for i in nbranch:
           u = self.min(i , branch+1)
           if u > maxu:
               maxu=u
        return maxu       
            
    def min(self , state , branch):
        utility = self.getUtility(branch , state)
        if utility != -1:
            return utility
        nbranch = self.generateStates(state , "O")
        minu = 101 #smaller than all utilites
        for i in nbranch:
           u = self.max(i , branch+1)
           if u < minu:
               minu=u
        return minu            
    def getUtility(self, depth, state):
        winner = self.check_winner(state)
        if winner == "X":
            return 100 - depth
        if winner == "O":
            return -100
        if winner == "Draw":
            return 0
        
    
        if 0 not in state:
            return 0
            
        return -1    

    def handle_end_game(self, winner):
        self.game_over = True
        self.redraw_board() 
        if winner == "Draw":
            self.label.configure(text="انتهت المباراة: تعادل!")
        else:
            self.label.configure(text=f"انتهت المباراة: فوز {winner}")

    def reset_board(self):
        self.board_array = [0] * 9
        self.game_over = False
        self.redraw_board()
        self.label.configure(text="بدء مباراة جديدة - دورك (O)")

if __name__ == "__main__":
    app = TicTacToeUI()
    app.mainloop()