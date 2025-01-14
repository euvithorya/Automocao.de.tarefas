import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


servidor_smtp = 'smtp.gmail.com'
porta_smtp = 587

email_remetente = 'seu_email@gmail.com'
senha = 'sua_senha'

destinatarios = ['email1@example.com', 'email2@example.com', 'email3@example.com']

assunto = 'Assunto do E-mail'
corpo_email = 'Este é o corpo do e-mail automatizado.'

def enviar_email(destinatario):
    try:
        msg = MIMEMultipart()
        msg['From'] = email_remetente
        msg['To'] = destinatario
        msg['Subject'] = assunto

        msg.attach(MIMEText(corpo_email, 'plain'))

        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        servidor.starttls()
        servidor.login(email_remetente, senha)
        texto = msg.as_string()
        servidor.sendmail(email_remetente, destinatario, texto)
        servidor.quit()

        print(f'E-mail enviado para {destinatario}')
    except Exception as e:
        print(f'Erro ao enviar e-mail para {destinatario}: {e}')

for destinatario in destinatarios:
    enviar_email(destinatario)

#:V