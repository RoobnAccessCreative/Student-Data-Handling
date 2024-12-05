import pandas as pd
import matplotlib.pyplot as plt

def num(input):
    # validates menu inputs on if they are numeric values.
    # returns either True or False.
    # @param input - the user input for a menu
    return input.isnumeric()


def save_data(frame, filename='data.csv'):
    # Saves the data from the internal dataframe - df -
    # to the external csv file 'data.csv'.
    # @param frame - the internal dataframe
    # @param filename - the name of the external file 
    # the data is saved to. Default value is 'data.csv'.
    frame.to_csv(filename, index=False)
    print(f"{filename} updated")


def load_data(frame, filename='data.csv'):
    # loads the data from an external csv file as a Dataframe.
    # returns the loaded Dataframe, or an empty version if none was supplied.
    # @param frame - the internal dataframe
    # @param filename - the name of the external file 
    # the data is saved to. Default value is 'data.csv'.
    try:
        with open(filename, '+r') as f:
            frame = pd.read_csv(f)
            print(frame)
            return frame
    
    except FileNotFoundError:
        print("File not found. Starting with an empty dataset.")
        return pd.DateFrame(columns=["ID","Name","Grade"])


def add_student(frame):
    # adds a new student to the internal Dataframe.
    # validates for unique student IDs and valid grade values.
    # @param frame - the internal Dataframe.
    print("\n--ADD STUDENT--")
    try:
        s_id = int(input("Enter Student ID ->"))
        if s_id in df['ID']:
            print("Error - ID is taken.")
            return
        
        name = int(input("Enter Student's Name ->"))
        
        grade = float(input("Enter Student's Grade (0-100) ->"))
        if grade < 0 or grade > 100:
            print("Error - Grade value out of bounds.")
        else: 
            frame.loc[len(df)] = {'ID': s_id, 'Name': name, 'Grade': grade}
            print("Student has been added.")

    except TypeError:
        print("Error - ID should be an integer.")


def analyse(frame):
    # displays the maximum, minimum, and mean grade values from the Datarame.
    # gives an error if the Dataframe is empty.
    # @param frame - the internal Dataframe
    print("\n--ANALYSE DATA--")

    if frame.empty:
        print("No data available for plotting.")
        return
    
    print(
        f"\nHighest Grade = {frame['Grade'].max()} \nLowest Grade = {frame['Grade'].min()} \nAverage Grade = {frame['Grade'].mean():.2f}"
    )



def sort_students(frame, column="Grade"):
    # sorts the values of the Dataframe by one of its columns.
    # returns the sorted Dataframe, or the original if an unkown column was passed.
    # @param frame - the internal Dataframe
    # @param column - the column that the data will be sorted by: either 'ID', 'Name' or 'Grade'. Default is 'Grade'.
    if column in frame.columns:
        return frame.sort_values(by=column, ascending=True)
    else:
        print(f"Column '{column}' not found.")
        return frame


def plot_grades(frame):
    # plots the grade values of each student as a bar chart.
    # @param frame - the internal Dataframe.
    print("\n--PLOT GRADES--")

    if frame.empty:
        print("No data available for plotting.")
        return
    
    plt.bar(frame["Name"], frame["Grade"], color="skyblue")
    plt.title("Student Grades")
    plt.xlabel("Student Name")
    plt.ylabel("Grade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show(block=False)


def plot_dist(frame):
    # plots a pie chart of the amount of passing students against the number of failing ones.
    # @param frame - the internal Dataframe.
    print("\n--GRADE DISTRIBUTION--")

    if frame.empty:
        print("No data available for plotting.")
        return
    
    passed = (frame['Grade'] >= 50).sum()
    failed = (df['Grade'] < 50).sum()

    plt.pie(
        [passed, failed],
        labels=['Pass', 'Fail'],
        autopct="%1.1f%%",
        colors=['blue', 'purple']
    )
    plt.title('Student Pass vs Fail Rates')
    plt.show(block=False)

 


def plot_hist(frame):
    # plots the grade values of each student as a histogram.
    # @param frame - the internal Dataframe.
    print("\n--GRADE HISTOGRAM--")
    if frame.empty:
        print("No data available for plotting.")
        return

    plt.hist(frame["Grade"], bins=10, color="purple", edgecolor="black")
    plt.title("Grade Distribution Histogram")
    plt.xlabel("Grade Range")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show(block=False)


# -- Main program

df = pd.DataFrame(columns=['ID', 'Name', 'Grade'])

flag = True
while flag:

    # Main menu
    print("\n\t\t --- STUDENT MENU --- \n")
    print(
        "(1) Save/Load Student Data\n(2) Add Student\n(3) Analyse Data\n(4) Sort Students\n(5) Plot Grades"
    )
    print(
        "\n(6) Plot Grade Distribution\n(7) Plot Grade Histogram\n(8) Exit"
    )
    
    print("\n------------------------------------------\n")

    choice = input("Select a menu option ->").strip()


    # Choice validation
    if num(choice) == False:
        print("\nINVALID MENU OPTION -- please enter a number.")

    elif int(choice) < 1 or int(choice) > 8:
        print("\nINVALID MENU OPTION -- please enter a valid number.")

    # Each menu choice
    else:
        match choice:
            case '1':
                print("\n(1) Save Data\n(2) Load Data")
                sec_choice = input("\nSelect ->").strip()

                if num(sec_choice) == False:
                    print("\nINVALID MENU OPTION -- please enter a number.")
                elif int(sec_choice) < 1 or int(sec_choice) > 2:
                    print("\nINVALID MENU OPTION -- please enter a valid number.")

                elif sec_choice == '1':
                    save_data(df)

                else:
                    df = load_data(df)

            case '2':
                add_student(df)

            case '3':
                df = analyse(df)

            case '4':
                print("\n--SORT BY--")
                print("\n(1) ID\n(2) Name\n(3) Grade")
                sec_choice = input("\nSelect ->").strip()

                if num(sec_choice) == False:
                    print("\nINVALID MENU OPTION -- please enter a number.")
                elif int(sec_choice) < 1 or int(sec_choice) > 3:
                    print("\nINVALID MENU OPTION -- please enter a valid number.")
                else:
                    df = sort_students(df)    

            case '5':
                df = plot_grades(df)

            case '6':
                df = plot_dist(df)

            case '7':
                plot_hist(df)

            case '8':
                exit('\nGoodbye :)')
