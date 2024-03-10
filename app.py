from flask import Flask, render_template, request
import smtplib

app = Flask(__name__, static_folder='static', template_folder='.')


EMAIL_ADDRESS = 'nicolas.descarp@outlook.fr'
EMAIL_PASSWORD = 'barriere76*'

@app.route('/',  methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/projects', methods=['GET'])
def project():
    return render_template('project.html')


@app.route('/contact', methods=['POST', 'GET'])
def send_email():
    if request.method == 'GET':
            return render_template('contact.html')


    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        email = request.form['mail']
        message = request.form['message']

        # Créer le contenu du mail
        email_content = f"Nom: {name}\nSujet: {subject}\nEmail: {email}\nMessage: {message}"

        # Envoyer l'e-mail
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, email_content)

        return 'Email envoyé avec succès'

if __name__ == '__main__':
    app.run(debug=True)
