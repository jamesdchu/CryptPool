from stellar_sdk import Server, Asset, Account, Keypair, TransactionBuilder, Network
from stellar_sdk.exceptions import NotFoundError, BadResponseError, BadRequestError
import qrcode

#Returns all balances of each asset in a list --> can be used to show how much a fundraiser has made so far
def balances(public_key):
    server = Server("https://horizon-testnet.stellar.org")
    account = server.accounts().account_id(public_key).call()
    return account['balances']

#Generates a unique QR code for each fundraiser
def makeQRcode(link, id_): 
    qr = qrcode.QRCode(version=10, 
                        box_size=20,
                        border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill='black',back_color='white')
    # img.save('f'+id_+'.png')
    return img

#Sending a payment to a fundraiser
def sendPayment(): 
    server = Server("https://horizon-testnet.stellar.org")
    
    return "beginning"



