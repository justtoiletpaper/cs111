# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


# define your functions here
dataset1 = []
dataset2 = []
student_list = []
score_list = []
outlier_list = []

def convert_row_type(row):
    row_converted = []
    for i in range(len(row)):
        conversion = float(row[i])
        row_converted.append(conversion)
    return row_converted


# def calculate_score(list):
#     output_file = open("student_scores.csv", "w")
#     for i in range(len(list)):
#         sum = ((list[i][0] / 160) * 0.3) + ((list[i][1] * 2) * 0.4) + (list[i][2] * 0.1) + (list[i][3] * 0.2)
#         score_list.append(round(sum, 2))
#         output_file.writelines(f"{student_list[i]},{sum:.2f}\n")
#     output_file.close()

def calculate_score(list):
    sum = ((list[0] / 160) * 0.3) + ((list[1] * 2) * 0.4) + (list[2] * 0.1) + (list[3] * 0.2)
    score_list.append(round(sum, 2))
    return sum


# def calculate_score_improved(student_index):
#     if score_list[student_index] >= 6.0 or is_outlier(dataset1[student_index]) == True:
#         return True
#     else:
#         return False

def calculate_score_improved(data):
    if calculate_score(data) >= 6.0 or is_outlier(data) == True:
        return True
    else:
        return False


def is_outlier(data):       # Finds outliers - interest score of 0 or bad SAT score with good GPA
    # for i in range(len(data)):
        sat = data[0] / 160  # Normalized SAT Score
        gpa = data[1] * 2    # Normalized GPA Score
        if data[2] == 0:
            return True
        elif gpa > sat + 2:     # If normalized GPA is more than 2 points higher than normalized SAT
            return True
        else:
            return False


def grade_outlier(grades):   # Takes student's semester grades and decides if theirs is an outlier
    sorted_grades = sorted(grades)
    if sorted_grades[0] < sorted_grades[1] - 20:
        return True
    else:
        return False

def grade_improvement(grades):
    if grades[0] <= grades[1] <= grades[2] <= grades[3]:
        return True
    else:
        return False


def main():
    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")    
    
    
    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()



    # TODO: loop through the rest of the file


    for line in input_file:     # Creates 2 datasets of float values
        current_row = line
        current_row = current_row[:-1]
        current_row = current_row.split(",")
        student_list.append(current_row[0])
        current_row = current_row[1:]
        converted_row = convert_row_type(current_row)
        dataset1.append(converted_row[0:4])
        dataset2.append(converted_row[4:8])

    output_file = open("student_scores.csv", "w")
    for i in range(len(dataset1)):
        score = calculate_score(dataset1[i])     # Writes each score to another file, while creating
    # two corresponding lists where the index matches the student to their score
        output_file.writelines(f"{student_list[i]},{score:.2f}\n")
    output_file.close()


    output_file = open("chosen_students.csv", "w")
    for i in range(len(student_list)):  # Create a list of 'chosen students' based on their calculated score
        if score_list[i] >= 6.0:
            output_file.writelines(student_list[i] + "\n")
    output_file.close()

    output_file = open("outliers.csv", "w")
    for i in range(len(student_list)):          # Creates list of outliers
        if is_outlier(dataset1[i]) == True:     # Checks the student's data to determine if they are an outlier
            output_file.writelines(student_list[i] + "\n")
    output_file.close()

    output_file = open("chosen_improved.csv", "w")
    for i in range(len(student_list)):          # Combines list of chosen and outlier students
        if score_list[i] >= 6.0:
            output_file.writelines(student_list[i] + "\n")
        elif is_outlier(dataset1[i]) == True and score_list[i] >= 5.0:
            output_file.writelines(student_list[i] + "\n")
    output_file.close()

    # output_file = open("better_improved.csv", "w")
    # for i in range(len(student_list)):
    #     if calculate_score_improved(i) == True:
    #         output_file.writelines(student_list[i] + "," + str(dataset1[i][0]) + "," + str(dataset1[i][1]) + "," +
    #                                str(dataset1[i][2]) + "," + str(dataset1[i][3]) + "\n")
    # output_file.close()

    output_file = open("better_improved.csv", "w")
    for i in range(len(student_list)):
        if calculate_score_improved(dataset1[i]) == True:
            output_file.writelines(student_list[i] + "," + str(dataset1[i][0]) + "," + str(dataset1[i][1]) + "," +
                                   str(dataset1[i][2]) + "," + str(dataset1[i][3]) + "\n")
    output_file.close()

    output_file = open("composite_chosen.csv", "w")
    for i in range(len(student_list)):
        if score_list[i] >= 6.0:
            output_file.writelines(student_list[i] + "\n")
        elif score_list[i] >= 5.0 and is_outlier(dataset1[i]) == True:
            output_file.writelines(student_list[i] + "\n")
        elif score_list[i] >= 5.0 and grade_outlier(dataset2[i]) == True:
            output_file.writelines(student_list[i] + "\n")
        elif score_list[i] >= 5.0 and grade_improvement(dataset2[i]) == True:
            output_file.writelines(student_list[i] + "\n")
    output_file.close()



    # TODO: make sure to close all files you've opened!
    input_file.close()
    print("done!")

# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
