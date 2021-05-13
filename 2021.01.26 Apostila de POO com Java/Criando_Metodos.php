<?php
class MinhaClasse {
  public $prop1 = "Sou uma propriedade de classe!";
  public function setPropriedade($newval) {
      $this->prop1 = $newval;
  }
  public function getPropriedade()  {
      return $this->prop1 . "<br />";
  }
}
 
$obj = new MinhaClasse;
echo 'valor inicial da propriedade';
echo ''."<br />";
echo $obj->getPropriedade(); // Lê o valor da propriedade
$obj->setPropriedade("Sou um novo valor da propriedade!"); // Atribui um novo valor

echo 'novo valor da propriedade';
echo ''."<br />";
echo $obj->getPropriedade(); // Lê o valor novamente para mostrar a mudança
 
?>
