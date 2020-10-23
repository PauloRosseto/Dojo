
#Composição do arquivo do sqlite ->  uma ou mais páginas de 512 a 65536 bytes.
#O tamanho da pagina está a 16 bytes do início do arquivo. Todas as páginas devem ter o mesmo tamanho
#O total de páginas é 2**32 - 2
#O header do arquivo 100 bytes

#Passo 1 descobrir o tamanho das páginas no byte 16 (big Endian)


def main():
    path = 'C:/Users/PAULOHENRIQUEROSSETO'
    path += '/AppData/Local/Google/Chrome'
    path += '/User Data/Default/login data'

    
    with open(path, 'rb') as f:
        f.seek(16)
        #Analisar header
        pSize = int(f.read(2).hex(),16)
        print(pSize)

        f.seek(pSize)
        
        
        

main()
