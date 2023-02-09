from django.shortcuts import render
from .models import Customers

##import hvac
##import base64

##client = hvac.Client(url='http://[private-IP]:8200',
##                     token="[your-token]"
##                     )

##def encrypt_data(value):
##    try:
##        encr = client.secrets.transit.encrypt_data(mount_point = "transit",
##                                                   name = "customer-key",
##                                                   plaintext = base64.b64encode(value.encode()).decode('ascii')
##                                                  )
##        enc_value = encr['data']['ciphertext']
##        return enc_value
##    except Exception as e:
##        print(f"Error encrypting data: {e}")
##        return value

##def decrypt_data(value):
##    try:
##        decr = client.secrets.transit.decrypt_data(mount_point = "transit",
##                                                   name = "customer-key",
##                                                   ciphertext = value
##                                                  )
##        dec_value = decr['data']['plaintext']
##        decoded = base64.b64decode(dec_value).decode()
##        return decoded
##    except Exception as e:
##        print(f"Error decrypting data: {e}")
##        return value


def homepage(request):
    return render(request, 'customerapp/index.html')

def dbview(request):
    records = Customers.objects.all()
    return render(request, 'customerapp/dbview.html', {"records": records})

def records(request):
    if request.method == "POST":
        rec = Customers(first_name= request.POST['first_name'], 
                        last_name= request.POST['last_name'], 
                        date_of_birth= request.POST['date_of_birth'], 
                        pan_number= request.POST['pan_number'],
                        ##pan_number= encrypt_data(request.POST['pan_number']),
                        credit_card_number= request.POST['credit_card_number'],
                        ##credit_card_number= encrypt_data(request.POST['credit_card_number']), 
                        email= request.POST['email'], 
                        address= request.POST['address'], 
                        salary= request.POST['salary'])
        rec.save()
    records = Customers.objects.all()
    records = list(records.values())
##    for i in range(len(records)):
##        records[i]['pan_number'] = decrypt_data(records[i]['pan_number'])
##        records[i]['credit_card_number'] = decrypt_data(records[i]['credit_card_number'])    
    return render(request, 'customerapp/records.html', {"records": records})

def add_cust(request):
    return render(request, 'customerapp/add.html')

