from PIL import Image, ImageDraw, ImageFont
import pandas as pd

#def getUserDetails():
  #return userCount,locationInImage

userCount,locationInImage=getUserCount()

form=pd.read_excel("userForm.xlsx")

userName=form['Name'].tolist()
locationList=form['Location'].tolist()
addressList=form['Address'].tolist()
vehicleNumber=form['VehicleNumber'].tolist()
wheelNumber=form['Wheeler'].tolist()
expiaryDate=form['Expiary'].tolist()
inspectionDueDate=form['DueDate'].tolist()
inspectionFreeReceiptNumber=form['InceptionReceipt'].tolist()
applicationNumber=form['Application'].tolist()
receiptDate=form['Receipt'].tolist()
chassisNumber=form['Chassis'].tolist()
engineNumber=form['Engine'].tolist()
seatingCapacity=form['Seating'].tolist()
bodyType=form['Type'].tolist()
registerationNumber=form['Registeration'].tolist()
vehicleCategory=form['Category'].tolist()
remark=form['Remark'].tolist()
inspectedBy_type=form['Inspected'].tolist()
printedOn=form['Printed'].tolist()
manufacturingYear=form['Manufacture'].tolist()
inspectedOn=form['InspectedDate'].tolist()
inspectedBy_name=form['InspectedBy'].tolist()
signature=form['Signature'].tolist()

for i in range(userCount):
  im=Image.open("templateCertificate.png")
  d=ImageDraw.Draw(im)
  location=(locationInImage[i])
  text_colour=(0,0,0)
  ImageFont.truetype("Times New Roman.ttf",150)
  d.text(location,i,fill=text_colour,font=font)
  im.save("Fitness_Certificate_"+str(i)+".pdf")
