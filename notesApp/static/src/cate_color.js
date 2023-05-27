let color = []
color['4']   = '154, 60, 208'
color['3']   = '255, 234, 35'
color['2']   = '253, 240, 213'
color['1']   = '255, 53, 197'

function change_color(){
    categoris_elements = document.getElementById('id_categorie');
    console.log(color[categoris_elements.value])
    categoris_elements.style.backgroundColor = "rgb("+color[categoris_elements.value]+")";
}