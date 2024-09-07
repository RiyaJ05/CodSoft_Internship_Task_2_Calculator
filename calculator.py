from tkinter import * 

# Classes
class TextLabel:
  def __init__(self, screen, label_text, font_family, font_size, fg_colour="#333333", bg_colour="#e6e6fa", photo_image=None, **kwargs):
    self.text_label = Label(screen,
                            text=label_text,
                            font=(font_family, font_size),
                            fg=fg_colour,
                            bg=bg_colour,
                            image=photo_image,
                            **kwargs)
    
  def get_label(self):
    return self.text_label
    
    
class MainFrame:
  def __init__(self, screen, bg_colour="#e6e6fa", **kwargs):
    self.main_frame = Frame(screen,
                            bg=bg_colour,
                            **kwargs)
    
  def get_frame(self):
    return self.main_frame


class DisplayEntry:
  def __init__(self, screen, font_family, font_size, fg_colour="#333333", bg_colour="#e6e6fa", **kwargs):
    self.display_entry = Entry(screen,
                              font=(font_family, font_size),
                              fg=fg_colour,
                              bg=bg_colour,
                              disabledbackground="#cce0ff",
                              **kwargs)
                        
  def get_entry(self):
    return self.display_entry
    
    
class CalcButton:
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
    
  def get_button(self):
    return self.calc_button
  
  
class ButtonController:
  def __init__(self, entry_widget):
    self.display_entry = entry_widget
    self.display_entry.config(state=DISABLED)
    
  def display(self, button_text):
    self.display_entry.config(state=NORMAL)
    self.display_entry.insert("end", button_text)
    
  def result(self):
    try:
      self.display_entry.config(state=NORMAL)
      expression = self.display_entry.get().strip()
      calc_result = eval(expression)
      self.display_entry.delete(0, END)
      self.display_entry.insert("end", str(calc_result))
      
    except ZeroDivisionError:
      self.display_entry.delete(0, END)
      self.display_entry.insert("end", "Can't divide by zero!")
    
    except Exception as e:
      self.display_entry.delete(0, END)
      self.display_entry.insert("end", "ERROR: Invalid input!")
      
  def clear(self):
    self.display_entry.config(state=NORMAL)
    self.display_entry.delete(0, END)
      
  
def main():
  # Initialising a window
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

  # Running the main loop
  window.mainloop()
  
  
if __name__ == "__main__":
  main()