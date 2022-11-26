from pathlib import Path

if __name__ == '__main__':
    try:
        exec(Path("task4" + ".py").read_text())
    except FileNotFoundError as e:
        print("File doesn't exist, try again")
