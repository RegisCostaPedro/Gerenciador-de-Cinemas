import questionary

class MenuLogin:
    def showMenu(self):
        userAuth = questionary.form(
            name=questionary.text("Name: "),
            password=questionary.password("Password: ")
        ).ask()
        print('User log',userAuth)
      
