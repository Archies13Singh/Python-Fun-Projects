import pyqrcode

def qrcode():
    # take user input
    q = pyqrcode.create(input("Generate : "))
    q.png("qrcode.png",scale=6)
    print("QR generated")

if __name__=="__main__":
    qrcode()
