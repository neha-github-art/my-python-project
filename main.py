def hello_world():
    """A simple function that prints a greeting message."""
    print("Hello, World! Welcome to GitHub Copilot learning.")

def greet(name):
    """A function that greets a person by their name."""
    return f"Hello, {name}! Nice to meet you."

if __name__ == "__main__":
    # Call the hello_world function
    hello_world()
    
    # Call the greet function
    user_name = "Neha"
    message = greet(user_name)
    print(message)
    
    print("\nYou've successfully created your first Python project with GitHub!")
    # Create a new route that exposes the cities of a country:
@app.get('/countries/{country}')
def cities(country: str):
    return list(data[country].keys())
    
