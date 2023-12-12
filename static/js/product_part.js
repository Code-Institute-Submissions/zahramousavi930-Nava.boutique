






// product countws
const decrease =document.getElementById('decrease')
const increase =document.getElementById('increase')
const maincount =document.getElementById('main-count')

decrease.addEventListener('click',()=>{
   if(maincount.value <= 0 ){
      maincount.value ==0
   }
   else{

      maincount.value--
   }
   

   
})

increase.addEventListener('click',()=>{
   maincount.value++
 })







