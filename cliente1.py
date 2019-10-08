from socket import *
s = socket ()
servidor="127.0.0.1"
porta=8792
s.connect((servidor, porta))


while True:
   sequencia = input ("Digite a sequência: ")
   s.send (str.encode (sequência, "utf-8"))
   if sequencia == " " || str.len(sequencia) =!8:
	 break

sequencia = s.recv (8792)
print (data.decode ("utf-8"))
print ("FIM")
s.close ()
