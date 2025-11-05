class DataAnalysis:
    def load_dataset(self):
        file_path = input("Enter the path to the CSV file: ")
        try:
            self.df = pd.read_csv(file_path)
            print("Dataset loaded successfully.")
        except Exception as e:
            print(f"Error loading dataset: {e}")

    def explore_data(self):
        print("\n=====Explore Data=====\n")
        print("1. Display the First 5 rows of the dataset:")
        print("2. Display the Last 5 rows of the dataset:")
        print("3. Display the Column Names:")
        print("4. Display the Data Types of each column:")
        print("5. Display Basic Information about the dataset:\n")
        choice = int(input("Enter your choice (1-5): "))
        print()

        if choice == 1:
            print(self.df.head())
        elif choice == 2:
            print(self.df.tail())
        elif choice == 3:
            print(self.df.columns)
        elif choice == 4:
            print(self.df.dtypes)
        elif choice == 5:
            print(self.df.info())
        else:
            print("Invalid choice. Please try again.")

    def perform_dataframe_operations(self):
        print("\n=====Dataframe Operations=====\n")
        print("1. Select a specific column:")
        print("2. Filter rows based on a condition:")
        print("3. Sort the dataset by a specific column:")
        print("4. Add a new column:")
        print("5. Remove a column:\n")
        choice = int(input("Enter your choice (1-5): "))
        print()
        if choice == 1:
            column = input("Enter the column name: ")
            print(self.df[column])
        elif choice == 2:
           condition = input("Enter the condition (e.g., column > 50): ")
           print(self.df.query(condition))

        elif choice == 3:
            column = input("Enter the column name to sort by: ")
            ascending = input("Sort in ascending order? (yes/no): ").lower() == 'yes'
            print(self.df.sort_values(by=column, ascending=ascending))
        elif choice == 4:
            new_column = input("Enter the new column name: ")
            values = input("Enter the values for the new column (comma-separated): ").split(',')
            self.df[new_column] = values
            print(f"Column '{new_column}' added successfully.")
        elif choice == 5:
            column = input("Enter the column name to remove: ")
            self.df.drop(columns=[column], inplace=True)
            print(f"Column '{column}' removed successfully.")
        else:
            print("Invalid choice. Please try again.")

    def handle_missing_data(self):
        print("\n=====Handle Missing Data=====\n")
        print("1. Display rows with missing values:")
        print("2. Fill missing values with mean:")
        print("3. Drops rows with missing values:")
        print("4. Replace missing values with a specific value:\n")
        choice = int(input("Enter your choice (1-4): "))
        print()
        if choice == 1:
            print(self.df[self.df.isnull().any(axis=1)])
        elif choice == 2:
            self.df.fillna(self.df.mean(numeric_only=True), inplace=True)
            print("Missing values filled with mean.")
        elif choice == 3:
            self.df.dropna(inplace=True)
            print("Rows with missing values dropped.")
        elif choice == 4:
            value = input("Enter the value to replace missing values with: ")
            self.df.fillna(value, inplace=True)
            print(f"Missing values replaced with '{value}'.")
        else:
            print("Invalid choice. Please try again.")

    def generate_descriptive_statistics(self):
        print("\n=====Descriptive Statistics=====\n")
        print("1. Summary Statistics:")
        print("2. Mean of each column:")
        print("3. Median of each column:")
        print("4. Standard Deviation of each column:")
        choice = int(input("Enter your choice (1-4): "))
        print()
        if choice == 1:
            print(self.df.describe())
        elif choice == 2:
            print(self.df.mean())
        elif choice == 3:
            print(self.df.median())
        elif choice == 4:
            print(self.df.std())
        else:
            print("Invalid choice. Please try again.")
    
    def data_visualization(self):
        print("\n=====Data Visualization=====\n")
        print("1. Bar Plot:")
        print("2. Line Plot:")
        print("3. Scatter Plot:")
        print("4. Pie Chart:")
        print("5. Histogram:")
        print("6. Stack Plot:\n")
        choice = int(input("Enter your choice (1-6): "))
        print()
        if choice == 1:
            x = input("Enter the column name for x-axis: ")
            y = input("Enter the column name for y-axis: ")
            self.df.plot(kind='bar', x=x, y=y)
            plt.show()
        elif choice == 2:
            x = input("Enter the column name for x-axis: ")
            y = input("Enter the column name for y-axis: ")
            self.df.plot(kind='line', x=x, y=y)
            plt.show()
        elif choice == 3:
            x = input("Enter the column name for x-axis: ")
            y = input("Enter the column name for y-axis: ")
            self.df.plot(kind='scatter', x=x, y=y)
            plt.show()
        elif choice == 4:
            column = input("Enter the column name for pie chart: ")
            self.df[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
            plt.show()
        elif choice == 5:
            column = input("Enter the column name for histogram: ")
            self.df[column].plot(kind='hist', bins=10)
            plt.show()
        elif choice == 6:
            x = input("Enter the column name for x-axis: ")
            y_columns = input("Enter the column names for y-axis (comma-separated): ").split(',')
            self.df.plot(kind='area', x=x, y=y_columns, stacked=True)
            plt.show()

    def save_visualizations(self):
        print("\n=====Save Visualizations=====\n")
        save_img = input("Enter file name to save the plot (e.g., plot.png): ")
        plt.savefig(save_img)
        print(f"Visualization saved as {save_img} successfully!")


analysis = DataAnalysis()

while True:
    print("\n===== Data Analysis & Visualization Program =====")
    print("\nPlease select an option:\n")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualizations")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        analysis.load_dataset()
    elif choice == '2':
        analysis.explore_data()
    elif choice == '3':
        analysis.perform_dataframe_operations()
    elif choice == '4':
        analysis.handle_missing_data()
    elif choice == '5':
        analysis.generate_descriptive_statistics()
    elif choice == '6':
        analysis.data_visualization()
    elif choice == '7':
        analysis.save_visualizations()
    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")