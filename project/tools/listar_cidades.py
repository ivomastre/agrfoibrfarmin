from project.tools.connect_db import *
def main():
    select_cidade(create_connection("D:\\sqlite\db\pythonsqlite.db"), "Serra Negra do Norte - RN")

if __name__ == '__main__':
    main()