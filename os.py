# very useful see video 46

import os
folders = os.listdir("data")
print(os.getcwd())
os.chdir(".//data")
print(os.getcwd())
# print(folders)

# for folder in folders: 
#     print(folder) 
# if(not os.path.exists("data")):
#     os.mkdir("data")
# for i in range(0, 100):
#     os.rename(f"data/Day{i+1}", f"data/Day {i+1}")
    