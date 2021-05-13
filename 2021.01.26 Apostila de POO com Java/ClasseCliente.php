<?php

   class cliente {

        public $nome;
        public $saldo;

        public function confirmarrecebimento(){
              echo  "<br/>Confirmando Informação";
        }       

        public function pagarconta($valor){
            echo "<br/>Foi pago o valor de R$ ".$valor;
        }     

    }   

$tempCliente = new Cliente();

//atribuindo valores aos atributos
$tempCliente->nome = "Tadeu";
$tempCliente->saldo = 1000;

//chamando os métodos da classe
$tempCliente->confirmarrecebimento();
$tempCliente->pagarconta(200);
 
echo "<br/>Nome do Cliente : ".$tempCliente->nome;
echo "<br/> Saldo : ".$tempCliente->saldo;

?> 