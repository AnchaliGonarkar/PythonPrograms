import sys

def get_python_version():
    return sys.version

# Main program
if __name__ == "__main__":
    version = get_python_version()
    print(f"The Python version is: {version}")
