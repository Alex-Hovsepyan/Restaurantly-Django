function menuFunc(e) {
    let header_menu = document.querySelector('.header_menu_close')
    
    console.log(e.target.className);
    if(e.target.className == 'burger' || e.target.parentNode.className == 'burger') {
        header_menu.classList.add('header_menu_open')
        let paths = document.querySelectorAll('.header_menu_container ul li')
        paths.forEach((item) => {
            item.addEventListener('click', function() {
                header_menu.classList.remove('header_menu_open')
            })
        })
    }
    else if(e.target.className == 'cross' || e.target.parentNode.className == 'cross') {
        header_menu.classList.remove('header_menu_open')
    }
}

window.onscroll = () => {
    let header = document.querySelector('.header')
    let general_header = document.querySelector('header')
    if(window.scrollY > 60) {
        header.style.opacity = '0'
        general_header.style.background = '#000000'
        general_header.style.position = 'fixed'
        general_header.style.top = '0'
    }
    else {
        header.style.opacity = '1'
        general_header.style.background = '#0c0b0999'
        general_header.style.position = 'relative'
    }
}

function foodSort(e) {
    let foods = document.querySelectorAll('.menu_content')
    let active_category = document.querySelector('.food_category_active')
    active_category.classList.remove('food_category_active')
    e.target.classList.add('food_category_active')
    foods.forEach(food => {
      if(e.target.dataset.category == 'all') {
        food.style.display = 'flex'
      }
        if(food.dataset.category != e.target.dataset.category && e.target.dataset.category != 'all') {
            food.style.display = 'none'
        }
        else if(food.dataset.category === e.target.dataset.category) {
            food.style.display = 'flex'
        }
    });
}

function SpecialsFunc(e) {
    let special_active = document.querySelector('.specials_info_active')
    let special = document.querySelector(`[data-category=${e.target.dataset.category}].specials_info`)
    let special_category_active = document.querySelector('.special_category_active')



    special_active.classList.remove('specials_info_active')
    special.classList.add('specials_info_active')
    special_category_active.classList.remove('special_category_active')
    e.target.classList.add('special_category_active')
}

let swiper = new Swiper(".mySwiper", {
    pagination: {
      el: ".swiper-pagination",
    },
    autoplay: {
        delay: 2000,
        disableOnInteraction: false,
    },  
    loop: true
  });




  function setActiveMenuLink() {
    const sections = document.querySelectorAll('.section');
    const navLinks = document.querySelectorAll('.nav-link');
    const scrollY = window.scrollY;
    navLinks.forEach(link => link.classList.remove('active'));
  
    if (scrollY <= 700) {
      navLinks[0].classList.add('active');
    } else if (scrollY > 700 && scrollY <= 1872) {
      navLinks[1].classList.add('active');
    } else if (scrollY > 1872 && scrollY <= 2669) {
      navLinks[2].classList.add('active');
    } else if (scrollY > 2669 && scrollY <= 3169) {
      navLinks[3].classList.add('active');
    } else if (scrollY > 3169 && scrollY <= 4545) {
      navLinks[4].classList.add('active');
    } else if (scrollY > 4545 && scrollY <= 5415) {
      navLinks[5].classList.add('active');
    }
    else if (scrollY > 5415 && scrollY <= 6063) {
      navLinks[6].classList.add('active');
    }
    else if (scrollY > 6063) {
      navLinks[7].classList.add('active');
    }    
  }
  
window.addEventListener('scroll', setActiveMenuLink);

setActiveMenuLink()