let color = []
color['4']   = '#FB4C4C'
color['3']   = '#3DFB5C'
color['2']   = '#54F1FB'
color['1']   = '#F7FB42'

function change_color(){
    categoris_elements = document.getElementById('id_categorie');
    console.log(color[categoris_elements.value])
    categoris_elements.style.backgroundColor = color[categoris_elements.value];
}