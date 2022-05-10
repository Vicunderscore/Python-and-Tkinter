import tkinter as tk
import string
import random

keys = string.ascii_letters
total_index = len(keys) - 1

class KeyMaster(tk.Tk):
    def __init__(self):
        super().__init__()

        'Footer'
        tk.Label(self, text='press ESC to exit', bg='gray').pack(side=tk.BOTTOM, fill=tk.X)

        self.bind('<Escape>', lambda e: self.destroy())
        self.START_FRAME = tk.Frame(self, bg='gray')
        self.start_page(self.START_FRAME)

        ''' Game Page '''
        self.GAME_FRAME = tk.Frame(self, bg='gray')
        self.label = tk.Label(self.GAME_FRAME,
                         bg='gray',
                         fg='Black',
                         font=('Times',45))
        self.label.pack(padx=20, pady=50)

    def start_page(self, win, bg='gray', fg='dark green'):
        self.START_FRAME.pack(expand=True, fill=tk.BOTH)

        label = tk.Label(win,
                         text='PRESS SPACE TO START',
                         font=('helvatica', 24, 'bold'),
                         fg=fg,
                         bg=bg)

        label.pack(side=tk.TOP, pady=200, padx=100)
        label.focus()
        label.bind('<space>', lambda e: self.transition())

    def transition(self):
        self.GAME_FRAME.pack(fill=tk.BOTH, expand=True)
        self.START_FRAME.destroy()
        self.game()

    def game(self):
        key = keys[random.randint(0, total_index)]
        self.label.config(text='Enter: \n' + key, fg='dark green')
        self.label.focus()

        self.label.bind(f'<{key}>', lambda e: self.game())



if __name__ == '__main__':
    KeyMaster().mainloop()
