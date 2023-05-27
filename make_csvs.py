"""
Converts 'UCSB Grades.csv' into individual CSV files under /csv

Assumptions:
- 'UCSB Grades.csv' is in the same directory as this script
- 'UCSB Grades.csv' has a header line
- 'UCSB Grades.csv' is sorted by quarter, level, course, instructor, grade

Directory structure is:
csv/
    - [year]_[quarter]/
        - [major]_[course_number]/
            - [instructor].csv

"""

import os

def getHeaders(filename):
  with open(filename) as infile:
    return infile.readline()
  
def writeHeaders(headers,filename):
  with open(filename, 'w') as outfile:
    outfile.write(headers)

def getQuarters(filename):
    quarters = []

    lineNum = 0
    with open(filename) as infile:
        for line in infile:
            lineNum += 1
            if lineNum == 1:
                header = line
            else:
                parts = line.split(",")
                qyy = parts[0]

                if qyy not in quarters:
                    quarters.append(qyy)
    return quarters


def getSubjectArea(course):
    return course[0:8].strip()


def getSubjectAreas(filename):
    subjectAreas = []

    lineNum = 0
    with open(filename) as infile:
        for line in infile:
            parts = line.split(",")
            course = parts[2]
            subjectArea = getSubjectArea(course)
            if subjectArea not in subjectAreas:
                subjectAreas.append(subjectArea)
    return subjectAreas


if __name__ == "__main__":
    filename = "UCSB Grades.csv"
    headers = getHeaders(filename)
    quarters = getQuarters(filename)
    print("quarters=", quarters)
    os.makedirs("tmp",exist_ok=True)
    for qyy in quarters:
        dirname = "quarters/" + qyy
        os.makedirs(dirname, exist_ok=True)
        tempFilename = "tmp/" + qyy + ".csv"
        command = "grep \"" + qyy + ",\" " + filename.replace(" ","\ ") + " > \"" + tempFilename + "\""
        print("Outer command=", command)
        os.system(command)
        subjectAreas = getSubjectAreas(tempFilename)
        print("subjectAreas=",subjectAreas)
        for subjectArea in subjectAreas:
            newFileName = f'{dirname}/{subjectArea}.csv'
            writeHeaders(headers,newFileName);
            command="grep \"," + subjectArea + "\" \"" + tempFilename + "\" >> \"" + newFileName + "\""
            print("Inner command=",command)
            os.system(command)

        # parts=line.split(",")

        # level=parts[1]
        # course=parts[2]
        # instructor=parts[3]
        # grade=parts[4]
        # count=parts[5]
        # subject = subjectArea(course)
        # courseNum = courseNumber(course)
        # quarter=letter2Quarter[qyy[0]]
        # year=qyy2Year(qyy)

        # yearQuarterDirectory=qyy2yearQuarterDirectory(qyy)
        # majorCourseDirectory=course2MajorCourseDirectory(course)
        # filename=instructor2Filename(instructor)

        # if previousYearQuarterDirectory!=yearQuarterDirectory:
        #     print("Creating directory:", yearQuarterDirectory)
        #     os.makedirs(yearQuarterDirectory, exist_ok=True)
        #     previousYearQuarterDirectory=yearQuarterDirectory

        # dirToCreate=yearQuarterDirectory + "/" + majorCourseDirectory
        # if previousDirToCreate!=dirToCreate:
        #     print("Creating directory:", dirToCreate)
        #     os.makedirs(dirToCreate, exist_ok=True)
        #     previousDirToCreate=dirToCreate

        # filenameToCreate = dirToCreate + "/" + filename
        # if previousFilenameToCreate!=filenameToCreate:
        #     print("Creating file:", filenameToCreate)
        #     with open(filenameToCreate, "w") as outfile:
        #       pass
        #     previousFilenameToCreate=filenameToCreate

        # with open(filenameToCreate, "a") as outfile:
        #     outfile.write(year + "," + quarter.capitalize() + "," + level + "," + subject + "," + courseNum.strip() + "," + instructor.replace(" ", "_") + "," + grade + "," + str(count))
