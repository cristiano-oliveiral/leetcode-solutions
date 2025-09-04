from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Encontra a mediana de dois arrays ordenados usando busca binária.
        
        A estratégia é particionar os dois arrays de forma que:
        - A parte esquerda tenha exatamente (m+n+1)//2 elementos
        - Todos elementos da esquerda sejam <= todos elementos da direita
        
        Args:
            nums1: Primeiro array ordenado
            nums2: Segundo array ordenado
            
        Returns:
            A mediana dos dois arrays combinados
        """
        # Garantir que nums1 seja o menor array para otimizar a busca binária
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # Partição em nums1
            partition_x = (left + right) // 2
            # Partição em nums2 para manter metade dos elementos à esquerda
            partition_y = (m + n + 1) // 2 - partition_x
            
            # Elementos máximos da parte esquerda
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            
            # Elementos mínimos da parte direita
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]
            
            # Verificar se encontramos a partição correta
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Partição correta encontrada
                if (m + n) % 2 == 0:
                    # Número par de elementos - mediana é a média dos dois elementos centrais
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    # Número ímpar de elementos - mediana é o maior da parte esquerda
                    return max(max_left_x, max_left_y)
            
            elif max_left_x > min_right_y:
                # Muitos elementos de nums1 na parte esquerda
                right = partition_x - 1
            else:
                # Poucos elementos de nums1 na parte esquerda
                left = partition_x + 1