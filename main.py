from vue.base import View
from controller.base import Controller

def main():


    view = View()
    app = Controller(view)
    app.launch()


if __name__ == "__main__":
    main()