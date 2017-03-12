from bs4 import BeautifulSoup
import urllib2
import sqlite3


def modification_name_call():
    display_name()  # same
    chk = input('By whom you want to modify it ? name , Volume ? , LastTrade ? or Symbol')
    if chk == "volume":
        print('This is by volume on name')
    elif chk == "name":
        name_value = input('Enter the Certain name value to set')
        name_place = input('Enter the name  place where you want to replace the upper value')
        modify_by_name(name_value, name_place)
    elif chk == "lastTrade":
        print('This is by trade on name')
        name_value = input('Enter the Certain name value to set')
        lastTrade_place = input('ENter the lastTrade place where you want to replace the upper value')
        modify_by_namelastTrade(name_value, lastTrade_place)  # this calls the lasttrade and name function
    elif chk == "symbol":
        print('This is by symbol on name')
        name_value = input('Enter the Certain name value to set')
        symbol_value = input('Enter the symbol where you want to check and replace the upper value')
        modify_by_namesymbol(name_value, symbol_value)
    else:
        print('Wrong Input /bad INput <-- check again ')
        exit()


def modification():  # This is the modification function which  is used to modify a particular data
    print('What you want to modify ?')
    input_check = input(
        'Enter volume to modify "volume" , Enter symbol to Modify "Symbol" , Enter name to modify name , Enter lastTrade to modify trade ')
    if input_check == "volume":  # if the user want to modify the volume
        display_volume()  # here you need to have two values , (one to set and another to check
        chk = input('By whom you want to modify it ? name , Volume ? , LastTrade ? or Symbol')
        if chk == "volume":
            volume_value = input('Enter the Certain volume value to set')
            volume_place = input('Enter the Volume place where you want to replace the upper value')
            modify_by_volume(volume_value, volume_place)  # this calls the modification function
        elif chk == "name":
            volume_value = input('Enter the Certain volume value to set')
            name_place = input('Enter the name  place where you want to replace the upper value')
            modify_by_volumename(volume_value, name_place)
        elif chk == "lastTrade":
            volume_value = input('Enter the Certain volume value to set')
            lastTrade_place = input('Enter the LastTrade place where you want to replace the upper value')
            modify_by_volumelastTrade(volume_value, lastTrade_place)
        elif chk == "symbol":
            volume_value = input('Enter the Certain volume value to set')
            symbol_place = input('Enter the Symbol place where you want to replace the upper value')
            modify_by_volumesymbol(volume_value,
                                   symbol_place)  # this calls the symbol function to modify the volume at a certain place
        else:
            print('Wrong Input /bad INput <-- check again ')
            exit()
    elif input_check == "Symbol":
        display_symbol()  # here you have to do the same
        chk = input('By whom you want to modify it ? name , Volume ? , LastTrade ? or Symbol')
        if chk == "volume":
            print('This is by volume on symbol')
        elif chk == "name":
            name_value = input('Enter the Certain name value to set')
            name_place = input('Enter the name  place where you want to replace the upper value')
        elif chk == "lastTrade":
            print('This is by trade on symbol')
        elif chk == "symbol":
            print('This is by symbol on symbol')
        else:
            print('Wrong Input /bad INput <-- check again ')
            exit()
    elif input_check == "name":
        modification_name_call()  # this calls the modification by the function-->
    elif input_check == "lastTrade":
        display_lastTrade()  # same as above just change
        chk = input('By whom you want to modify it ? name , Volume ? , LastTrade ? or Symbol')
        if chk == "volume":
            print('This is by volume on name')
        elif chk == "name":
            name_value = input('Enter the Certain name value to set')
            name_place = input('Enter the name  place where you want to replace the upper value')
            modify_by_name(name_value, name_place)
        elif chk == "lastTrade":
            print('This is by trade on name')
        elif chk == "symbol":
            print('This is by symbol on name')
        else:
            print('Wrong Input /bad Input <-- check again ')
            exit()
    else:
        print('Wrong choice exiting the propgram !!!')
        exit()


def modify_by_volume(volume_value, volume_place):
    print('Modification in progress')
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''UPDATE Finance SET volume = (?) WHERE volume= (?)''', (volume_value, volume_place))
    conn.commit()
    curr.close()
    conn.close()  # this will close the connection
    print('Modification complete!.')


def modify_by_volumename(volume_value, name_place):
    print('Modification in progress by name ')
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''UPDATE Finance SET volume = (?) WHERE name= (?)''', (volume_value, name_place))
    conn.commit()
    curr.close()
    conn.close()  # this will close the connection
    print('Modification complete!.')


def modify_by_volumelastTrade(volume_value, lastTrade_value):
    print('Modification in progress by lasttrade value on volume. ')
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''UPDATE Finance SET volume = (?) WHERE LastTrade= (?)''', (volume_value, lastTrade_value))
    conn.commit()
    curr.close()
    conn.close()  # this will close the connection
    print('Modification complete!.')


def modify_by_volumesymbol(volume_value, symbol_value):
    print('Modification in progress by lasttrade value on volume. ')
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''UPDATE Finance SET volume = (?) WHERE Symbol= (?)''', (volume_value, symbol_value))
    conn.commit()
    curr.close()
    conn.close()  # this will close the connection
    print('Modification complete!.')


