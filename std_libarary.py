'''
My most used functions,
'''
import csv
import os
import Scripts.customization as Customization

def titlecase(string : str) -> str:
    '''
    A function designed to format a string in a tital format.
    Divisors (" ","-")
    '''
    letter = False
    string_list = list(string)
    for i,char in enumerate(string_list):
        # if letter == is an integer dont uppercase letters after
        if (ord('0') <= ord(char) <= ord('9')) and (letter is False):
            letter = True
        # if letter == is already uppercase dont uppercase letters after
        elif (ord('A') <= ord(char) <= ord('Z')) and (letter is False):
            letter = True
        # if letter == is lowercase and we are  dont uppercase letters after
        elif (ord('a') <= ord(char) <= ord('z')) and (letter is False):
            letter = True
            string_list[i] = char.upper()
        elif char == " ":
            if letter is False:
                string_list[i] = ''
            else:
                letter = False
        elif char == "-":
            letter = False
        else:
            continue
    string = "".join(string_list)

    return string

def read_csv(directory,header=False,column = False):
    '''
    This simply reads in a csv file and exports its result as a list\n
    header = False(Remove First Row) || True(Keep First Row)
    '''
    error = ''
    export_list = []
    try:
        import_list = []
        with open(directory, newline='',encoding = 'UTF-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for i,row in enumerate(spamreader):
                if (i>=1) and (header is False):
                    import_list.append(row)
                elif header is True:
                    import_list.append(row)
        if column is not False:
            for i,item_i in enumerate(import_list):
                export_list.append(item_i[column])
        else:
            export_list = import_list
    except FileNotFoundError:
        error = f'This file cannot be found {directory}'
    return export_list,error

def read_csv_as_dic(directory,header = False):
    '''
    Read a csv on as a dictionary
    '''
    data_list,error = read_csv(directory,header)
    dic = {}
    if error == "":
        try:
            for row in data_list:
                if len(row) > 2:
                    temp = row[1:len(row)]
                    dic[row[0].lower()] = temp
                else:
                    temp = [row[1]]
                    dic[row[0].lower()] = temp
        except KeyError:
            error = f'Error {directory}'

    return dic,error

def read_qlt(directory,header=False,column = False):
    '''
    This simply reads in a csv file and exports its result as a list\n
    header = False(Remove First Row) || True(Keep First Row)
    '''
    error = ''
    export_list = []
    try:
        import_list = []
        with open(directory, newline='',encoding = 'UTF-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
            for i,row in enumerate(spamreader):
                if (i>=1) and (header is False):
                    import_list.append(row)
                elif header is True:
                    import_list.append(row)
        if column is not False:
            for i,item_i in enumerate(import_list):
                temp = []
                for j,item_j in enumerate(column):#pylint: disable = W0612:unused-variable
                    temp.append(item_i[item_j])
                export_list.append(temp)
        else:
            export_list = import_list
    except FileNotFoundError:
        error = f'This file cannot be found {directory}'
    return export_list,error

def write_to_csv(file_name,file_row):
    '''
    This function will take a list of lists the primary list being the rows
    and the nested list being the columns
    '''
    with open(f'{file_name}.csv', 'w+', newline= "",encoding="UTF-8") as file:
    # using csv.writer method from CSV package
        write = csv.writer(file)
        for i,file in enumerate(file_row):
            write.writerow(file_row[i])
            Customization.progress_bar(i+1,len(file_row),"EXPORTED")

def write_to_qlt(file_name:str,file_row: tuple) -> None:
    '''
    This uses "	" as a deliminator instead of a ","
    '''
    with open(f'{file_name}.qlt', 'w+', newline= "", encoding= "UTF-8") as f:
    # using csv.writer method from CSV package
        write = csv.writer(f,delimiter = "\t")
        for i,rows in enumerate(file_row):#pylint: disable = W0612:unused-variable
            write.writerow(file_row[i])
            Customization.progress_bar(i+1,len(file_row),"EXPORTED")
        print()

def contains_number(s):
    '''detects if a string contains number'''
    return any(char.isdigit() for char in s)

def remove_strings_with_numbers(input_list):
    '''Generates a list of strings without a number'''
    return [item for item in input_list if not contains_number(item)]

def getdir_without_num(directory: str) -> list:
    '''Generates a list of directories unless they contain a number'''
    return remove_strings_with_numbers(os.listdir(directory))

def create_dir_if_not_existent(path: str) -> None:
    '''Generates a file unless it already exist's'''
    if not os.path.isdir(path):
        os.makedirs(path)
