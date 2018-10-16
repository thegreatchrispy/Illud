from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog
import os

class Illud:
	__root = Tk()

	# Default sizes and colors
	__width = 100
	__height = 30
	__bg = '#1576B0'
	__fg = '#F0F0F0'

	# Default text area
	__textArea = None
	__state = None # State can be 'new', 'edited', or 'current'
	__menu = Menu(__root)
	__fileMenu = Menu(__menu, tearoff=0)
	# __editMenu = Menu(__menu, tearoff=0)
	# __frmtMenu = Menu(__menu, tearoff=0)
	# __viewMenu = Menu(__menu, tearoff=0)
	# __helpMenu = Menu(__menu, tearoff=0)

	# Default file name
	__file = None

	# Initialize object
	def __init__(self):
		# Set icon
		# TODO

		# Initialize window (size and state)
		self.__textArea = scrolledtext.ScrolledText(self.__root, width=self.__width, height=self.__height, bg=self.__bg, fg=self.__fg, insertbackground=self.__fg)
		self.__state = 'new'
		self.__root.title('Untitled - Illud')

		# File menu
		self.__menu.add_cascade(label='File', menu=self.__fileMenu)
		self.__fileMenu.add_command(label='New', command=self.__newFile, accelerator='Ctrl+N')

		self.__root.config(menu=self.__menu)
		self.__textArea.pack()

	def __newFile(self):
		if self.__state in ('new', 'current'):
			self.__textArea.delete('1.0', END)
			self.__root.title('Untitled - Illud')
			self.__state = 'new'


	def main(self):
		self.__root.mainloop()

if __name__ == '__main__':
	illud = Illud()
	illud.main()