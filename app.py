import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Python Learning App", page_icon="🐍", layout="wide")

st.title("🐍 Python Learning Roadmap - Made by Imtiaz")
st.markdown("Learn Python step by step with interactive mini-projects!")

menu = [
    "Basics", 
    "Control Flow", 
    "Functions", 
    "Data Structures", 
    "OOP", 
    "File Handling", 
    "Error Handling", 
    "Advanced (Decorators/Generators)", 
    "Popular Libraries", 
    "AI/ML Intro"
]

choice = st.sidebar.selectbox("📌 Select Topic", menu)

# ---------------- BASICS ----------------
if choice == "Basics":
    st.header("🔹 Basics: Print, Variables, Input")
    name = st.text_input("Enter your name:")
    if st.button("Say Hello"):
        st.success(f"Hello, {name}! Welcome to Python 🚀")

    st.code('''# Example
name = "Imtiaz"
print("Hello", name)''')

# ---------------- CONTROL FLOW ----------------
elif choice == "Control Flow":
    st.header("🔹 Control Flow: Number Guessing Game")
    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 10)

    guess = st.number_input("Guess a number (1-10)", 1, 10)
    if st.button("Check"):
        if guess == st.session_state.number:
            st.success("🎉 Correct! You guessed it.")
            st.session_state.number = random.randint(1, 10)  # reset
        elif guess < st.session_state.number:
            st.warning("Too low! Try again.")
        else:
            st.warning("Too high! Try again.")

    st.code('''# Example
import random
num = random.randint(1,10)
guess = int(input("Enter number: "))
if guess == num:
    print("Correct!")
''')

# ---------------- FUNCTIONS ----------------
elif choice == "Functions":
    st.header("🔹 Functions: Simple Calculator")
    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")
    op = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

    def calculator(x, y, operation):
        if operation == "Add": return x + y
        elif operation == "Subtract": return x - y
        elif operation == "Multiply": return x * y
        elif operation == "Divide": return x / y if y != 0 else "❌ Cannot divide by zero"

    if st.button("Calculate"):
        st.success(f"Result: {calculator(a, b, op)}")

# ---------------- DATA STRUCTURES ----------------
elif choice == "Data Structures":
    st.header("🔹 Data Structures: Student Records")

    if "students" not in st.session_state:
        st.session_state.students = {"Ali": 90, "Ayesha": 85, "Imtiaz": 95}

    st.write("Student Records:", st.session_state.students)

    new_name = st.text_input("Add new student name")
    new_score = st.number_input("Add score", 0, 100)
    if st.button("Add Student"):
        st.session_state.students[new_name] = new_score
        st.success(f"Added {new_name} with score {new_score}")
        st.write(st.session_state.students)

# ---------------- OOP ----------------
elif choice == "OOP":
    st.header("🔹 OOP: Library System")

    if "lib" not in st.session_state:
        class Book:
            def __init__(self, title, author):
                self.title = title
                self.author = author
                self.available = True

        class Library:
            def __init__(self):
                self.books = []

            def add_book(self, book):
                self.books.append(book)

        st.session_state.lib = Library()
        st.session_state.lib.add_book(Book("Python Basics", "Imtiaz"))
        st.session_state.lib.add_book(Book("AI with Python", "Imtiaz"))

    for book in st.session_state.lib.books:
        st.write(f"📘 {book.title} by {book.author}")

# ---------------- FILE HANDLING ----------------
elif choice == "File Handling":
    st.header("🔹 File Handling: Save & Read Notes")

    note = st.text_area("✍️ Write a note")
    if st.button("Save Note"):
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        st.success("✅ Note saved to notes.txt")

    if st.button("Read Notes"):
        try:
            with open("notes.txt", "r") as f:
                content = f.read()
            st.text_area("📖 Saved Notes", content, height=200)
        except FileNotFoundError:
            st.error("❌ No notes found. Save a note first!")

# ---------------- ERROR HANDLING ----------------
elif choice == "Error Handling":
    st.header("🔹 Error Handling: Divide Numbers Safely")

    x = st.number_input("Enter numerator", value=10)
    y = st.number_input("Enter denominator", value=0)

    if st.button("Divide"):
        try:
            result = x / y
            st.success(f"✅ Result: {result}")
        except ZeroDivisionError:
            st.error("❌ Cannot divide by zero!")
        except Exception as e:
            st.error(f"⚠️ Error occurred: {e}")

# ---------------- ADVANCED ----------------
elif choice == "Advanced (Decorators/Generators)":
    st.header("🔹 Advanced: Decorators & Generators")

    st.subheader("✨ Decorator Example")
    def decorator(func):
        def wrapper():
            return f"Before → {func()} → After"
        return wrapper

    @decorator
    def say_hello():
        return "Hello Imtiaz!"

    st.write(say_hello())

    st.subheader("🔄 Generator Example")
    def count_up_to(n):
        i = 1
        while i <= n:
            yield i
            i += 1

    n = st.slider("Generate numbers up to", 1, 10, 5)
    st.write(list(count_up_to(n)))

# ---------------- POPULAR LIBRARIES ----------------
elif choice == "Popular Libraries":
    st.header("🔹 Popular Libraries: Pandas & Matplotlib")

    data = {"Names": ["Ali", "Ayesha", "Imtiaz"], "Scores": [90, 85, 95]}
    df = pd.DataFrame(data)
    st.write(df)

    fig, ax = plt.subplots()
    ax.bar(df["Names"], df["Scores"])
    st.pyplot(fig)
    plt.close(fig)

# ---------------- AI/ML INTRO ----------------
elif choice == "AI/ML Intro":
    st.header("🔹 AI/ML Intro: Iris Flower Classifier 🌸")

    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression

    # Load dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Train model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    st.success(f"✅ Model trained with accuracy: {model.score(X_test, y_test):.2f}")

    # User input
    st.subheader("🔮 Predict Flower Type")
    sepal_length = st.slider("Sepal length", 4.0, 8.0, 5.0)
    sepal_width = st.slider("Sepal width", 2.0, 4.5, 3.0)
    petal_length = st.slider("Petal length", 1.0, 7.0, 4.0)
    petal_width = st.slider("Petal width", 0.1, 2.5, 1.0)

    if st.button("Predict"):
        input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(input_data)[0]
        flower = iris.target_names[prediction]
        st.success(f"🌼 Predicted Flower: **{flower}**")
