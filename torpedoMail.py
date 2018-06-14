#!usr/bin/Python3


import smtplib,  email.mime.base
from email  import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text  import MIMEText 



'''Generamos la infomarcion para el envio de los mails, destino e autentificacion'''
'''Retorna un diccionario con toda la info'''

def  fromTo():
        From = {}
        addr_from ='agustinbmaletti@gmail.com'
        addr_to = str(input('Ingresa o e-mail destino:'))
 
        smtp_server = 'smtp.gmail.com'
        smtp_user=  str(input('Ingresa tu usuario Gmail:  '))
        smtp_pass=str(input('Ingresa password: '))
        infoSoup ={'from': addr_from,      'to': addr_to,
                    'server': smtp_server,'user': smtp_user, 
                    'passw': smtp_pass }
        return infoSoup

'''Gravamos infoSoup'''
infoSoup_ = fromTo()    

'''Construimos el mensaje , plain ou html '''
def mailConstructor():
        msg = MIMEMultipart() 
        msg['From'] = infoSoup_.get('from')
        msg['To'] = infoSoup_.get('to')
        msg['Subject'] = str(input(' Ingresa o asunto do Mail:  ') )
        text = str(input('Ingresa o texto do Mail'))
        msg.attach(MIMEText(text, 'plain'))
        msgSoup = {'msg':msg, 'msgFrom':msg['from'],
        'msgSubject':msg['Subject'], 'texto':text }
        return msgSoup
  
'''Gravamos el diccionario y colocamos msg en una variable por que la vamos a necesitar usar mas'''
    msgSoup_= mailConstructor()
    msg = msgSoup_.get('msg')


'''Elegimos que archivo queremos adjuntar'''
def elegirArchivo():
        opcion = str(input('Adjuntar Archivo:a)Aeropark\nb) Mackovieky\nc) Ningun Archivo\n'))
        if  opcion == 'a':
            archivoAdjunto ='Aeropark.pdf'
        elif opcion =='b':
            archivoAdjunto  ='Mackovieky.pdf'
        elif opcion == 'c':
            archivoAdjunto = 0
        infoArchivo = {'opc':opcion, 'archivo':archivoAdjunto}
        return infoArchivo

'''Gravamos info Archivo'''
    infoArchivo_= elegirArchivo()        

'''Abrimos e adjuntamos el archivo'''
#@trace
def adjuntarArchivo():
        if infoArchivo_.get('opc') == 'a' or  'b':      
            archivoAdjunto = infoArchivo_.get('archivo')
            with open('/home/agustinmaletti/Escritorio/CorretorImoveis/Lopes/EmprendimentosPdf/Adjuntos'+archivoAdjunto, 'rb') as fp:
                adjunto=MIMEBase('multipart','encrypted')
                adjunto.set_payload(fp.read())
                encoders.encode_base64(adjunto)
                adjunto.add_header('Contetent-Disposition', 'attachment', filename=archivoAdjunto_)
            msg.attach(adjunto)
        else:
        pass
    return None   
     
adjuntarArchivo()  

'''Creamos el smtpObjt e mandamos el mail'''
def mandarMail():
        smtpObj=smtplib.SMTP(infoSoup_.get('server'),587)#creating smtp object
        smtpObj.ehlo()                                      # saying hello to the server
        smtpObj.starttls()                                   #start tls encrytation
        try :
            smtpObj.login( infoSoup_.get('user'), infoSoup_.get('passw')) #login ingresado
            print('ACCESS GRANTED, Now I will send..')
        smtpObj.sendmail(infoSoup_.get('from') , infoSoup_.get('to'), msg.as_string())
        smtpObj.quit() 
        return None                                        #apagamos conexion


mandarMail()



