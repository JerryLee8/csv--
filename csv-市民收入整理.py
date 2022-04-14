"""
範例程式: 0412HW
撰寫時間: 0412
作者: jerry
功能: HW
"""

import csv # csv 的檔案函式庫
import matplotlib.pyplot as plt

# 取得特定的筆數資料
def CSVGetRow(fileName,row1):
    with open(fileName, 'r') as fin:
        i = 0
        fileName = csv.reader(fin, delimiter=',')  # 用都號區分資料
        for row in fileName:
            if i == row1:
                #print(row)  # 印出這一筆的資料
                return row
            i = i + 1

 # 取得特定的欄數資料
def CSVGetCol(fileName,col1,header=0,changeTOFloat= "no"):
    list1 = []
    with open(fileName, 'r') as fin:
        i = 0
        dataCSV = csv.reader(fin, delimiter=',')  # 用都號區分資料
        for row in dataCSV:
            if i >= header:
                if changeTOFloat == "yes":
                    list1.append(float(row[col1]))  # 把第二個欄位的資料 放到list1 中
                else:
                    list1.append(row[col1])
            i = i + 1
    return list1

# 取得特定的欄數 不重複的資料
def CSVGetColNoSame(fileName,col1,header=0,changeTOFloat= "no"):
    list1 = []
    with open(fileName, 'r') as fin:
        i = 0
        dataCSV = csv.reader(fin, delimiter=',')  # 用都號區分資料
        for row in dataCSV:
            if i >= header:
                test = row[col1] in list1
                if test == False:
                    if changeTOFloat == "yes":
                        list1.append(float(row[col1]))  # 把第二個欄位的資料 放到list1 中
                    else:
                        list1.append(row[col1])
            i = i + 1
    return list1
# 取得特定的欄數 與特定的欄數相關的資料
def CSVGetColWithSpecial(fileName,col1,specialCol,specialName,header=0,changeTOFloat= "no"):
    list1 = []
    with open(fileName, 'r') as fin:
        i = 0
        dataCSV = csv.reader(fin, delimiter=',')  # 用都號區分資料
        for row in dataCSV:
            if i >= header:
                if row[specialCol] == specialName:
                    if changeTOFloat == "yes":
                        list1.append(float(row[col1]))  # 把第二個欄位的資料 放到list1 中
                    else:
                        list1.append(row[col1])
            i = i + 1
    return list1

"""
#### 第1題 ######
請自行到 openData 找自己感興趣的題目來做
txt, CSV, XLSX, XLS

比如：
https://data.tycg.gov.tw/
https://data.taipei/
http://www.kaggle.com

先不找JSON, XML,  SOAP
"""

