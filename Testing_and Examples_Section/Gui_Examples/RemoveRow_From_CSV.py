""" ==============TASK
1. Search for any given username
2. Delete the whole row for that particular user

e.g.
Enter username: marvR
>>The record for marvR has been deleted from file.
"""

import csv
def main():
    #1. This code snippet asks the user for a username and deletes the user's record from file.
    updatedlist=[]
    with open("fakefacebook.txt",newline="") as f:
      reader=csv.reader(f)
      username=input("Enter the username of the user you wish to remove from file:")
      
      for row in reader: #for every row in the file
            
                if row[0]!=username: #as long as the username is not in the row .......
                    updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'
      print(updatedlist)
      updatefile(updatedlist)
        
def updatefile(updatedlist):
    with open("fakefacebook.txt","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")
        

main()