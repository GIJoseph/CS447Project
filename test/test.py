import pefile
pe = pefile.PE('MTGAInstaller.exe')
print(pe.FILE_HEADER)
print(pe.PE_TYPE)
