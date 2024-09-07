from tkinter import * 

# Classes

class TextLabel:
  """
  A class that encapsulates the creation of a Label widget with customizable properties.

  Attributes:
      screen: The parent widget (usually a window or frame) where the label will be placed.
      label_text: The text to be displayed on the label.
      font_family: The font family for the label text.
      font_size: The size of the font for the label text.
      fg_colour: The foreground color of the label text.
      bg_colour: The background color of the label.
      photo_image: An optional image to be displayed on the label.
      kwargs: Additional keyword arguments for the label widget.
  """
  def __init__(self, screen, label_text, font_family, font_size, fg_colour="#333333", bg_colour="#e6e6fa", photo_image=None, **kwargs):
    self.text_label = Label(screen,
                            text=label_text,
                            font=(font_family, font_size),
                            fg=fg_colour,
                            bg=bg_colour,
                            image=photo_image,
                            **kwargs)
    
  # Returns the label widget
  def get_label(self):
    return self.text_label
    
    
class MainFrame:
  """
  A class that encapsulates the creation of a Frame widget with customizable properties.

  Attributes:
      screen: The parent widget (usually a window) where the frame will be placed.
      bg_colour: The background color of the frame.
      kwargs: Additional keyword arguments for the frame widget.
  """
  def __init__(self, screen, bg_colour="#e6e6fa", **kwargs):
    self.main_frame = Frame(screen,
                            bg=bg_colour,
                            **kwargs)
    
  # Returns the frame widget
  def get_frame(self):
    return self.main_frame


class DisplayEntry:
  """
  A class that encapsulates the creation of an Entry widget with customizable properties.

  Attributes:
      screen: The parent widget (usually a frame) where the entry widget will be placed.
      font_family: The font family for the entry text.
      font_size: The size of the font for the entry text.
      fg_colour: The foreground color of the entry text.
      bg_colour: The background color of the entry widget.
      kwargs: Additional keyword arguments for the entry widget.
  """
  def __init__(self, screen, font_family, font_size, fg_colour="#333333", bg_colour="#e6e6fa", **kwargs):
    self.display_entry = Entry(screen,
                              font=(font_family, font_size),
                              fg=fg_colour,
                              bg=bg_colour,
                              disabledbackground="#cce0ff",
                              **kwargs)
   
  # Returns the entry widget
  def get_entry(self):
    return self.display_entry
    
    
class CalcButton:
  """
  A class that encapsulates the creation of a Button widget with customizable properties.

  Attributes:
      screen: The parent widget (usually a frame) where the button will be placed.
      button_text: The text to be displayed on the button.
      font_family: The font family for the button text.
      font_size: The size of the font for the button text.
      fg_colour: The foreground color of the button text.
      bg_colour: The background color of the button.
      active_bg: The background color when the button is active.
      active_fg: The foreground color when the button is active.
      btn_width: The width of the button.
      kwargs: Additional keyword arguments for the button widget.
  """
  def __init__(self, screen, button_text, font_family="Arial", font_size=18, fg_colour="#FFFFFF", bg_colour="#4d94ff", active_bg="#4d94ff", active_fg="#FFFFFF", btn_width=3, **kwargs):
    self.calc_button = Button(screen,
                              text=button_text,
                              font=(font_family, font_size),
                              fg=fg_colour,
                              bg=bg_colour,
                              activebackground=active_bg,
                              activeforeground=active_fg,
                              width=btn_width,
                              **kwargs)
    
  # Returns the button widget
  def get_button(self):
    return self.calc_button
  
  
class ButtonController:
  """
  A class that handles the functionality of calculator buttons including display, result calculation, and clearing the entry.

  Attributes:
      entry_widget: The Entry widget where the calculator input and results are displayed.
  """
  def __init__(self, entry_widget):
    self.display_entry = entry_widget
    self.display_entry.config(state=DISABLED)
    
  def display(self, button_text):
    """
    Inserts the given button_text into the entry widget.

    Args:
        button_text: The text to be inserted into the entry widget.
    """
    self.display_entry.config(state=NORMAL)
    self.display_entry.insert("end", button_text)
    
  def result(self):
    """
    Evaluates the expression in the entry widget and displays the result.
    Handles ZeroDivisionError and other exceptions with appropriate messages.
    """
    try:
      self.display_entry.config(state=NORMAL)
      expression = self.display_entry.get().strip()
      calc_result = eval(expression)
      self.display_entry.delete(0, END)
      self.display_entry.insert("end", str(calc_result))
      
    except ZeroDivisionError:
      self.display_entry.delete(0, END)
      self.display_entry.insert("end", "ERROR: Can't divide by zero!")
    
    except Exception as e:
      self.display_entry.delete(0, END)
      self.display_entry.insert("end", "ERROR: Invalid input!")
      
  def clear(self):
    self.display_entry.config(state=NORMAL)
    self.display_entry.delete(0, END)
      
  
