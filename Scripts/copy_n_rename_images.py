import shutil

original = r'/Users/johnsonnieh/Documents/hapebeast/HapeM_images/wehapetogether.png'
target = r'/Users/johnsonnieh/Documents/hapebeast/HapeM_images/wehapetogether_'


for i in range(1,1001):
    new_target = target + f'{i}' + '.png'
    shutil.copyfile(original, new_target)

