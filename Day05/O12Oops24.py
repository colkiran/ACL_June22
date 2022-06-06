
import O11Oops23

def withDraw(self):
    print("You can withdraw upto 4k per day.......")

O11Oops23.HDFC.withDraw = withDraw

print("-" * 40)
hdfc = O11Oops23.HDFC()
hdfc.withDraw()
