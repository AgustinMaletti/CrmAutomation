#!/usr/bin/python3
#Discador
#el programa esta armado con 100% de zoom pyautogui, pyperclip, time
import pyperclip, time, pyautogui, openpyxl
import torpedoMail as tpd


pyautogui.FAILSAFE = True


campoTelefono = (400, 486)
campoDDD = (348, 486)
campoNombre = (355, 451)

subCopiar_telefono = (471, 245)
subSeleccionarTodo_nombre = (385,532)
subCopiar_nombre = (408, 214)
subCopiar_DDD = (397,273)

discador = (1250,110)
botonLlamar = (1170,190)
botonColgar = (1299,200)

barraDesplazadora = (1360,183)
barraDragTo = (1360,446)

consolaDeGestion =(1172, 621)

botonOpciones = (566,288)

contestadorAutomatico_opciones = (444,743)
naoInteresa_opciones = (477,689)
naoAtende_opciones = (472,600)
numeroErrado_opciones = (446,720)
botonFinalizarGestion = (615,469)
aceptarGestion = (907,390)




#pyautogui.click(button='left',duration=0.22) 
#pyautogui.moveTo(campoTelefono)
#pyautogui.click(button='left',duration=0.25)
#pyautogui.doubleClick(button='left')


#

#COPIAR NOMBRE
pyautogui.click(campoNombre, clicks=3, duration=0.2)
pyautogui.click(button='right')
pyautogui.click(subCopiar_nombre, duration=0.2)
nombre = str(pyperclip.paste())
print(nombre)

#COPIAR TELEFONO
pyautogui.click(campoTelefono, clicks=3, duration=0.2)
pyautogui.click(button='right')
pyautogui.click(subCopiar_telefono, duration=0.2)
telefono = str(pyperclip.paste())
print(telefono)

time.sleep(2)
#movermouse a la consola python para poder gestionar el llamado
pyautogui.click(consolaDeGestion,duration=0.25)



        
def cortarTelefono():
    pyautogui.moveTo(botonColgar)
    pyautogui.click(button="left",duration=0.25)


def clickAndDragBar():
    pyautogui.moveTo(barraDesplazadora,duration=0.25)
    pyautogui.dragTo(barraDragTo,duration=0.25)
    
def clickOption():
    pyautogui.click(botonOpciones, button='left',duration=0.35)
    

def clickToContestadorAutomatico():
    pyautogui.click(contestadorAutomatico_opciones,button='left', duration=0.35)

def clickToNaoAtende():
    pyautogui.click(naoAtende_opciones,button='left',duration=0.35)

def clickToNaoInteressa():
    pyautogui.click(naoInteresa_opciones, button="left",duration=0.35)

def clickToNumeroErrado():
    pyautogui.click(numeroErrado_opciones,button="left",duration=0.35)


def finalizarGestion():
    pyautogui.click(botonFinalizarGestion,button="left",duration=0.55)

def clickAceptarGestion():
    pyautogui.click(aceptarGestion,duration=0.55)

#este click es para dejar el mouse arriva del scrip para poder correro con f5
def ultimoClick():
    pyautogui.click(1178,588,duration=0.3)
    pyautogui.typewrite(['up'])

def guardarDato():
    wb = openpyxl.load_workbook('/home/agustinmaletti/Escritorio/CorretorImoveis/Lopes/prospect.xlsx')
    sheet = wb['ArchivoGeral']
    ultimaFila = sheet['D1'].value 
    sheet['A' + str(ultimaFila )] = nombre
    sheet['B' + str(ultimaFila )] = telefono
    sheet['D1'] = ultimaFila + 1
    wb.save('/home/agustinmaletti/Escritorio/CorretorImoveis/Lopes/prospect.xlsx')
    notaOpcion= input('\n\n\n\nQuieres colocar Nota?, s ou n: ')
    if notaOpcion == 's':
        nota = input('ingresa nota: ')
        sheet['C' + str(ultimaFila)] = nota
        wb.save('/home/agustinmaletti/Escritorio/CorretorImoveis/Lopes/prospect.xlsx')
        wb.close()
    elif notaOpcion == 'n':
        wb.close()
        print('Sin nota')
    



