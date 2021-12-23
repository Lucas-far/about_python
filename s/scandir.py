

# Forma de coletar informações sobre arquivos em um local do sistema

from os import scandir

this_path = 'C:\\Users\\Conta secundária\\Desktop\\shortcuts'
target = tuple(scandir(this_path))

print(target)

print([1], target[1].inode())       # 41376821576473041
print([2], target[1].is_dir())      # False
print([3], target[1].is_file())     # True
print([4], target[1].is_symlink())  # False
print([5], target[1].name)          # Downloads.lnk
print([6], target[1].path)          # C:\Users\Lucas\Desktop\Downloads.lnk
print([7], target[1].stat)          #
# print([8], target[1].close())
