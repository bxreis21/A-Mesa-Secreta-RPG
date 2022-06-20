var btn_back= document.querySelector('#btn-back')
var btn_next = document.querySelector('#btn-next')
var btn_conf= document.querySelector('#btn-conf')

var info = 0;
var qtd = document.querySelectorAll('.info').length;
var info_componet = document.querySelector('.box').children

btn_next.addEventListener('click', function () {
  
  if (info==qtd-1){
    info=0
  }

  if (info==qtd-2){
    info_componet.item(info+1).style.display = 'flex';
    info_componet.item(info).style.display = 'none';
    btn_next.style.display='none';
    info+=1;
    btn_conf.style.display='block';
    
  }else if (info==0){
    info_componet.item(info).style.display = 'none';
    info_componet.item(info+1).style.display = 'flex';
    btn_back.style.display = 'block';
    info+=1
    
  }else{
    info_componet.item(info).style.display = 'none';
    info_componet.item(info+1).style.display = 'flex';
    info+=1

  } 
})

btn_back.addEventListener('click', function () {
  
  if (info==1){
    info_componet.item(info).style.display = 'none';
    info_componet.item(info-1).style.display = 'flex';
    btn_back.style.display = 'none';
    
  }else if (info==qtd-1){
    info_componet.item(info).style.display = 'none';
    btn_conf.style.display='none';
    info_componet.item(info-1).style.display = 'flex';
    btn_next.style.display = 'block';
    
  }else{
    info_componet.item(info).style.display = 'none';
    info_componet.item(info-1).style.display = 'flex';
    console.log(qtd,info)
  } 

  info-=1
})
