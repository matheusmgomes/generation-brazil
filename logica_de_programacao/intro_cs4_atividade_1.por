programa
{
	
	funcao inicio()
	{
		const inteiro tamanho = 10
		inteiro nums[tamanho]
		inteiro i, j, temp

		para(i=0;i<tamanho;i++){
			escreva("Digite o item ", i+1," da lista: ")
			leia(nums[i])
		}

		para(i=0; i<tamanho-1;i++){
			para(j=0; j<tamanho-1;j++){
				se (nums[j] < nums[j+1]){
					temp = nums[j]
					nums[j] = nums[j+1]
					nums[j+1] = temp
				}
			}
		}

		para(i=0;i<tamanho;i++){
			escreva(nums[i], "\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 208; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */