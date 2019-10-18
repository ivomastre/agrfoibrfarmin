from project.tools.main import writeContacts


def main():
    print("digite uma cidade: ")
    x = input()
    writeContacts("contacts.xlsx", x)

main()
