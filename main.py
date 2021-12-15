import pdfkit
import secrets
import string
from credential import credential

config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
output_filename = 'out.pdf'
options = {
    "enable-local-file-access": True
}


def split(word):
    return [char for char in word]


with open('names.txt', 'r') as f:
    lines = f.read()

persons = []

# Split string into words
family_list = lines.split(", ")

print("\n")
# Iterate a list
print("Printing all usernames")
for name in family_list:
    chars = split(name)
    username = chars[0]
    length = len(chars)
    c = " "
    spaces = [pos for pos, char in enumerate(name) if char == c]
    spacePos = spaces[0] + 1
    for item in chars[spacePos:]:
        username = ''.join((username, item))

    # Generating Password
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password

    # Write to Object
    u1 = credential()
    u1.username = username.lower()
    u1.password = password
    persons.append(u1)
    print("Username: " + u1.username + " Password: " + u1.password)


def as_round_box(color, content):
    return "<div id=\"content\"" + \
           "style=\"" + \
           "font-family: Calibri; " + \
           f"font-size: 24px; background-color: {color};" + \
           "border-radius: 15px; " + \
           "padding: 30px;\">" + \
           content + \
           "</div>"


def generate_file():
    file = '<div style="height: 300px" style="page-break-before: always;"><img src="/Users/leonarderdik/PycharmProjects/pythonProject/logo.png" ' \
           'alt="Test" width="300px" ' \
           'style="right:0px; position: absolute"><p>B@ltic Networks<br>Hamburg<br><br>Internal document</p></div>  ' \
           '<style>.pb { page-break-before: always; }</style> '

    file += as_round_box("lightgray", "<h1 style=\"font-family: Tahoma;\">Checkliste - Credentials: </h1>")
    for i in persons:
        file += as_round_box("gray",
                             as_round_box("#eeeeee",
                                          "<div> Credentials: <br><input type=\"checkbox\"/> <b>Username:</b> " + i.username + "<br><input "
                                            "type=\"checkbox\"/> <b>Passwort: </b>" + i.password + "<br><hr> "
                                            "<b>Benutzerpfad: ""</b>" +
                                            "C:/balticnetworks/users/" + i.username + "<br><hr> "
                                            "<b>Benutzergruppe: </b>" + "Employees <br><hr> </div>"
                                          ))
    file += "</div>"
    return file


file = generate_file()
print(file)
pdfkit.from_string(file, output_filename, configuration=config, options=options)
