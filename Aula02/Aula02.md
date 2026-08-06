## Aula 2

1) Para que usar SD? 

R: Compartilhar recursos

2) Como SD opera? 

R: SD opera através de protocolos de rede que permitem a comunicação entre dispositivos e a gestão centralizada de recursos

3) Arquitetura: Cliente-Servidor

# THREAD 

- mini processos, cada um usando um recurso individual
- SD
- encapsulamento
- "envolvem" rotinas ou tarefas ou instruções

-Tipos:
- Sem seção critica = memória compartilhada
- sincronismo = SO (semáforo, lock)

Processo:

-Thread (classe) ------ Sem M.C
-Runnable (interface) ------ Com M.C

MinhaThread = new MinhaThread();

