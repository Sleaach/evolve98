from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
def mail():
    try:
        email = input("Gönderen Mail: ")
        postsifre = input("Gönderen Şifre veya Uygulama Şifresi: ")
        send = input("Alıcı Mail Adresi: ")
        subjet = input("Konu: ")
        message = input("Mesaj: ")

        content = MIMEMultipart()
        content["From"] = email
        content["To"] = send
        content["Subject"] = subjet
        content.attach(MIMEText(message, "plain"))

        mail = smtplib.SMTP("smtp.yandex.com", 587)
        mail.ehlo()
        mail.starttls()

        mail.login(email, postsifre)

        mail.sendmail(email, send, content.as_string())

        mail.quit()

        print("\nMail gönderildi.")
    except Exception as e:
        print(f"Bir hata oluştu. {e}")