def main():
  # Initialize the main window
  window = Tk()
  window.title("CALCULATOR")
  window.geometry("600x600")
  window.config(bg="#e6e6fa")

  # Image(s)
  calc_icon = PhotoImage(file="images/calculator.png")

  # Header Label
  header_label = TextLabel(window,
                     "CALCULATOR",
                     "Impact",
                     35,
                     "#ff4d6d",
                     photo_image=calc_icon,
                     compound=RIGHT,
                     padx=15).get_label()
  header_label.pack(pady=25)

  # Calculator Frame
  main_frame = MainFrame(window).get_frame()
  main_frame.pack()

  # Display Area Entry Widget
  display_area = DisplayEntry(main_frame,
                              "Arial",
                              18,
                              fg_colour="#333333",
                              bg_colour="#cce0ff",
                              relief=FLAT,
                              width=18).get_entry()
  display_area.grid(row=0, column=0, columnspan=4, ipady=12, pady=5)
  
  # Calculator Buttons Controller
  btn_controller = ButtonController(display_area)

  # Calculator Buttons
  calc_btn_7 = CalcButton(main_frame,
                          "7", 
                          command=lambda: btn_controller.display("7")).get_button()
  calc_btn_7.grid(row=1, column=0, padx=5, pady=5)
  
  calc_btn_8 = CalcButton(main_frame, 
                          "8",
                          command=lambda: btn_controller.display("8")).get_button()
  calc_btn_8.grid(row=1, column=1, padx=5, pady=5)
  
  calc_btn_9 = CalcButton(main_frame, 
                          "9",
                          command=lambda: btn_controller.display("9")).get_button()
  calc_btn_9.grid(row=1, column=2, padx=5, pady=5)
  
  calc_btn_divide = CalcButton(main_frame, 
                               "/",
                               command=lambda: btn_controller.display("/")).get_button()
  calc_btn_divide.grid(row=1, column=3, padx=5, pady=5)
  
  calc_btn_4 = CalcButton(main_frame, 
                          "4",
                          command=lambda: btn_controller.display("4")).get_button()
  calc_btn_4.grid(row=2, column=0, padx=5, pady=5)
  
  calc_btn_5 = CalcButton(main_frame, 
                          "5",
                          command=lambda: btn_controller.display("5")).get_button()
  calc_btn_5.grid(row=2, column=1, padx=5, pady=5)
  
  calc_btn_6 = CalcButton(main_frame, 
                          "6",
                          command=lambda: btn_controller.display("6")).get_button()
  calc_btn_6.grid(row=2, column=2, padx=5, pady=5)
  
  calc_btn_multiply = CalcButton(main_frame, 
                                  "*",
                                  command=lambda: btn_controller.display("*")).get_button()
  calc_btn_multiply.grid(row=2, column=3, padx=5, pady=5)
  
  calc_btn_3 = CalcButton(main_frame, 
                          "3",
                          command=lambda: btn_controller.display("3")).get_button()
  calc_btn_3.grid(row=3, column=0, padx=5, pady=5)
  
  calc_btn_2 = CalcButton(main_frame, 
                          "2",
                          command=lambda: btn_controller.display("2")).get_button()
  calc_btn_2.grid(row=3, column=1, padx=5, pady=5)
  
  calc_btn_1 = CalcButton(main_frame, 
                          "1",
                          command=lambda: btn_controller.display("1")).get_button()
  calc_btn_1.grid(row=3, column=2, padx=5, pady=5)
  
  calc_btn_subtract = CalcButton(main_frame, 
                                 "-",
                                 command=lambda: btn_controller.display("-")).get_button()
  calc_btn_subtract.grid(row=3, column=3, padx=5, pady=5)
  
  calc_btn_0 = CalcButton(main_frame, 
                          "0",
                          command=lambda: btn_controller.display("0")).get_button()
  calc_btn_0.grid(row=4, column=0, padx=5, pady=5)
  
  calc_btn_decimal = CalcButton(main_frame, 
                                ".",
                                command=lambda: btn_controller.display(".")).get_button()
  calc_btn_decimal.grid(row=4, column=1, padx=5, pady=5)
  
  calc_btn_equals = CalcButton(main_frame, 
                               "=",
                               command=btn_controller.result).get_button()
  calc_btn_equals.grid(row=4, column=2, padx=5, pady=5)
  
  calc_btn_add = CalcButton(main_frame, 
                            "+",
                            command=lambda: btn_controller.display("+")).get_button()
  calc_btn_add.grid(row=4, column=3, padx=5, pady=5)
  
  calc_btn_clear = CalcButton(main_frame, 
                              "C",
                              command=btn_controller.clear).get_button()
  calc_btn_clear.grid(row=5, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

  # Run the the main loop of the application
  window.mainloop()
  
  
if __name__ == "__main__":
  main()