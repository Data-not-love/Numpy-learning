import csv

data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'London'],
    ['Bob', 35, 'Paris']
] #list

with open ('ex.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
data_2 = [
    ['Id','Brand','Car Name','Owner_id'],
    [1,'Lamborghini','Aventador',34],
    [2,'Ferrari','488 Pista',45],
    [4,'Pagani','Huayra',67]

]

with open ('ex2.csv','w', newline='') as file:
    writer_2 =csv.writer(file)
    writer_2.writerows(data_2)