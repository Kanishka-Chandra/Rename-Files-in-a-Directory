from os import chdir as change_dir, listdir as list_dir, rename
from sys import exit

parentfolder_path = ''
while parentfolder_path == '':
      parentfolder_path = input("Enter path to the Root folder\n")
      if parentfolder_path == '':
            print("You have not entered the path. Please enter the path")
            print("If you want to exit type quit\n")
      if parentfolder_path.lower() == 'quit':
            exit(0)

image_name = input("Enter new name of image (default is Cover)\n")
pdf_name = input("Enter new name of pdf (default is Part)\n")

if image_name == '':
      image_name = 'Cover'
if pdf_name == '':
      pdf_name = 'Part'

try:
      change_dir(parentfolder_path)
except Exception:
      print("ERROR: Path not found: "+parentfolder_path)
      print("\nPress any key to exit")
      input()
      exit(0)

subfolders = list_dir()

files_in_parentfolder = []
for content in subfolders:
      if "." in content:
            files_in_parentfolder.append(content)

subfolders = [folder for folder in subfolders if folder not in files_in_parentfolder]

subfolder_paths = [parentfolder_path+'\\'+subfolder_name for subfolder_name in subfolders]
folders_with_files_paths = [parentfolder_path] + subfolder_paths

for i in range(0,len(folders_with_files_paths)):
      change_dir(folders_with_files_paths[i])
      file_index = 1
      files_in_parentfolder = list_dir()
      for folder in files_in_parentfolder:
            try:
                  if '.jpg' in folder:
                        src=folder
                        dst=image_name+'.jpg'
                        rename(src,dst)
                  if '.png' in folder:
                        src=folder
                        dst=image_name+'.png'
                        rename(src,dst)
                  elif '.pdf' in folder:
                        src=folder
                        dst=pdf_name+str(file_index)+".pdf"
                        rename(src,dst)
                        file_index+=1
            except Exception:
                  print("ERROR: Cannot rename files. File names already exists.")
                  print("\nPress Enter to exit")
                  input()
                  exit(0)

print("\nRenaming done.\nPress Enter to exit")
input()
exit(0)
