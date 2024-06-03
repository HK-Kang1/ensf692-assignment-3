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

def main():
    """
    Main function for computing and printing school enrollment statistics.
    
    This function prompts the user to enter a high school name or school code,
    retrieves and displays various enrollment statistics for the specified school,
    and prints general statistics for all schools.
    """
    print("\nENSF 692 School Enrollment Statistics\n")
    # Print Stage 1 requirements here
    print("Shape of full data array:", data.shape)
    print("Dimensions of full data array:", data.ndim)

    # Prompt for user input 
    i = True
    while i:
        try:
            # Prompt the user to enter a high school name or code
            school_input = input("Please enter the high school name or school code: ")
            # If the input is a valid school name, get the corresponding school code.
            if school_input in school_map:
                school_code = school_map[school_input]
                school_name = school_input
                i = False

            # If the input is a valid school code, find the corresponding school name.
            elif school_input in school_map.values():
                school_code = school_input
                for name, code in list(school_map.items()):
                    if code == school_input:
                        school_name = name
                        i = False

            else:
                # If the input is invalid, raise a ValueError.
                raise ValueError("not a valid input")
                    
        except ValueError:
            print("\nYou must enter a valid school name or code.")

    # Get the index of the school in the data array.
    school_index = list(school_map.values()).index(school_code)
        

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    print("School Name:", school_name + ",", "School Code:", school_code)

    # Calculate and print mean enrollment across all years for each grade
    print("Mean enrollment for Grade 10:", int(np.nanmean(data[:, school_index, 0])))
    print("Mean enrollment for Grade 11:", int(np.nanmean(data[:, school_index, 1])))
    print("Mean enrollment for Grade 12:", int(np.nanmean(data[:, school_index, 2])))

    # Print highest and lowest enrollment for a single grade
    print("Highest enrollment for a single grade:", int(np.nanmax(data[:, school_index, :])))
    print("Lowest enrollment for a single grade:", int(np.nanmin(data[:, school_index, :])))

    # Print total enrollments for each year and over ten years
    year = 2013
    num_years, num_schools, num_grades = data.shape

    for i in range(num_years):
        print("Total enrollment for", year, ":", int(np.nansum(data[i, school_index, :])))
        year += 1
    
    print("Total ten year enrollment:", int(np.nansum(data[:, school_index, :])))
    print("Mean total enrollment over 10 years:", int(np.nansum(data[:, school_index, :]) / num_years))

    # Print median value for enrollments over 500, if any. If not, print that there is no enrollments over 500
    specific_data = data[:, school_index, :]
    if np.any(specific_data < 500): 
        print("No enrollments over 500.")
    else:
        print("For all enrollments over 500, the median value was:", int(np.nanmedian(specific_data[specific_data > 500])))

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    # Print general stats: mean enrollment of 2013 and 2022, total graduating class of 2022,
    # highest enrollment for a single grade, and the lowest enrollment for a single grade.
    print("Mean enrollment in 2013:", int(np.nanmean(data[0, :, :])))
    print("Mean enrollment in 2022:", int(np.nanmean(data[9, :, :])))
    print("Total graduating class of 2022:", int(np.nansum(data[9, :, 2])))
    print("Highest enrollment for a single grade:", int(np.nanmax(data[:, :, :])))
    print("Lowest enrollment for a single grade:", int(np.nanmin(data[:, :, :])), "\n")

if __name__ == '__main__':
    main()
