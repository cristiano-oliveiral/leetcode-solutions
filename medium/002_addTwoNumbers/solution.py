class Solution:
    """
    Solução para o problema Add Two Numbers.
    Fonte: https://leetcode.com/problems/add-two-numbers/
    """
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Soma dois números representados como listas ligadas em ordem reversa.
        
        Args:
            l1 (Optional[ListNode]): Primeira lista ligada representando um número
            l2 (Optional[ListNode]): Segunda lista ligada representando um número
            
        Returns:
            Optional[ListNode]: Lista ligada representando a soma dos dois números
        """
        # Nó dummy para simplificar a construção da lista resultado
        dummy_head = ListNode(0)
        current = dummy_head
        
        # Variável para controlar o "vai um" da adição
        carry = 0
        
        # Processa enquanto há nós em qualquer lista ou carry pendente
        while l1 is not None or l2 is not None or carry != 0:
            # Obtém valores dos nós atuais (0 se nó não existir)
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calcula a soma total incluindo carry anterior
            total_sum = val1 + val2 + carry
            
            # Extrai o dígito atual e o novo carry
            digit = total_sum % 10
            carry = total_sum // 10
            
            # Cria novo nó com o dígito calculado
            current.next = ListNode(digit)
            current = current.next
            
            # Avança os ponteiros das listas de entrada
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        # Retorna a lista resultado (excluindo o nó dummy)
        return dummy_head.next