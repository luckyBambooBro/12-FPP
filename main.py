from load_school_data import load_school_data
import sys

def main():
    schools_data = load_school_data()
    if not schools_data:
        print("School data failed to load")
        sys.exit(1)
    print(schools_data)


if __name__ == "__main__":
    main()