#!/bin/bash


for ARQ in 'arq.txt' 'arq2.txt'
do
	#Executa o codigo python
	python3 hash.py -a md5 -f arq.txt > saida_py.txt
	md5sum arq.txt | awk '{print $1}' > saida_sh.txt

	#Compara a diferença nas saídas
	if diff saida_py.txt saida_sh.txt
	then
		echo "Resultado Ok para arquivo $ARQ"
	else
		echo "Erro para o arquivo $ARQ"
	fi
	#Remove arquivos temporarios
	rm saida_py.txt saida_sh.txt
done
