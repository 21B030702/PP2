import os
print('Exist:', os.access('c:\\Users\\a_nus\\Desktop\\PP2.spring2022', os.F_OK))
print('Readable:', os.access('c:\\Users\\Public\\Desktop\\PP2.spring2022', os.R_OK))
print('Writable:', os.access('c:\\Users\\Public\\Desktop\\PP2.spring2022', os.W_OK))
print('Executable:', os.access('c:\\Users\\Public\\Desktop\\PP2.spring2022', os.X_OK))