def modify_by_name(name_value, name_place):
    print('Modification in progress by name value on name. ')
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''UPDATE Finance SET name = (?) WHERE name= (?)''', (name_value, name_value))
    conn.commit()
    curr.close()
    conn.close()  # this will close the connection
    print('Modification complete!.')


def modify_by_namesymbol(name_value, symbol_place):
    print('Modification in progress by symbol value on name. ')
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''UPDATE Finance SET name = (?) WHERE Symbol= (?)''', (name_value, symbol_place))
    conn.commit()
    curr.close()
    conn.close()  # this will close the connection
    print('Modification complete!.')


def modify_by_namelastTrade(name_value, lastTrade_value):
    print('Modification in progress by lastTrade value on name. ')
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''UPDATE Finance SET name = (?) WHERE LastTrade= (?)''', (name_value, lastTrade_value))
    conn.commit()
    curr.close()
    conn.close()  # this will close the connection
    print('Modification complete!.')


def display_volume():
    print('This is to modify the volume')
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''SELECT Volume FROM FINANCE''')
    Volume_list = curr.fetchall()
    print(Volume_list)
    conn.commit()
    curr.close()
    conn.close()


def display_name():
    print('This is to modify the Name')
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''SELECT name FROM FINANCE''')
    name_list = curr.fetchall()
    print(name_list)
    conn.commit()
    curr.close()
    conn.close()


def display_symbol():
    print('This is to modify the symbol')
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''SELECT Symbol FROM FINANCE''')
    symbol_list = curr.fetchall()
    print(symbol_list)
    conn.commit()
    curr.close()
    conn.close()


def display_lastTrade():
    print('This is to modify the volume')
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''SELECT lastTrade FROM FINANCE''')
    last_Trade = curr.fetchall()
    print(last_Trade)
    conn.commit()
    curr.close()
    conn.close()


def insertintodatabase(symbol, name, lastTrade, volume):
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''INSERT INTO FINANCE (SYMBOL , Name , LastTrade , Volume ) VALUES (?,?,?,?)''',
                 (symbol, name, lastTrade, volume))
    conn.commit()
    curr.close()
    conn.close()


def database_creation():
    conn = sqlite3.connect('finance.sqlite')
    curr = conn.cursor()
    curr.execute('''DROP TABLE IF EXISTS FINANCE''')
    curr.execute(
        '''CREATE TABLE IF NOT EXISTS FINANCE(Symbol TEXT, Name TEXT , LastTrade TEXT , Volume TEXT)''')
    print('Data base is created !')
    curr.close()
    conn.close()


def read_from_web(inner_link):
    data_in_file = urllib2.urlopen(inner_link)  # retrives the web  page using the urllib requests to open url
    soup = BeautifulSoup(data_in_file, "lxml")  # Access the Bs4 such that the retrieved page is beautified
    data_in_file.close  # urllib is closed
    # print (soup)
    required_table = soup.find_all(class_="yfnc_tableout1")
    required_table = BeautifulSoup(str(required_table), "lxml")
    required_inner_table = required_table.find_all(class_="yfnc_tabledata1")
    # data_list = list()

    for j in required_inner_table:
        if j.string is not None:
            data_list.append(j.string)
        # print (j.string)
        try:
            if j.b.span is not None:
                # print (j.b.span.string)
                data_list.append(j.b.span.string)
                # print (j.nobr.small.span.string)
                data_list.append(j.nobr.small.span.string)
        except:
            continue
        else:
            continue
    element = 0
    while element < len(data_list) - 4:
        print(str(data_list[element] + " " + str(data_list[element + 1]) +
                  str(str(data_list[element + 2]) + " " + str(data_list[element + 3]) + " " + str(
                      data_list[element + 4]))))
        print('*******inserted*******')  # debug purposes
        element += 5


def scrap_link(link, pages):
    counter = 0  # counter is just to check if pages doesnt cross the link sized pages
    while counter < pages:
        read_from_web(link + str(counter))
        print(link + str(counter))  # Visualize the links in the compiler
        counter += 1  # this is the counter +1 such that the automata is finite
    print('Pages link generated!')  # this generates the link of the pages


if __name__ == '__main__':  # this is the main entry of the program
    link = "https://uk.finance.yahoo.com/q/cp?s=%5EFTSE&c="  # this is the main link which is needed to be scrapped
    page_no = (input('How much pages You want to scrap from the web ?'))  # identify users how much pages
    if page_no is "": page_no = int(3)
    page_no = int(page_no)  # this is to identify how much page numbers we have
    database_creation()  # this is for the database creation
    data_list = list()  # this is the data list
    scrap_link(link, page_no)  # this calls the function of the scrap link to scrap the data from the web
    element = 0
    while element < len(data_list) - 4:  # inserts all the elements in to the database
        insertintodatabase(data_list[element], data_list[element + 1],
                           str(str(data_list[element + 2]) + " " + str(data_list[element + 3])),
                           data_list[element + 4])
        print('*******inserted processing*******')  # debug purposes
        element += 5
    print(' Insertion is completed !!! ')
    keyword = (
        input('Do you want to Modify the data ? Y/y for Yes , N/n for no'))  # if you want to modify this calls
    if keyword in ['y', 'Y']:
        print('Yes you want to modify the data ')
        modification()  # modification function is called
    elif keyword in ['n', 'N']:
        print('No? ok then Exiting the Program')
        exit()  # Exit function is called cause there is no need to continue to another as we dont want modification
    else:
        print('Invalid input , next time try to read the statment carefully')
        exit()
    # Note the values will keep on updating whenever you rerun the program , since the values on the links are updating
    #  Time by time (even in seconds )
