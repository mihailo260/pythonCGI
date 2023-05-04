#!C:\Users\Mihailo\AppData\Local\Programs\Python\Python39\python.exe
import cgi, cgitb
import re
import sys
cgitb.enable()
form = cgi.FieldStorage()


def printHtml():
    print("<html>")
    print("<head>")
    print("<title>Checkbox - Third CGI Program</title>")
    print("</head>")
    print("<body>")
    print("<div>")
    print("<h2> Ime narucioca %s</h2>" % imePrezime)
    print("<h2> adresa narucioca is %s</h2>" % adresa)
    print("<h2> telefon %s</h2>" % telefon)
    print("<h2> email %s</h2>" % email)
    print("<h2> vrsta pice %s</h2>" % vrsta_pice)
    print("<h2> velicina %s</h2>" % velicina)
    print("</div>")
    print("</body>")
    print("<script>")
    print(" setTimeout(() => {")
    print("window.location.replace('http://localhost/index.html?Error=ok')")
    print("}, 3000);")
    print("</script>")
    print("</html>")
telefonPatern = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
emailPatern = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
redirekcija = "http://localhost/index.html"
print("Content-type:text/html\r\n\r\n")
if form.getvalue('submit'):
    imePrezime = form.getvalue('imePrezime')
    adresa = form.getvalue('adresa')
    telefon = form.getvalue('telefon')
    email = form.getvalue('email')
    vrsta_pice = form.getvalue('vrsta_pice')
    velicina = form.getvalue('velicina')

    if imePrezime is None or adresa is None or telefon is None or email is None or vrsta_pice is None or velicina is None:
        print('<meta http-equiv=refresh content=0;URL='+redirekcija+"?Error=praznoPolje"+'>')
        sys.exit()
    if not re.search(telefonPatern,telefon):
        print('<meta http-equiv=refresh content=0;URL=' + redirekcija + "?Error=telefon" + '>')
        sys.exit()
    if not re.search(emailPatern,email):
        print('<meta http-equiv=refresh content=0;URL=' + redirekcija + "?Error=email" + '>')
        sys.exit()

    file1 = open("PORUDZBINA.txt", "a")
    file1.write(imePrezime +" "+ adresa +" "+ telefon + email + "vrsta pice"+vrsta_pice + "velicina"+velicina+"\n")
    file1.close()
    printHtml()
    # print('<meta http-equiv=refresh content=0;URL=' + redirekcija + "?Error=ok" + '>')

else:
    print("Location: http://localhost/index.html")


