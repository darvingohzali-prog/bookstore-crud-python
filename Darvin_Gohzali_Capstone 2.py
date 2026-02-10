from prettytable import PrettyTable

# ===================== DATA =====================
Book_Store = [
    # ===== SELF IMPROVEMENT (100s) =====
    [101, "How to Win Friends and Influence People", 150000, 10, "Non Fiction", "Self Improvement", "Non Series"],
    [102, "Atomic Habits", 145000, 8, "Non Fiction", "Self Improvement", "Non Series"],
    [103, "The 7 Habits of Highly Effective People", 155000, 7, "Non Fiction", "Self Improvement", "Non Series"],
    [104, "Think and Grow Rich", 135000, 6, "Non Fiction", "Self Improvement", "Non Series"],
    [105, "Rich Dad Poor Dad", 140000, 9, "Non Fiction", "Self Improvement", "Non Series"],
    
    # ===== NOVEL (200s) =====
    [201, "Laskar Pelangi", 80000, 12, "Fiction", "Novel", "Non Series"],
    [202, "Bumi Manusia", 95000, 9, "Fiction", "Novel", "Non Series"],
    [203, "Perahu Kertas", 85000, 10, "Fiction", "Novel", "Non Series"],
    [204, "Dilan 1990", 90000, 8, "Fiction", "Novel", "Series"],
    [205, "Dilan 1991", 92000, 7, "Fiction", "Novel", "Series"],
   

    # ===== COMIC (300s) =====
    [301, "Naruto", 40000, 13, "Fiction", "Comic", "Series"],
    [302, "One Piece", 45000, 20, "Fiction", "Comic", "Series"],
    [303, "Dragon Ball", 42000, 15, "Fiction", "Comic", "Series"],
    [304, "My Hero Academia", 45000, 14, "Fiction", "Comic", "Series"],
    [305, "Fairy Tail", 43000, 12, "Fiction", "Comic", "Series"],
   
    # ===== KNOWLEDGE (400s) =====
    
    [401, "Dasar-dasar Python", 140000, 10, "Non Fiction", "Knowledge", "Non Series"],
    [402, "Pengantar Ilmu Ekonomi", 120000, 8, "Non Fiction", "Knowledge", "Non Series"],
    [403, "Economics in One Lesson", 135000, 7, "Non Fiction", "Knowledge", "Non Series"],
    [404, "Principles of Microeconomics", 160000, 6, "Non Fiction", "Knowledge", "Non Series"],
    [405, "Basic Accounting", 125000, 9, "Non Fiction", "Knowledge", "Non Series"],
    
]

# ===================== THEME CODE =====================
Theme_CODE = {
    "Self Improvement": 100,
    "Novel": 200,
    "Comic": 300,
    "Knowledge": 400
}
# ===================== Unique Title =====================
def generate_unique_title(title):
    existing_titles = [book[1] for book in Book_Store]

    if title not in existing_titles:
        return title

    count = 1
    new_title = f"{title} {count}"
    while new_title in existing_titles:
        count += 1
        new_title = f"{title} {count}"

    return new_title

# ===================== HELPER =====================
def generate_id(theme, exclude_id=None):
    base = Theme_CODE.get(theme, 900)

    used_ids = sorted(
        book[0]
        for book in Book_Store
        if book[5] == theme and book[0] != exclude_id
    )

    # No books yet in this theme
    if not used_ids:
        return base + 1

    expected = base + 1
    for uid in used_ids:
        if uid != expected:
            return expected
        expected += 1

    return expected

def show_books(data):
    table = PrettyTable()
    table.field_names = ['ID', 'Title', 'Price', 'Stock', 'Type', 'Theme', 'Series']
    for book in data:
        table.add_row(book)
    print(table)


def find_book_by_id(book_id):
    for book in Book_Store:
        if book[0] == book_id:
            return book
    return None

