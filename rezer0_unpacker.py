from PIL import Image
import sys, getopt

#Decode the Bitmap
def imparse(a):
    list = []
    num = a.width - 1
    i = 0
    while i <= num:
        num2 = a.height - 1
        j = 0
        while j <= num2:
            pixel = a.getpixel((i,j))
            black = (0,0,0,0)
            flag = bool(pixel != black)
            if flag:
                list.append(pixel[0]) #R
                list.append(pixel[1]) #G
                list.append(pixel[2]) #B
            j += 1
        i += 1
    return list
#Unscramble
def decode(a):
    arr = [0] * (len(a) - 16 - 1 + 1)
    arr = a[16:]
    num = len(arr) - 1
    i = 0
    while i <= num:
        arr2 = arr
        num2 = i
        a_num = i % 16
        arr2[num2] ^= a[a_num]
        arr2[num2] = chr(arr2[num2])
        i += 1
    return "".join(arr)

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'rezer0_unpacker.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'rezer0_unpacker.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'input: ', inputfile
   print 'output: ', outputfile
   im = Image.open(inputfile)
   dec = imparse(im)
   dec = decode(dec)

   with open(outputfile, "w") as f:
	 f.write(dec)
   f.close()
   print 'Unpacked Successfully!! '

if __name__ == "__main__":
   main(sys.argv[1:])
