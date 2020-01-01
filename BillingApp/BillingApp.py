from tkinter import *
import sqlite3

window = Tk()
window.title("Billing App")
window.geometry("550x300")

conn = sqlite3.connect("myDatabase.db")
curse = conn.cursor()

'''' curse.execute("CREATE TABLE customer_data(customer_ID integer, first_name text, last_name text, product_name text,"
              "product_price integer, quantity integer)") '''

TEXTS = ["Customer ID", "First Name", "Last Name", "Product Name", "Product Price", "Quantity"]

data = ""

i = 0
for text in TEXTS:
    label = Label(window, text=text, anchor=W, justify=LEFT).grid(row=i, column=0, sticky=W, padx=5, pady=5)
    i += 1


def add():
    conn = sqlite3.connect("myDatabase.db")
    curse = conn.cursor()

    curse.execute("INSERT INTO customer_data VALUES (:c_id, :f_name, :l_name, :p_name, :p_price, :quantity)",
                  {
                      'c_id': c_id.get(),
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'p_name': p_name.get(),
                      'p_price': p_price.get(),
                      'quantity': quantity.get()
                  })

    conn.commit()
    conn.close()

    c_id.delete(0, END)
    f_name.delete(0, END)
    l_name.delete(0, END)
    p_name.delete(0, END)
    p_price.delete(0, END)
    quantity.delete(0, END)


def show_data():
    records = Tk()
    records.title("Customer Records")
    records.geometry("550x300")
    conn = sqlite3.connect("myDatabase.db")
    curse = conn.cursor()
    curse.execute("SELECT *, oid FROM customer_data")
    global data
    data = curse.fetchall()
    j = 1
    for texts in data:
        info = texts
        id = info[0]
        cust_name = str(info[1] + info[2])
        product_name  = info[3]
        product_price = info[4]
        label_id = Label(records, text=id, anchor=W, justify=LEFT).grid(row=j, column=0, sticky=W, padx=5, pady=5)
        label_name = Label(records, text=cust_name, anchor=W, justify=LEFT).grid(row=j, column=1, sticky=W, padx=5, pady=5)
        label_p_name = Label(records, text=product_name, anchor=W, justify=LEFT).grid(row=j, column=2, sticky=W, padx=5, pady=5)
        label_p_price = Label(records, text=product_price, anchor=W, justify=LEFT).grid(row=j, column=3, sticky=W, padx=5, pady=5)
        j += 1

    label1 = Label(records, text="ID", anchor=W, justify=LEFT, bg="skyblue").grid(row=0, column=0, sticky=W, padx=5, pady=5)
    label2 = Label(records, text="Customer Name", anchor=W, justify=LEFT, bg="skyblue").grid(row=0, column=1, sticky=W, padx=5, pady=5)
    label3 = Label(records, text="Product Name", anchor=W, justify=LEFT, bg="skyblue").grid(row=0, column=2, sticky=W, padx=5, pady=5)
    label4 = Label(records, text="Product Price", anchor=W, justify=LEFT, bg="skyblue").grid(row=0, column=3, sticky=W, padx=5, pady=5)
    conn.commit()
    conn.close()
    window.mainloop()


c_id = Entry(window, width=50)
c_id.grid(row=0, column=1, padx=20)
f_name = Entry(window, width=50)
f_name.grid(row=1, column=1)
l_name = Entry(window, width=50)
l_name.grid(row=2, column=1)
p_name = Entry(window, width=50)
p_name.grid(row=3, column=1)
p_price = Entry(window, width=50)
p_price.grid(row=4, column=1)
quantity = Entry(window, width=50)
quantity.grid(row=5, column=1)


button = Button(window, text="Save to Database", command=add).grid(row=6, column=1)

button2 = Button(window, text="Show Records", command=show_data).grid(row=7, column=1)

conn.commit()
conn.close()

window.mainloop()