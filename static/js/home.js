// $(document).ready(function(){

//     $("about").mouseover(function(){
//         $(this).css("z-index", "9")
//     });
//     $("about").mouseout(function(){
//         $(this).css("z-index", "0")
//     });


// })

// ------------------About Start-----------------
var about=document.getElementById('about');
about.addEventListener('click',function(){
    this.style.border="thin solid #0000FF";
    alert("This is my About")
})

var about_name=document.getElementById('about_name')
about_name.addEventListener('mouseenter',function(){
    this.style.textAlign='center';
    this.style.fontFamily='monopace'
    
})

var btn=document.getElementById('about_description')
btn.addEventListener('mouseover',function(){
    // alert('This is about');
    this.style.backgroundColor='#ded5d5';
    this.style.fontSize="large";
    // this.style.transition="all 1s"
 
})
btn.addEventListener('mouseout',function(){
    // alert('This is about');
    this.style.backgroundColor='white';
    this.style.fontSize="medium";
 
})

var about_info=document.getElementById('about_info')
about_info.addEventListener('mouseover',function(){
    // alert('This is about');
    this.style.backgroundColor='#ded5d5';
    this.style.fontSize="large";
 
})
about_info.addEventListener('mouseout',function(){
    // alert('This is about');
    this.style.backgroundColor='white';
    this.style.fontSize="medium";
 
})




// -------------------------About end---------------------


// skill
var skill_heading=document.getElementById('skill_heading')
skill_heading.addEventListener('mouseenter',function(){
    this.style.textAlign='center';
    this.style.fontSize='60';
    
})

skill_heading.addEventListener('mouseout',function(){
    this.style.textAlign='center';
    this.style.fontSize="40";
    
})
// work_exp_heading
var work_exp_heading=document.getElementById('work_exp_heading')
work_exp_heading.addEventListener('mouseenter',function(){
    this.style.textAlign='center';
    this.style.fontSize='60';
    
    
})

work_exp_heading.addEventListener('mouseout',function(){
    this.style.textAlign='center';
    this.style.fontSize="40";
    
})


// Education

var education_heading=document.getElementById('education_heading')
education_heading.addEventListener('mouseenter',function(){
    this.style.textAlign='center';
    this.style.fontSize='60';
    
    
})

education_heading.addEventListener('mouseout',function(){
    this.style.textAlign='center';
    this.style.fontSize="40";
    
})


