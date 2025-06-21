import questionary

class MenuRegister:
    def showMenu(self):
        userRegistred = questionary.form(
            name=questionary.text("Name: "),
            password=questionary.password("Password: ")
        ).ask()
        print('User registred',userRegistred)
      
