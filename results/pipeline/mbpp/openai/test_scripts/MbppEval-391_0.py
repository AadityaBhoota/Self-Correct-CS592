def convert_list_dictionary(l1, l2, l3):
    result = []  # Step 1

    for i in range(len(l1)):  # Step 2
        nested_dict = {l1[i]: {l2[i]: l3[i]}}  # Step 3
        result.append(nested_dict)

    return result  # Step 4

def check(candidate):
    assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
    assert convert_list_dictionary(["abc","def","ghi","jkl"],["python","program","language","programs"],[100,200,300,400])==[{'abc':{'python':100}},{'def':{'program':200}},{'ghi':{'language':300}},{'jkl':{'programs':400}}]
    assert convert_list_dictionary(["A1","A2","A3","A4"],["java","C","C++","DBMS"],[10,20,30,40])==[{'A1':{'java':10}},{'A2':{'C':20}},{'A3':{'C++':30}},{'A4':{'DBMS':40}}]

check(convert_list_dictionary)