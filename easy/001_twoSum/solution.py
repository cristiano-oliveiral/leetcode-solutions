class Solution:
    """
    Solução para o problema Two Sum.
    Fonte: https://leetcode.com/problems/two-sum/
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Encontra os índices de dois números que somam o valor alvo (target).

        Args:
            nums: Uma lista de inteiros.
            target: O valor alvo para a soma.

        Returns:
            Uma lista contendo os índices dos dois números.
        """
        # Cria um dicionário para armazenar o número e seu índice
        seen = {}
        
        # Percorre o array 'nums' com o índice 'i'
        for i, num in enumerate(nums):
            # Calcula o complemento necessário para alcançar o alvo
            complement = target - num
            
            # Verifica se o complemento já está no dicionário
            if complement in seen:
                # Se estiver, retorna o índice do complemento e o índice atual
                return [seen[complement], i]
            
            # Se não estiver, adiciona o número atual e seu índice ao dicionário
            seen[num] = i