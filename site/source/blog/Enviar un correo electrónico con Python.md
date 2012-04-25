title: Enviar un correo electrónico con Python
date: 2011-05-08 13:29
tags: python, email, smtp, linux, one-liner

Existen varias maneras de enviar un correo electrónico a través de **Python**, 
por ejemplo empleando el modulo `smtplib` de la librería estándar de Python. Si 
estamos en **Linux** y contamos con un servidor de correo funcionando, enviar un
 correo puede ser algo tan sencillo como este script:

    :::python>
    #!/usr/bin/env python
    # -*- coding: utf8 -*-

    import os
    import socket
    import smtplib

    def send_mail_local(subject, text):
        """Send a mail to the user's local mailbox."""
        # Set the local mail address for the script' user
        email = "@".join([os.getenv("LOGNAME"), socket.gethostname()])
        msg = ("From: {0}\nTo: {0}\nSubject: {1}\n{2}".format(email, subject, text))
        server = smtplib.SMTP("localhost")
        server.sendmail(email, email, msg)
        server.quit()
        return

    def main():
        """Main section"""

        send_mail_local("Comprobando el envío de correo localmente",
                        "Si puedes leer esto, tu servidor local SMTP está OK")

        print("Comprueba el correo en tu buzón local {0}\nEste normalmente se "
              "encuentra situado en /var/mail/{1}".
              format("@".join([os.getenv("LOGNAME"), socket.gethostname()]),
                     os.getenv("LOGNAME")))

    if __name__ == "__main__":
        main()


Que si lo ejecutamos, nos generará una salida por consola como esta:

    :::text
    Comprueba el correo en tu buzón local tuusuario@tumaquina
    Este normalmente se encuentra situado en /var/mail/tuusuario


Y tendrás en la bandeja de correo de tu usuario en la maquina algo como esto:

    :::text
    De: 	tuusuario@tumaquina
    Para: 	tuusuario@tumaquina
    Asunto: 	Comprobando el envío de correo localmente
    Fecha: 	Sun, 08 May 2011 12:57:30 +0200

    Si puedes leer esto, tu servidor local SMTP está OK


Es algo realmente sencillo, y la mayoría de las lineas sirven para construir el 
ejemplo, lo que realmente hace el trabajo, y solo necesita el modulo `smtplib` 
para funcionar es esto:

    :::python
    server = smtplib.SMTP("localhost")
    server.sendmail(email, email, msg)
    server.quit()


Pero si lo que queremos es enviar correos más complejos, con adjuntos, empleando 
servidores SMTP externos y enviar con copia (CC) ó copia oculta (CCO) a varios 
usuarios, entonces ya necesitamos emplear las opciones del modulo `email` que 
nos permite hacer prácticamente cualquier tarea relacionada con los correos 
electronicos. Para estas situaciones desarrolle en su día una función que ha 
cubierto todas las situaciones que se me han dado hasta ahora. Además devuelve 
mensajes de error allí donde algo puede ir mal.

    :::python
    # The more complete solution. This adds the Cc: (Carbon Copy) and Bcc: (Blind 
    # Carbon Copy) fields and the ability to add attachments. 
    def send_email(subject, text, send_from="", dest_to=None, attachments=None,
                   send_cc=None, send_bcc=None, server="localhost", port=25,
                   user="", passwd=""):
        """Send a email with(out) attachment(s) enabling CC and BCC fields.

        Arguments:
            (str) subject -- the mail's subject
            (str) text -- the message's text
            (str) send_from -- a sender's email address (default "")
            (list) dest_to -- a list of receivers' email addresses ("")
            (list) attachments -- a list of attachments files (default None)
            (list) send_cc -- a list of carbon copy's email addresses (def. None)
            (list) send_bcc -- a list of blind carbon copy's email addresses (None)
            (str) server -- the smtp server (default "localhost")
            (int) port -- the smtp server port (default 25)
            (str) user -- the smtp server user (default "")
            (str) passwd --the smtp server password (default "")

        If "send_from" or "dest_to" are empty or None, then script user's mailbox 
        is assumed instead. Useful for logging scripts

        """
        local_email = "@".join([os.getenv("LOGNAME"), socket.gethostname()])
        send_from = send_from if send_from else local_email
        dest_to = dest_to if dest_to else [local_email]

        dest_to_addrs = dest_to # receivers mails including to, cc and bcc fields
        message = MIMEMultipart()
        message["Subject"] = subject
        message["From"] = send_from
        message["To"] = COMMASPACE.join(dest_to)
        if send_cc:
            message["Cc"] = COMMASPACE.join(send_cc)
            dest_to_addrs += send_cc
        if send_bcc:
            dest_to_addrs += send_bcc
        message["Date"] = formatdate(localtime=True)
        message.preamble = "You'll not see this in a MIME-aware mail reader.\n"
        message.attach(MIMEText(text))

        # For all type of attachments
        if attachments:
            for att_file in attachments:
                with open(att_file, "rb") as attmnt:
                    att = MIMEBase("application", "octet-stream")
                    att.set_payload(attmnt.read())
                encoders.encode_base64(att)
                att.add_header("content-disposition", "attachment",
                               filename=os.path.basename(att_file))
                message.attach(att)

        # initialize the mail server
        smtp_server = smtplib.SMTP()
        # Connect to mail server
        try:
            smtp_server.connect(server, port)
        except socket.gaierror:
            print("mail error", "Wrong server, are you sure is correct?")
        except socket.error:
            print("mail error", "Server unavailable or connection refused")
        # Login in mail server
        if server != "localhost":
            try:
                smtp_server.login(user, passwd)
            except smtplib.SMTPAuthenticationError:
                print("mail error", "Authentication error")
            except smtplib.SMTPException:
                print("mail error", "No suitable authentication method")
        # Send mail
        try:
            smtp_server.sendmail(send_from, dest_to_addrs, message.as_string())
        except smtplib.SMTPRecipientsRefused:
            print("mail error", "All recipients were refused."
                  "Nobody got the mail.")
        except smtplib.SMTPSenderRefused:
            print("mail error", "The server didn’t accept the from_addr")
        except smtplib.SMTPDataError:
            print("mail error", "An unexpected error code, Data refused")
        # Disconnect from server
        smtp_server.quit()


Para las situaciones en las que no disponemos de un servidor de correo SMTP 
funcionando, podemos montar uno temporalmente para realizar pruebas. La tarea 
puede tan sencilla como recurrir a uno de los **python one-liners** que 
mencionaba en [Python one-liners. Potencia en una sola línea](http://joedicastro.com/python_one_liners_potencia_en_una_sola_linea).

    :::python
    python -m smtpd -n -c DebuggingServer localhost:8025


que es  exactamente lo mismo que hace este script que empleo habitualmente para 
las mismas funciones (me permite montar un segundo servidor SMTP en un puerto 
distinto sin necesitar permisos de administrador, lo que me permite llamarlo 
desde otros scripts). Emplear una u otra forma, pues ya depende de uno.

    :::python
    #!/usr/bin/env python
    # -*- coding: utf8 -*-

    import smtpd
    import asyncore

    def smtp_server(port):
        """Starts a smtp server for test purposes."""
        smtpd.DebuggingServer(("localhost", port), None)

    smtp_server(8025)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


El código completo con ejemplos de estas funciones, se puede encontrar en mi 
repositorio *Python Recipes* que se encuentra alojado en [bitbucket][bb] y en
[github][gh].

  [bb]: http://bitbucket.org/joedicastro/python-recipes
  [gh]: http://github.com/joedicastro/python-recipes
  
