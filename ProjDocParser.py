from bs4 import BeautifulSoup
import csv

html = open("C:/BasicWorkDocs_203-104_WA/projectDoc/Object Documentation (20190312163416)/1.html").read()
soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all("table", "OBJECTNAME")
count = 1
objectNames = []
objNameDict = {}
objDict = {}


def print_deets(obj, objname=''):
    """Prints the details of an object including opject type and assigned value at time of call"""
    objectStr = objname
    print(objname + ' [Type: ' + str(type(obj)) + ']: ' + objectStr + '\r\n')
    return


# print('Tables [Type: ' + str(type(tables)) + ']:\r\n' + str(tables) + '\r\n')
for table in tables:
    rowCount = 1
    curRowDict = {}
    ObjectNameParentTable = table.parent
    for table_row in table.find_all('tr'):
        rowCount = rowCount + 1
        ColCount = 1
        for column in table_row.find_all('td'):
            if column.string is not None:
                colList = [column.string]
                objectNames.append({'id':str(count), 'row':{'name': column.string}})
                # print_deets(column. 'column')
                # print_deets(table_row, 'table_row')
                tableSectionHeaderMainBody = table.find_next('table','SECTIONHEADER').find_next('table', 'MAINBODY')
                # print_deets(tableSectionHeaderMainBody, 'tableSectionHeaderMainBody')
                DetailRows = tableSectionHeaderMainBody.find_all('tr')
                # print_deets(DetailRows, 'DetailRows')

                for DetailRow in DetailRows:
                    # print_deets(DetailRow, 'DetailRow')
                    detailColumns = DetailRow.find_all('td')
                    # print_deets(detailColumns, 'detailColumns')
                    for detailCol in detailColumns:
                        imgTag = detailCol.find('img')
                        # print_deets(imgTag, 'imgTag')
                        if imgTag is not None: imgTag.extract()
                        if detailCol is not None:
                            print_deets(detailCol, 'detailCol')
                            detailColString = detailCol.string
                            if detailColString is not None:
                                if detailColString[-1] == ':':
                                    key = 'KEY'
                            # print_deets(detailColString, 'detailColString')
                            key = ''

            ColCount = ColCount + 1
        curRowDict.clear()
    count = count + 1


"""
#with open('..\output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(objectNames)
"""
