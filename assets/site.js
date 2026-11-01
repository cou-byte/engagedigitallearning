(function(){
  var btn=document.getElementById('menuBtn'),menu=document.getElementById('menu');
  if(btn&&menu){
  btn.addEventListener('click',function(){var o=menu.classList.toggle('open');btn.setAttribute('aria-expanded',o)});
  menu.addEventListener('click',function(e){if(e.target.tagName==='A'){menu.classList.remove('open');btn.setAttribute('aria-expanded','false')}});
  }

  var lb=document.getElementById('lightbox'),lbImg=document.getElementById('lbImg');
  if(lb){
  document.querySelectorAll('.gallery button').forEach(function(b){
    b.addEventListener('click',function(){lbImg.src=b.dataset.full;lbImg.alt=b.querySelector('img').alt;lb.hidden=false;document.getElementById('lbClose').focus()});
  });
  function close(){lb.hidden=true;lbImg.src=''}
  document.getElementById('lbClose').addEventListener('click',close);
  lb.addEventListener('click',function(e){if(e.target===lb)close()});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!lb.hidden)close()});
  }


  var fw={
    content:['Learner ↔ Content','Multimedia and instructional video designed so students do something with the material: in-video questions, guided viewing, and activities that turn watching into practice.','Parts I and II · Chapters 1–4'],
    peer:['Learner ↔ Learner','Social annotation, peer assessment and group projects that turn a roster into a working community.','Parts III and IV · Chapters 5–9'],
    teacher:['Learner ↔ Teacher','Visible teaching presence through facilitation, timely feedback and dialogue, with strategies that scale to large online courses.','Throughout · every chapter'],
    ai:['Learner ↔ AI','AI as a learning partner and as an object of inquiry, with human judgment and learning goals kept at the center.','Part V · Chapter 10']
  };
  var cards=document.querySelectorAll('.card');
  cards.forEach(function(c){c.addEventListener('click',function(){cards.forEach(function(x){x.setAttribute('aria-pressed',String(x===c))});var d=fw[c.dataset.k];document.getElementById('fwTitle').textContent=d[0];document.getElementById('fwCopy').textContent=d[1];document.getElementById('fwRef').textContent=d[2]})});

  var form=document.getElementById('contactForm');
  if(form) form.addEventListener('submit',function(e){
    if(form.getAttribute('action')==='#'){e.preventDefault();document.getElementById('formNote').hidden=false;document.getElementById('formNote').textContent='This form is not connected yet. Point its action at a form service to make it live.'}
  });
})();
