var info = 0;
var qtd = document.querySelectorAll('.box').length;
var info_componet = document.querySelector('.box').children

document.addEventListener("keypress", function(e) {
  if(e.key === 'Enter') {
    
    if (info==qtd){
      info=0
    }

    info_componet.item(info).style.display = 'none'
    info_componet.item(info+1).style.display = 'flex'

    info+=1
  }
});