class My_own_class:
     '''def_init_(self, stroka):
        self.stroka = stroka'''
     def getString(self):
          stroka = input()
          self.stroka = stroka
     def  printString(self):
          print(self.stroka.upper())
Arsen = My_own_class()
Arsen.getString()
Arsen.printString()