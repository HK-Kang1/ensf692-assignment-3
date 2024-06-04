# school_data.py
# Heemin Kang
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

# Reshaping the given high school enrollment data into a 3-dimensional array.
# First dimension represents the year, second dimension represents the school, and the third dimension represents the grade.
data = np.array([year_2013.reshape(20,3), year_2014.reshape(20,3), 
                year_2015.reshape(20,3), year_2016.reshape(20,3), 
                year_2017.reshape(20,3), year_2018.reshape(20,3), 
                year_2019.reshape(20,3), year_2020.reshape(20,3),
                year_2021.reshape(20,3), year_2022.reshape(20,3)])

# Creating a dictionary for school names and their codes
school_map = {'Centennial High School': '1224', 'Robert Thirsk School': '1679',
    'Louise Dean School': '9626', 'Queen Elizabeth High School': '9806',
    'Forest Lawn High School': '9813', 'Crescent Heights High School': '9815',
    'Western Canada High School': '9816', 'Central Memorial High School': '9823',
    'James Fowler High School': '9825', 'Ernest Manning High School': '9826',
    'William Aberhart High School': '9829', 'National Sport School': '9830',
    'Henry Wise Wood High School': '9836', 'Bowness High School': '9847',
    'Lord Beaverbrook High School': '9850', 'Jack James High School': '9856',
    'Sir Winston Churchill High School': '9857', 'Dr. E. P. Scarlett High School': '9858',
    'John G Diefenbaker High School': '9860', 'Lester B. Pearson High School': '9865'}

class SchoolStats:
    """
    A class to compute and print statistics for a specific school and general statistics for all schools.
    """
    # Initialize SchoolStats with given data and school map.
    def __init__(self, data, school_map):
        self.data = data
        self.school_map = school_map
        self.school_code = ''
        self.school_name = ''
        self.school_index = 0

    def get_name_code(self, school_input):
        """
        Given the school name or code, store the corresponding school, code and the index. If an invalid name or code is provided,
        a ValueError exception is used to prompt for re-entry without terminating the program.

        Args:
            school_input (str): School name or code input by the user
        """
        i = True
        while i:
            try:
                # If the input is a valid school name, get the corresponding school code.
                if school_input in school_map:
                    self.school_code = school_map[school_input]
                    self.school_name = school_input
                    i = False

                # If the input is a valid school code, find the corresponding school name.
                elif school_input in school_map.values():
                    self.school_code = school_input
                    for name, code in list(school_map.items()):
                        if code == school_input:
                            self.school_name = name
                            i = False

                else:
                    # If the input is invalid, raise a ValueError.
                    raise ValueError("not a valid input")
                        
            except ValueError:
                    print("\nYou must enter a valid school name or code.")
                    school_input = input("Please enter the high school name or school code: ")


        # Get the index of the school in the data array.
        self.school_index = list(school_map.values()).index(self.school_code)

    def school_stats(self):
        """
        Calculates and prints the statistics for the user specified school.
        """

        # Calculate and print mean enrollment across all years for each grade
        print("Mean enrollment for Grade 10:", int(np.nanmean(data[:, self.school_index, 0])))
        print("Mean enrollment for Grade 11:", int(np.nanmean(data[:, self.school_index, 1])))
        print("Mean enrollment for Grade 12:", int(np.nanmean(data[:, self.school_index, 2])))

        # Print highest and lowest enrollment for a single grade
        print("Highest enrollment for a single grade:", int(np.nanmax(data[:, self.school_index, :])))
        print("Lowest enrollment for a single grade:", int(np.nanmin(data[:, self.school_index, :])))

        # Print total enrollments for each year and over ten years
        year = 2013
        num_years = data.shape[0]

        for i in range(num_years):
            print("Total enrollment for", year, ":", int(np.nansum(data[i, self.school_index, :])))
            year += 1
        
        # Print the total tne year enrollment
        print("Total ten year enrollment:", int(np.nansum(data[:, self.school_index, :])))
        # Print the mean total enrollment over 10 years
        print("Mean total enrollment over 10 years:", int(np.nansum(data[:, self.school_index, :]) / num_years))

        # Print median value for enrollments over 500, if any. If not, print that there is no enrollments over 500
        specific_data = data[:, self.school_index, :]
        if np.any(specific_data > 500): 
            print("For all enrollments over 500, the median value was:", int(np.nanmedian(specific_data[specific_data > 500])))
        else:
            print("No enrollments over 500.")
            
    def general_stats(self):
        """
        Calculates and prints general statistics for all schools.
        """
        # Print mean enrollment of 2013
        print("Mean enrollment in 2013:", int(np.nanmean(data[0, :, :])))
        # Print mean enrollment of 2022
        print("Mean enrollment in 2022:", int(np.nanmean(data[9, :, :])))
        # Print total graduating class of 2022
        print("Total graduating class of 2022:", int(np.nansum(data[9, :, 2])))
        # Print highest enrollment for a single grade
        print("Highest enrollment for a single grade:", int(np.nanmax(data[:, :, :])))
        # Print lowest enrollment for a single grade
        print("Lowest enrollment for a single grade:", int(np.nanmin(data[:, :, :])), "\n")


def main():
    # main method to calculate and print school specific statistics and general statistics. 
    print("\nENSF 692 School Enrollment Statistics\n")
    # Create an instance of the class SchoolStats
    school_data = SchoolStats(data, school_map) 

    # Print Stage 1 requirements here
    print("Shape of full data array:", data.shape) # prints shape of data
    print("Dimensions of full data array:", data.ndim) #prints dimensions of data

    # Prompt for user input 
    school_input = input("Please enter the high school name or school code: ")
    school_data.get_name_code(school_input)

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    # Prints the methods in school_stats method
    print("School Name:", school_data.school_name + ",", "School Code:", school_data.school_code)
    school_data.school_stats()

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    # Prints the methods in general_stats method
    school_data.general_stats()

if __name__ == '__main__':
    main()
