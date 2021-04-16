import os

def menu():
    print("""Choose option:
    Press 1 to work with files;
    Press 2 to work with directories;
    Press 0 to exit
    """)

def fileMenu():
    print("""Choose option:
    1. Delete file
    2. Rename file
    3. Add content to this file
    4. Rewrite content of this file
    5. Return to the parent directory
    """)

def dirMenu():
    print("""Choose option:
        1. Rename directory
        2. Print number of files
        3. Print number of directories
        4. List content of the directory
        5. Add file to this directory
        6. Add new directory to this directory
        """)

print("Welcome to file manager!")

while True:
    menu()
    # we get the current directory
    curPath = os.getcwd()
    location = int(input())
    if location==1:
        # files
        fileMenu()
        n = int(input())
        if n==1:
            # Delete file
            filename = input('Enter the name of file u want to delete: ')
            if os.path.exists(filename+'.txt'):
                os.remove(curPath + '/' + filename + '.txt')
                print('File removed')
            else:
                print('No such file, bro')
        elif n==2:
            # Rename file
            filename = input('Enter the name of file u want to rename: ')
            if os.path.exists(filename + '.txt'):
                print('Enter the new name of file')
                newName = input()
                os.rename(filename + '.txt', newName + '.txt')
                print('File renamed')
            else:
                print('No such file, bro')
        elif n==3:
            # Add content to this file
            filename = input('Enter the name of file u want to add content: ')
            if os.path.exists(filename + '.txt'):
                print('Enter the new content: ')
                newContent = input()
                curFile = open(filename + '.txt', 'a')
                curFile.write(newContent)
                curFile.close()
                print('Content added')
            else:
                print('No such file, bro')
        elif n==4:
            # Rewrite content of this file
            filename = input('Enter the name of file u want to rewrite:')
            if os.path.exists(filename + '.txt'):
                print('Enter the content:')
                content = input()
                file = open(filename + '.txt', 'w')
                file.write(content)
                file.close()
                print('Everything is okey')
            else:
                print('No such file, bro')
        elif n==5:
            # Return to the parent directory
            os.chdir('..')
            # os.chdir(os.path.dirname(os.getcwd()))
            print('Everything is okey')

    elif location==2:
        # directories
        dirMenu()
        curDir = os.getcwd()
        print(curDir)
        n = int(input())
        if n==1:
            # Rename directory
            dirRename = input('Enter the name of directory u want to rename:')
            if os.path.exists(dirRename):
                newName = input('Enter the new name:')
                os.rename(dirRename, newName)
                print('Directory is renamed')
            else:
                'Something is wrong, bro'
        elif n==2:
            # Print number of files
            dirCount = input('Enter the name of directory u want to print the count of files:')
            if os.path.exists(dirCount):
                dirList = os.listdir(dirCount)
                numOfFiles = len([1 for i in list(os.scandir(dirCount)) if i.is_file])
                print("In this directory " + str(numOfFiles) + 'files.')
            else:
                'Something is wrong, bro'

        elif n==3:
            # Print number of directories
            dirCoco = input('Enter the name of directory u want to print the count of directories:')
            if os.path.exists(dirCoco):
                print(len(next(os.walk(dirCoco))[1]))
            else:
                print('Something is wrong')
        elif n==4:
            # List content of the directory
            dirList = input('Enter the name of directory u want to get list of content:')
            if os.path.exists(dirList):
                print(os.listdir(dirList))
            else:
                print('Something is wrong')
        elif n==5:
            # Add file to this directory
            cocoJambo = input('Enter the name of directory u want to add new file:')
            if os.path.exists(cocoJambo):
                jamboCoco = input('Enter the name of new file:')
                os.mknod(jamboCoco)
                print('okey-dokey')
            else:
                print('404 error)')
        elif n==6:
            # Add new directory to this directory
            dirr = input('Enter the name of directory u want to add new directory:')
            if os.path.exists(dirr):
                newDir = input('Enter the name of new directory:')
                os.mkdir(newDir)
                print('okey-dokey')
            else:
                'Something is wrong!'
    elif location==0:
        # exit
        print('Good bye')
        exit()

