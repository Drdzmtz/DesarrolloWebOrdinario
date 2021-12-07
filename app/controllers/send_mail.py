from typing import Dict
from app.models.User_dal import User_dal
from app.models.Mail import Mail_Sender

html = '''\
    <!DOCTYPE html>
	<html>
	<head>
	<title></title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta content="" />
	
	</head>
	
	<table  cellpadding="0" cellspacing="0" width="100%">
		<tr>
			<td align="center" style="background-color: #eeeeee;">
			<table align="center" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
				<tr>
					<td align="left" valign="top" style="font-size:0; padding: 15px 0px 2px 20px;" bgcolor="#10476b">
	  
					<div style="display:inline-block; vertical-align:top; width:100%;">
						<table align="left" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;">
							<tr>
								<td align="left" valign="top" style="font-family: Open Sans, Helvetica; font-size: 34px; font-weight: 800; line-height: 35px;">
									<h1 style="font-size: 36px; font-weight: 800; color: #ffffff;">Administradores: <span style="color: LightGray; font-size: 28px;" > Notificacion de Contacto de cliente</span> </h1>
								</td>
							</tr>
						</table>
					</div>
	
	
	
				</tr>
				<tr>
					<td align="center" style="padding: 35px 35px 20px 35px; background-color: #ffffff;" bgcolor="#ffffff">
	
					<table >
						<tr>
							<td align="center" style="font-family: Open Sans, Helvetica; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 25px;">
								<h2 style="font-size: 30px; font-weight: 800; line-height: 36px; color: #333333; margin: 0;">
									Notificacion de contacto de cliente <span style="color:#3c84ab;"> {{ full_name }} </span>
								</h2>
							</td>
						</tr>
						<tr>
							<td align="left" style="font-family: Open Sans, Helvetica; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 10px;">
								<p style="font-size: 16px; font-weight: 400; line-height: 24px; color: #777777;">
									Cliente <span style="color:#3c84ab;"> {{ full_name }} </span> con correo <span style="color:#3c84ab;"> {{ email }} </span> a dejo el siguiente mensaje a través del servicio de contacto.
								</p>
								<p style="font-size: 16px; font-weight: 400; line-height: 24px; color: #777777;">
								<span style="font-weight: 800;">Mensaje: </span> 
                                <br>
                                {{ message }}
								</p>
							</td>
						</tr>
						<tr>
							<td align="left" style="padding-top: 20px;">
								<table cellspacing="0" cellpadding="0" width="100%">
									<tr>
										<td width="75%" align="left" bgcolor="#eeeeee" style="font-family: Open Sans, Helvetica; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px; color:black;">
											Correo
										</td>
										<td width="25%" align="left" bgcolor="#eeeeee" style=" color:black;font-family: Open Sans, Helvetica; font-size: 12px; font-weight: 800; line-height: 24px; padding: 10px;">
										{{ email }}
										</td>
									</tr>
									<tr>
										<td width="75%" align="left" style="font-family: Open Sans, Helvetica; font-size: 16px; font-weight: 400; line-height: 24px; padding: 5px 10px;color:black;">
											Numero de telefono
										</td>
										<td width="25%" align="left" style="font-family: Open Sans, Helvetica; font-size: 12px; font-weight: 400; line-height: 24px; padding: 5px 10px; color:#3c84ab">
										{{ phone_number }}
										</td>
									</tr>

								</table>
							</td>
						</tr>
						<tr>
						</tr>
					</table>
	
					</td>
				</tr
                <tr>
					<td align="center" style="background-color: #ffffff;" bgcolor="#ffffff">
				<div style="text-align: center; width: 100%;"> 				
					<table align="center; cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
					<tr>

							<p style="font-family: Open Sans, Helvetica;font-size: 12px; font-weight: 400; line-height: 20px; color: #777777;">
								Favor de no responder a esta dirección de correo electrónico. <br> Contactarse con el cliente de la manera mas apropiada
							</p>
					</tr>
				<tr>
					<td align="center" style=" padding: 35px; background-color: #8ec0db;" bgcolor="#8ec0db">
                        <img src="../static/images/large-logo.png" alt="">
					</td>
				</tr>

					</table>
				</div>
	
	
					</td>
				</tr>
			</table>
	
			</td>
		</tr>
	</table>
	   
	</body>
	</html>'''

text = """\
    Administradores: Notificacion de Contacto de cliente
    Notificacion de contacto de cliente {{ full_name }}
    Cliente {{ full_name }} con correo {{ email }} a dejo el siguiente mensaje a través del servicio de contacto.
    Mensaje:
    {{ message }}
"""

def mail_tag_replacer(to_replace:Dict[str, str], text:str) -> str:
    
    for k,v in to_replace.items():
        text = text.replace(k, v, -1)

    return text

def send_mail(form:dict):
    db = User_dal()
    res = db.get_all()

    emails = []
    for user in res.values():
        emails.append(user.get("email", ""))

    to_replace = {
        "{{ full_name }}":      form.get("full_name", ""),
        "{{ email }}":          form.get("email", ""), 
        "{{ message }}":        form.get("message", ""), 
        "{{ phone_number }}":   form.get("phone_number", "") ,
    }

    html_template = mail_tag_replacer(to_replace, html)
    text_template = mail_tag_replacer(to_replace, text)

    mail_sender = Mail_Sender(subject=          "Contacto de Clientes",  
                              receivers=        emails,
                              html_template=    html_template,
                              text_template=    text_template)

    try:
            mail_sender.send_mail()
    except Exception as e: return {"Success": False, "Error": str(e)}

    return {"Success": True, "mensaje": "Correo mandado con exito"}

