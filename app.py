
from flask import Flask, render_template
import datetime

app = Flask(__name__)
site_title = "Python and Flask"
year = datetime.datetime.now().strftime("%Y")

pythons_list = [
    {   
        "answer": "Python is a programming language used for building object oriented interactive interfaces that need a programmable interface. It is used to build everything from applications to robots.",
        "question": "What is Python and what is it used for?"
    },
    { 
        "answer": "A class is used by creating a class statement which is a particular object type. An Object is a collection of methods and data. An class is a blueprint for that object.",
        "question": "What is a class and what is an object in Python?"
    },
    {
        "answer": "@property is used in python to create getters and setters in object oriented programming. Attributes are used to create access controls to classes.",
        "question": "What are properties/attributes in Python and in what way(s) do they differ from variables?"
    },
    { 
        "answer": "When invoked functions stored in class dictionaries get turned into methods. Methods only differ from regular functions in that the object instance is prepended to the other arguments. By convention, the instance is called self but could be called this or any other variable name.",
        "question": "What are methods in Python and in what way(s) do they differ from functions?"
    },
    {
        "answer": "There are many types of magic methods. They automatically perform special actions. They are name with two underscores before and after the function. Descriptors are used to bind functions to methods. The constructor method is a method called __init__() in Python which is called when a new instance of the class is created by using the class name as a function. ",
        "question": "What are magic methods, what is the constructor method specifically, and how do they differ from normal methods?"
    },
    {
        "answer": "Private class variable names are class variable names which are only accessible from inside of the class they are defined in and its methods and which can therefore only be altered using the methods inside of that class. Private name mangling is used to keep the code object-oriented by keeping the data encapsulated inside of the object and to keep the processing of that data abstracted from the user.",
        "question": "What is private name mangling and why is it used?"
    },
    {
        "answer": "The 4 priniples of object-oriented programming are Encapsulation; the inclusion of one thing within another thing so that the included thing is not apparent, Abstraction; is used for efficiency purposes when the developer hides certain part to make it less complex, Inheritance; when sublcasses inherit definitions of one or more classes and Polymorphism; when objects can do different things depending on the context without changing the core interface.",
        "question": "Identify and define the four principles of object-oriented programming and explain in what way(s), each is used in Python."
    },
    {
        "answer": "PIP stands for PIP Installs Packages. It is used for installing thrid party libraries and packages for Python. ",
        "question": "What is PIP, what is a wheel and what are they used for?"
    },
    {
        "answer": "Flask is a framework for creating applications in python. Flask is used to provide a router and server and connect a thirty party HTML templating engine Jinja",
        "question": "What is Flask, what is Jinja and what are they used for?"
    },
    {
        "answer": "SQL is a programming language used to manage relational databases. MySQL and MariaDB are relational database systems where you can create, update and administer a relational database. MySQL Connector is a library to connect and manage MySQL or MariaDB in python.",
        "question": "What is SQL/ MySQL/MariaDB, what is MySQL Connector and what are they used for?"
    },
]

@app.route("/")
def index():
    return render_template(
        "index.html.j2",
        site_title = site_title,
        page_title = site_title + " - Home",
        year = year,
        pythons_list = pythons_list
    )

if __name__ == "__main__":
    app.run(debug = True)