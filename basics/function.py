#function = A block of reusable code place
    #    after the function name to invoke it 

def display_invoice(username, amt, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amt:.2f} is due : {due_date}")

display_invoice("Hitler", 120.34, "08/10")

 