---

## Systemcalls e Ferramenta strace

### O que são Systemcalls?

Systemcalls são métodos utilizados por processos para se comunicar e requisitar serviços do sistema operacional. Elas atuam como uma ponte de comunicação entre o processo e o sistema operacional.

### Ferramenta strace

O `strace` é uma ferramenta que monitora as chamadas de sistema (system calls) e os sinais recebidos pela aplicação.

### Como Utilizar o strace

Para utilizar o `strace`, siga os passos abaixo:

1. **Obtenha o PID da aplicação:**

   Use o comando `ps aux | grep (nome da aplicação)` para obter o PID. Por exemplo, para o nginx:
   ```sh
   ps aux | grep nginx
   ```

2. **Execute o strace:**

   Utilize o comando `strace -p (PID)` para iniciar o monitoramento. Por exemplo:
   ```sh
   strace -p (PID)
   ```

3. **Parar o Processo:**

   Para parar o processo, use o comando:
   ```sh
   sudo kill -s SIGSTOP (PID)
   ```

### Exemplo Prático

Como mostrado na imagem, obtive o PID do nginx usando o `ps aux` e o `grep` para realizar a filtragem. Depois, executei o `strace` para realizar o monitoramento do serviço e recebimento de sinais.

[Saída do PID](https://prnt.sc/153o635)

### Considerações

Com o `strace`, pode-se verificar se o processo está funcionando de maneira correta. No entanto, o `strace` não funciona em todos os softwares. O rastreamento é finalizado quando o processo rastreado é finalizado.

#### Exemplo de Saída do strace:

[Exemplo de Saída](https://prnt.sc/153pj8d)

---
