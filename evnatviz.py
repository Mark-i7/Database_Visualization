import pandas as pd
import json
from collections import defaultdict
import operator
import matplotlib.pyplot as plt


def show():
    path2017='C:/Users/Mark/Desktop/Sapi2020-2021/2felev/Adatbazis2/Labor/labor5_vizualizacio/grades2017.json'
    path2016 = 'C:/Users/Mark/Desktop/Sapi2020-2021/2felev/Adatbazis2/Labor/labor5_vizualizacio/grades2016.json'
    path2015 = 'C:/Users/Mark/Desktop/Sapi2020-2021/2felev/Adatbazis2/Labor/labor5_vizualizacio/grades2015.json'
    path2019 = 'C:/Users/Mark/Desktop/Sapi2020-2021/2felev/Adatbazis2/Labor/labor5_vizualizacio/grades2019.json'
    schoolMingrade2019 = read(path2019)
    schoolMingrade2019.pop(7)

    schoolMingrade2017 = read(path2017)
    schoolMingrade2016 = read(path2016)
    schoolMingrade2015 = read(path2015)
    
    schoolMingrade2019 = sortGrade(schoolMingrade2019)
    schoolMingrade2017 = sortGrade(schoolMingrade2017)
    schoolMingrade2016 = sortGrade(schoolMingrade2016)
    schoolMingrade2015 = sortGrade(schoolMingrade2015)


    label1, yval1 = zip(*schoolMingrade2019)
    label2, yval2 = zip(*schoolMingrade2017)
    label3, yval3 = zip(*schoolMingrade2016)
    label4, yval4 = zip(*schoolMingrade2015)


    df = pd.DataFrame({'2019': yval1,
                       '2017': yval2,
                       '2016': yval3,
                       '2015': yval4 }, index=label1)
    colors = ['red', 'blue', 'green', 'yellow']

    ticks = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]

    df.plot.bar(rot=30, alpha=1, grid=True, yticks=ticks, color=colors,
                title='Marosvasarhely iskolainak a legkisebb atlag jegyei a kepessegi vizsgan')

    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    plt.show()



def read(path):
    with open(path) as grade:
        data= json.load(grade)
        grades = data['results']
        schoolMingrade = []

        for i in range(1, len(grades)):
            if grades[i]['location'] == "Marosvasarhely" or grades[i]['location'] == "Targu Mures":
                schoolMingrade.append(tuple((grades[i]['shortSchoolName'], float(grades[i]['avg']))))

        d = defaultdict(list)

        for loc, avg in schoolMingrade:
            d[loc].append(avg)
    schoolMingrade = list(zip(d, map(min, d.values())))
    schoolMingrade = sorted(schoolMingrade, key=operator.itemgetter(0))

    return schoolMingrade


def sortGrade(schoolMingrade):
    
    d = defaultdict(list)

    for loc, avg in schoolMingrade:
        d[loc].append(avg)
    schoolMingrade = list(zip(d, map(min, d.values())))
    schoolMingrade = sorted(schoolMingrade, key=operator.itemgetter(1))

    return schoolMingrade
    


