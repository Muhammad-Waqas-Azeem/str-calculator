import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define basic and scientific functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def sin(x):
    return np.sin(np.radians(x))  # Input in degrees

def cos(x):
    return np.cos(np.radians(x))  # Input in degrees

def tan(x):
    return np.tan(np.radians(x))  # Input in degrees

def log(x, base):
    if x <= 0:
        return "Error! Logarithm undefined for zero or negative values."
    return np.log(x) / np.log(base)

# Streamlit app UI
st.title("Scientific Calculator with Graph Plotter")

# Selection for basic or scientific operations
mode = st.sidebar.selectbox("Select Mode", ("Basic Calculator", "Scientific Calculator", "Graph Plotter"))

if mode == "Basic Calculator":
    st.header("Basic Calculator")

    operation = st.selectbox("Select operation:", ("Add", "Subtract", "Multiply", "Divide"))
    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")

    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        
        st.write(f"The result is: {result}")

elif mode == "Scientific Calculator":
    st.header("Scientific Calculator")

    operation = st.selectbox("Select scientific operation:", ("Sine", "Cosine", "Tangent", "Logarithm"))
    num = st.number_input("Enter number", format="%f")
    
    if operation == "Logarithm":
        base = st.number_input("Enter logarithm base", value=10.0, format="%f")
        if st.button("Calculate"):
            result = log(num, base)
            st.write(f"The result is: {result}")
    else:
        if st.button("Calculate"):
            if operation == "Sine":
                result = sin(num)
            elif operation == "Cosine":
                result = cos(num)
            elif operation == "Tangent":
                result = tan(num)
            
            st.write(f"The result is: {result}")

elif mode == "Graph Plotter":
    st.header("Graph Plotter")
    
    function = st.text_input("Enter a function of x (e.g., sin(x), cos(x), x**2, log(x)):")
    x_min = st.number_input("Enter minimum x value", value=-10.0, format="%f")
    x_max = st.number_input("Enter maximum x value", value=10.0, format="%f")
    
    if st.button("Plot"):
        try:
            x = np.linspace(x_min, x_max, 1000)
            y = eval(function)  # Evaluates the input function
            plt.figure(figsize=(10, 6))
            plt.plot(x, y, label=f"y = {function}")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.legend()
            plt.grid(True)
            st.pyplot(plt)
        except Exception as e:
            st.write("Error in function! Please check the syntax.")
