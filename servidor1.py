
from socket import *
from threading import Thread
def atende (conn, cliente1):
conn.settimeout(10.00)

while True:
	try:
	    data = conn.recv (8792)
	except:
            print ("Erro na conexão com o cliente "+str(cliente))
              break

while True:
(conn, cliente) = s.accept ()
print ("Recebi a conexao de "+str(cliente))
nthr += 1

if str.len(sequencia) != 8:
      print ("Tamanho não condiz com o esperado");
            break
if sequencia == "FIM":
            break

else:
     for (i=0; i<9; i++)
        if (sequencia [i] == "T" || "G" || "C" || "A")
                print ("Sequência válida"))
      break


print ("Criando thread "+str(nthr))
t = Thread(target=atende,args=(conn, cliente,))
t.start()