def choose_type_theme_series():
    # ===== TYPE =====
    while True:
        print("""
Book Type:
1. Fiction
2. Non Fiction
3. Custom
""")
        Type_choice = input("Choose: ")
        if Type_choice == '1':
            Type = "Fiction"
            break
        elif Type_choice == '2':
            Type = "Non Fiction"
            break
        elif Type_choice == '3':
            Type = input("Custom Type: ")
            break
        else:
            print("❌ Invalid input")

    # ===== THEME =====
    while True:
        if Type == "Fiction":
            print("1.Comic 2.Novel 3.Custom")
            Theme_choice = input("Choose: ")
            if Theme_choice == '1':
                Theme = "Comic"
                break
            elif Theme_choice == '2':
                Theme = "Novel"
                break
            elif Theme_choice == '3':
                Theme = input("Custom Theme: ")
                break
            else:
                print("❌ Invalid input")

        elif Type == "Non Fiction":
            print("1.Self Improvement 2.Knowledge")
            Theme_choice = input("Choose: ")
            if Theme_choice == '1':
                Theme = "Self Improvement"
                break
            elif Theme_choice == '2':
                Theme = "Knowledge"
                break
            else:
                print("❌ Invalid input")

        else:  # Custom Type
            print("1.Comic 2.Novel 3.Self Improvement 4.Knowledge 5.Custom")
            Theme_choice = input("Choose: ")
            if Theme_choice == '1':
                Theme = "Comic"
                break
            elif Theme_choice == '2':
                Theme = "Novel"
                break
            elif Theme_choice == '3':
                Theme = "Self Improvement"
                break
            elif Theme_choice == '4':
                Theme = "Knowledge"
                break
            elif Theme_choice == '5':
                Theme = input("Custom Theme: ")
                break
            else:
                print("❌ Invalid input")

    # ===== SERIES =====
    while True:
        print("1.Series 2.Non Series 3.Custom")
        Series_choice = input("Choose: ")
        if Series_choice == '1':
            Series = "Series"
            break
        elif Series_choice == '2':
            Series = "Non Series"
            break
        elif Series_choice == '3':
            Series = input("Custom Series: ")
            break
        else:
            print("❌ Invalid input")

    return Type, Theme, Series

# ===================== READ MENU =====================
def Read_Menu():
    print("""
1. Show All Books
2. Show Partial (Filter)
""")
    choice = input("Choose: ")

    if choice == '1':
        show_books(Book_Store)

    elif choice == '2':
        print("""
1. Fiction
2. Non Fiction
""")
        book_type = input("Choose Type: ")

        if book_type == '1':
            fiction_books = [b for b in Book_Store if b[4] == 'Fiction']

            print("""
1. Comic
2. Novel
""")
            sub_type = input("Choose Category: ")

            if sub_type == '1':
                show_books([b for b in fiction_books if b[5] == 'Comic'])
            elif sub_type == '2':
                show_books([b for b in fiction_books if b[5] == 'Novel'])
            else:
                print("Invalid choice ❌")

        elif book_type == '2':
            non_fiction_books = [b for b in Book_Store if b[4] == 'Non Fiction']

            print("""
1. Self Improvement
2. Knowledge
""")
            sub_type = input("Choose Category: ")

            if sub_type == '1':
                show_books([b for b in non_fiction_books if b[5] == 'Self Improvement'])
            elif sub_type == '2':
                show_books([b for b in non_fiction_books if b[5] == 'Knowledge'])
            else:
                print("Invalid choice ❌")


        else:
            print("Invalid choice ❌")

    else:
        print("Invalid choice ❌")

# ===================== CREATE =====================
def Create_Data():
    while True:
        try:
            raw_title = input("Title: ")
            Title = generate_unique_title(raw_title)
            Price = int(input("Price: "))
            Stock = int(input("Stock: "))

            Type, Theme, Series = choose_type_theme_series()

            ID_Book = generate_id(Theme)
            Book_Store.append([ID_Book, Title, Price, Stock, Type, Theme, Series])

            print(f"✅ Book added with ID {ID_Book}")
            break

        except ValueError:
            print("❌ Price & Stock must be numbers")
