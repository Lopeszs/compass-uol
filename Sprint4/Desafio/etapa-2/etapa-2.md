### Etapa 2

É possível reutilizar containers no Docker, pois ele preserva o sistema de arquivos e as configurações do container.  
O comando utilizado para reiniciar um container parado no Docker é:

**docker start (nome do container)**  
            ou   
**docker start (id do container)**  

Em meu ambiente, posso verificar os meus container e seus respectivos status a partir do comando 'docker ps -a'.  
Ao identificar um container com o status "Exited", como é o caso do container nomeado como 'container_carguru',  
eu posso reiniciá-lo utilizando o comando:

**docker start container_carguru**  
            ou  
**docker start 16365c5e5e6b**  