# 打開 臺北市所得收入者每人所得－年齡組別按年別(整理).csv 檔案
with open('臺北市所得收入者每人所得－年齡組別按年別(整理).csv', 'r') as fin:        # 打開 臺北市所得收入者每人所得－年齡組別按年別(整理).csv 檔案
    dataCSV = csv.reader(fin, delimiter=',')  # 讀取 csv 檔案，並用逗號區分
    header = next(dataCSV)
    #row1 = CSVGetRow("臺北市所得收入者每人所得－年齡組別按年別(整理).csv",1)
    col1 = CSVGetCol("臺北市所得收入者每人所得－年齡組別按年別(整理).csv",5)
    col1.remove(col1[0])
    col2 = []
    for x in col1:
        col2.append(int(x))

    """
    #### 第2題 ######
    分析數據
    Max, Min, Ave,  Mid 中間值, 均值......
    
    166-CSV-環境輻射即時監測資訊歷史資料-圖表-統計.py
    """
    # print(row1)
    print("可支配所得最大值為", max(col1), "元")
    print("可支配所得最小值為", min(col1), "元")
    print("可支配所得平均值為 %.1f" % (sum(col2) / len(col2)), "元")

    """
    #### 第3題 ######
    畫圖表
    156-作業答案-讀取excel顯示9個圖表.py
    """

    year = CSVGetColNoSame("臺北市所得收入者每人所得－年齡組別按年別(整理).csv",0)
    year.remove(year[0])
    # print(year)

    agerange = CSVGetColNoSame("臺北市所得收入者每人所得－年齡組別按年別(整理).csv",1)
    agerange.remove(agerange[0])
    # print(agerange)

    ageMoney = []
    for x in range(len(agerange)):
        ageMoney.append(x)
        ageMoney[x] = CSVGetColWithSpecial("臺北市所得收入者每人所得－年齡組別按年別(整理).csv",
                                           5,1,agerange[x],changeTOFloat="yes")
    # print(ageMoney)

    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 步驟一（替換字型）
    plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

    dataName = agerange
    yData = ageMoney
    xData = year
    title1 = "台北市所得"
    ytitle = header[5]
    xtitle = header[0]

    # 折線圖

    fig, ax = plt.subplots(nrows=2, ncols=3)  # 上下兩份 左右3份
    i = 0
    while i < len(dataName):
        ax[0, 0].plot(xData, yData[i], label=dataName[i])
        i = i + 1
    ax[0, 0].legend(loc="upper left")
    ax[0, 0].set_title(title1)
    ax[0, 0].set_ylabel(ytitle)  # 顯示y 座標的文字
    ax[0, 0].set_xlabel(xtitle)  # 顯示x 座標的文字

    # 柱狀圖
    i = 0
    bottomMenber = []
    for x in range(len(xData)):
        bottomMenber.append(0)

    while i < len(dataName):

        ax[0, 1].bar(xData, yData[i], label=dataName[i], bottom=bottomMenber)
        x = 0
        # 算底部人數
        while x < len(bottomMenber):
            bottomMenber[x] = bottomMenber[x] + yData[i][x]
            x = x + 1

        i = i + 1
    ax[0, 1].legend(loc="upper left")
    ax[0, 1].set_title(title1)
    ax[0, 1].set_ylabel(ytitle)  # 顯示y 座標的文字
    ax[0, 1].set_xlabel(xtitle)  # 顯示x 座標的文字


    # 　fill圖
    i = 0
    bottomMenber = []
    for x in range(len(xData)):
        bottomMenber.append(0)
    topMenber = []
    for x in range(len(xData)):
        topMenber.append(0)

    # color = ["blue","orange","green"]
    while i < len(dataName):
        # 算頂部人數
        x = 0
        while x < len(topMenber):
            topMenber[x] = topMenber[x] + yData[i][x]
            x = x + 1

        ax[0, 2].fill_between(year, bottomMenber, topMenber, label=dataName[i])

        # 算底部人數
        x = 0
        while x < len(bottomMenber):
            bottomMenber[x] = bottomMenber[x] + yData[i][x]
            x = x + 1

        i = i + 1

    ax[0, 2].legend(loc="upper left")
    ax[0, 2].set_title(title1)
    ax[0, 2].set_ylabel(ytitle)  # 顯示y 座標的文字
    ax[0, 2].set_xlabel(xtitle)  # 顯示x 座標的文字

    # step圖

    i = 0
    bottomMenber = []
    for x in range(len(xData)):
        bottomMenber.append(0)
    topMenber = []
    for x in range(len(xData)):
        topMenber.append(0)

    while i < len(dataName):
        # 算頂部人數
        x = 0
        while x < len(topMenber):
            topMenber[x] = topMenber[x] + yData[i][x]
            x = x + 1

        ax[1, 0].step(year, yData[i], label=dataName[i])

        # 算底部人數
        x = 0
        while x < len(bottomMenber):
            bottomMenber[x] = bottomMenber[x] + yData[i][x]
            x = x + 1

        i = i + 1

    ax[1, 0].legend(loc="upper left")
    ax[1, 0].set_title(title1)
    ax[1, 0].set_ylabel(ytitle)  # 顯示y 座標的文字
    ax[1, 0].set_xlabel(xtitle)  # 顯示x 座標的文字

    # barh圖
    i = 0
    bottomMenber = []
    for x in range(len(xData)):
        bottomMenber.append(0)
    topMenber = []
    for x in range(len(xData)):
        topMenber.append(0)

    while i < len(dataName):
        # 算頂部人數
        x = 0
        while x < len(topMenber):
            topMenber[x] = topMenber[x] + yData[i][x]
            x = x + 1

        ax[1, 1].barh(year, topMenber, left=bottomMenber, label=dataName[i])

        # 算底部人數
        x = 0
        while x < len(bottomMenber):
            bottomMenber[x] = bottomMenber[x] + yData[i][x]
            x = x + 1


        i = i + 1

    ax[1, 1].legend(loc="upper left")
    ax[1, 1].set_title(title1)
    ax[1, 1].set_ylabel(xtitle)  # 顯示y 座標的文字
    ax[1, 1].set_xlabel(ytitle)  # 顯示x 座標的文字

    # stem圖
    i = 0
    bottomMenber = []
    for x in range(len(xData)):
        bottomMenber.append(0)
    topMenber = []
    for x in range(len(xData)):
        topMenber.append(0)

    while i < len(dataName):
        # 算頂部人數
        x = 0
        while x < len(topMenber):
            topMenber[x] = topMenber[x] + yData[i][x]
            x = x + 1

        ax[1, 2].stem(year, yData[i], label=dataName[i])

        # 算底部人數
        x = 0
        while x < len(bottomMenber):
            bottomMenber[x] = bottomMenber[x] + yData[i][x]
            x = x + 1

        i = i + 1

    ax[1, 2].legend(loc="upper left")
    ax[1, 2].set_title(title1)
    ax[1, 2].set_ylabel(ytitle)  # 顯示y 座標的文字
    ax[1, 2].set_xlabel(xtitle)  # 顯示x 座標的文字
    plt.show()