# ===================== UPDATE =====================
def Update_Data():
    try:
        book_id = int(input("Input Book ID: "))
        book = find_book_by_id(book_id)

        if not book:
            print("Book not found ❌")
            return

        print("""
1. Update All
2. Update Partial
""")
        choice = input("Choose: ")

        # ===== UPDATE ALL =====
        if choice == '1':
            book[1] = generate_unique_title(input("New Title: "))
            book[2] = int(input("New Price: "))
            book[3] = int(input("New Stock: "))

            Type, Theme, Series = choose_type_theme_series()
            old_theme = book[5]

            book[4] = Type
            book[5] = Theme
            book[6] = Series

            if Theme != old_theme:
                book[0] = generate_id(Theme, exclude_id=book[0])

            print("✅ Update All success ✏️")

        # ===== UPDATE PARTIAL =====
        elif choice == '2':
            print("""
1. Title
2. Price
3. Stock
4. Type / Theme / Series
""")
            field = input("Choose field: ")

            if field == '1':
                book[1] = generate_unique_title(input("New Title: "))

            elif field == '2':
                book[2] = int(input("New Price: "))

            elif field == '3':
                book[3] = int(input("New Stock: "))

            elif field == '4':
                Type, Theme, Series = choose_type_theme_series()
                old_theme = book[5]

                book[4] = Type
                book[5] = Theme
                book[6] = Series

                if Theme != old_theme:
                    book[0] = generate_id(Theme, exclude_id=book[0])

                print("✅ Type / Theme / Series updated")

            else:
                print("❌ Invalid field")

        else:
            print("❌ Invalid menu")

    except ValueError:
        print("❌ Invalid number input")

# ===================== DELETE =====================
def Delete_Data():
    try:
        book_id = int(input("Input Book ID: "))
        book = find_book_by_id(book_id)

        if not book:
            print("Book not found ❌")
            return

        confirm = input("Are you sure? (y/n): ")
        if confirm.lower() != 'y':
            print("Cancelled")
            return

        print("1. Delete All")
        print("2. Delete Partial Stock")
        choice = input("Choose: ")

        if choice == '1':
            Book_Store.remove(book)
            print("Book deleted 🗑️")
        elif choice == '2':
            qty = int(input("Quantity to remove: "))
            if qty >= book[3]:
                Book_Store.remove(book)
                print("Book deleted 🗑️")
            else:
                book[3] -= qty
                print("Stock updated")

    except ValueError:
        print("Invalid input ❌")

# ===================== BUY BOOK =====================
def Buy_Book():
    try:
        show_books(Book_Store)

        book_id = int(input("Input Book ID to buy: "))
        book = find_book_by_id(book_id)

        if not book:
            print("Book not found ❌")
            return

        qty = int(input("Quantity to buy: "))

        if qty <= 0:
            print("Invalid quantity ❌")
            return

        if qty <= book[3]:
            total = qty * book[2]
            book[3] -= qty
            print(f"Total price: Rp {total}")
            print("Thank you for your purchase 🛒")
        else:
            print("Stock not enough ❌")

    except ValueError:
        print("Invalid input ❌")

# ===================== MAIN MENU =====================
while True:
    print("""
=== BOOK STORE MENU ===
1. List Book 
2. Add Book
3. Update Book
4. Delete Book
5. Buy Book
6. Exit
""")

    menu = input("Choose: ")

    if menu == '1':
        Read_Menu()
    elif menu == '2':
        show_books(Book_Store)
        Create_Data()    
        show_books(Book_Store)
    elif menu == '3':
        show_books(Book_Store)
        Update_Data()
        show_books(Book_Store)
    elif menu == '4':
        show_books(Book_Store)
        Delete_Data()
        show_books(Book_Store)
    elif menu == '5':
        Buy_Book()
        show_books(Book_Store)
    elif menu == '6':
        print("Thank you 👋")
        break

    else:
        print("Invalid menu ❌")
