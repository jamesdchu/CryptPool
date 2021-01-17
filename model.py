from stellar_sdk import Server, Asset, Account, Keypair, TransactionBuilder, Network
from stellar_sdk.exceptions import NotFoundError, BadResponseError, BadRequestError
import qrcode, datetime, requests

#Verifying Stellar account
def verify_destination(public_key): 
    server = Server("https://horizon-testnet.stellar.org")
    try: 
        server.load_account(public_key)
    except NotFoundError: 
        return False
    return True

#Returns all balances of each asset in a list --> can be used to show how much a fundraiser has made so far
def balances(public_key):
    server = Server("https://horizon-testnet.stellar.org")
    account = server.accounts().account_id(public_key).call()
    return account['balances']
 
#Creating a keypair
def createKeypair(): 
    pair = Keypair.random() 
    return [pair.secret, pair.public_key]

#Creating an account using the public key 
def createAccount(public_key): 
    response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")
    if response.status_code == 200:
        print(f"SUCCESS!: \n{response.text}")
    else:
        print(f"ERROR! Response: \n{response.text}")


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

#Returns the current timestamp
def currentDateTime(): 
    now = datetime.datetime.now()
    now_str = str(now.strftime("%Y-%m-%d %H:%M:%S"))
    return now_str

#Sending a payment to a fundraiser
def sendPayment(sender_sKey, destination_pKey, amount, asset_code, message, user_id, fundraiser_id): 
    server = Server("https://horizon-testnet.stellar.org")
    source_key = Keypair.from_secret(sender_sKey)
    destination_id = destination_pKey
    
    try: 
        server.load_account(destination_id)
    except NotFoundError: 
        #Shouldn't be a problem since we're using fundraiser wallets (will verify when creating fundraisers/accounts)
        print("PKOSKIOSJNIROFJSLOIMSOMRSOIOM")
        return False
        raise Exception("THe destination account is invalid")
    # If there was no error, load up-to-date information on your account.
    source_account = server.load_account(source_key.public_key)
    # Let's fetch base_fee from network
    base_fee = server.fetch_base_fee()
    transaction = (
        TransactionBuilder( 
            source_account=source_account, 
            network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
            base_fee=base_fee
        )
        .append_payment_op(destination=destination_id, amount=str(amount), asset_code=asset_code)
        .add_text_memo(user_id + "d" + fundraiser_id) # COULD ADD DETAILS TO TRANSACTION 
        .set_timeout(10)
        .build()
  
    )

    #Proof of identity of sender
    transaction.sign(source_key)
    
    try: 
        #Sending the transaction to Stellar
        response = server.submit_transaction(transaction)
        print(f"Response: {response}")
    except (BadRequestError, BadResponseError) as err:
        print(f"Something went wrong!\n{err}")
        return False
    return True


####### TESTING CODE #########
#def getCryptoBalance()
# print(balances("GAMMA7XWCR2FT6OCMT4XNEHAMBMF4IFUUHTXW7N27HWLDDLZ2W74QZPT"))
# print(balances("GAAJ3ATNIT7YTMCYLGCB2DUTV4NZDWCYXAZQQ4J5D3YXSW5DOZNC3CMY"))
# sendPayment("SBYU7Y6XHPGBUEBRNKH4FBFQ6XPJNHQCLMT63CXDN6ZZYSMIZEDERR3Z", "GAAJ3ATNIT7YTMCYLGCB2DUTV4NZDWCYXAZQQ4J5D3YXSW5DOZNC3CMY", 500, "XLM")
# print(balances("GAMMA7XWCR2FT6OCMT4XNEHAMBMF4IFUUHTXW7N27HWLDDLZ2W74QZPT"))
# print(balances("GAAJ3ATNIT7YTMCYLGCB2DUTV4NZDWCYXAZQQ4J5D3YXSW5DOZNC3CMY"))

# print(balances("GDJNK3QWBGJNPYZ5YIQDDS7IGNMQBEA4JKQZ34SBGINLBH6SIXW2E4YW"))