def ligarMaisTarde():
    pyautogui.click(456,420,duration=0.25)
    pyautogui.click(456,212,duration=0.25)
    if hora==1:
        pyautogui.click(456,265,duration=0.25)#11-12
        pyautogui.click(693,392,duration=0.15)#finalizar gestion
    if hora==2:
        pyautogui.click(456,286,duration=0.25)#12-13
        pyautogui.click(693,392,duration=0.15)#finalizar gestion

    if hora==3:
        pyautogui.click(456,367,duration=0.25)#14-15
        pyautogui.click(693,392,duration=0.15)#finalizar gestion

    if hora==4:
        pyautogui.click(456,399,duration=0.25)#15-16
        pyautogui.click(693,392,duration=0.15)#finalizar gestion

    if hora==5:
        pyautogui.click(456,426,duration=0.25)#16-17
        pyautogui.click(693,392,duration=0.15)#finalizar gestion        
    if hora==6:
        pyautogui.click(456,452,duration=0.25)#17-18
        pyautogui.click(693,392,duration=0.15)#finalizar gestion

    if hora==7:
        pyautogui.click(456,476,duration=0.25)#18-19 
        pyautogui.click(693,392,duration=0.15)#finalizar gestion
    if hora==8:
        pyautogui.click(456,502,duration=0.25)#19-20                      
        pyautogui.click(693,392,duration=0.15)#finalizar gestion
        



# --------------------MENU---------------------------------------------

print("1. Contestador  Automatico \n2. Nao Atende \n3. Nao tem Interesse\n4. Numero Errado\n5. Ligar Mais Tarde\n6. Gestion Manual\n7. Guardar Dato\n8. Torpedo Mail" )

gestionOption=int(input(" Ingresa opcion de gestion: "))
print(gestionOption)

if gestionOption==1:
     cortarTelefono()
     clickAndDragBar()
     clickOption()
     clickToContestadorAutomatico()
     finalizarGestion()
     clickAceptarGestion()
     ultimoClick()

if gestionOption==2:
    cortarTelefono()
    clickAndDragBar()
    clickOption()
    clickToNaoAtende()
    finalizarGestion()
    clickAceptarGestion()
    ultimoClick()
    
if gestionOption==3:
    cortarTelefono()
    clickAndDragBar()
    clickOption()
    clickToNaoInteressa()
    finalizarGestion()
    clickAceptarGestion()
    ultimoClick()

if gestionOption==4:
    cortarTelefono()
    clickAndDragBar()
    clickOption()
    clickToNumeroErrado()
    finalizarGestion()
    clickAceptarGestion()
    ultimoClick()
    

if gestionOption==5:
    print("1. 11-12hs\n2. 12-13hs\n3. 14-15hs\n4. 15-16hs\n5. 16-17hs\n6. 17-18hs\n7. 18-19hs\n8. 19-20hs\n")
    hora=int(input(" Ingresa opcion de Horario: "))
    cortarTelefono()
    clickAndDragBar()
    clickOption()
    ligarMaisTarde()#finalizar gestion esta en esta funcion
    clickAceptarGestion()
    ultimoClick()
    
if gestionOption==6:
    print("Manual")

if gestionOption==7:
   cortarTelefono()
   guardarDato()
   ultimoClick() 
    
if gestionOption==8:
    infoSoup_ = tpd.FromTo()
    msgSoup_= tpd.mailConstructor()
    msg = msgSoup_.get('msg')
    infoArchivo_ = tpd.elegirArchivo()
    tpd.adjuntarArchivo()
    tpd.mandarMail()
    
    
     
#doble click
#copy to pyperclip
#moverse al zoiper
#escirbir +5548
#pegar telefono
#mover mouse para llamar
#llamar
    
