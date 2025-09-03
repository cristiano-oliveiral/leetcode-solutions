from typing import Dict


class Solution:
    """
    Solução para o problema Longest Substring Without Repeating Characters.
    Fonte: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    """
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Encontra o comprimento da maior substring sem caracteres repetidos.
        
        Utiliza sliding window com hash table para otimização, permitindo
        saltos inteligentes quando caracteres duplicados são encontrados.
        
        Args:
            s (str): String de entrada para análise
            
        Returns:
            int: Comprimento da maior substring sem caracteres duplicados
        """
        # Caso base: string vazia
        if not s:
            return 0
        
        # Dicionário para mapear caracteres às suas posições mais recentes
        char_index_map: Dict[str, int] = {}
        
        # Ponteiros da janela deslizante
        left_pointer = 0
        max_length = 0
        
        # Expansão da janela com ponteiro direito
        for right_pointer, current_char in enumerate(s):
            # Verifica se o caractere atual já existe na janela atual
            if (current_char in char_index_map and 
                char_index_map[current_char] >= left_pointer):
                
                # Move ponteiro esquerdo para posição após a duplicata
                # Isso garante que a janela não contenha caracteres duplicados
                left_pointer = char_index_map[current_char] + 1
            
            # Atualiza a posição mais recente do caractere atual
            char_index_map[current_char] = right_pointer
            
            # Calcula comprimento da janela atual e atualiza máximo se necessário
            current_length = right_pointer - left_pointer + 1
            max_length = max(max_length, current_length)
        
        return max_length