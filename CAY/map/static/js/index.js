function openTab(evt, tab) {
    var i, tabindex, tabcontents;
    tabindex = document.getElementsByClassName('tabindex');
    for (i = 0; i < tabindex.length; i++) {
        tabindex[i].className = tabindex[i].className.replace(" active", '');
    }
    tabcontents = document.getElementsByClassName('tabcontents');
    for (i = 0; i < tabcontents.length; i++) {
        tabcontents[i].style.display = 'none'
    }
    document.getElementById(tab).style.display = 'block';
    evt.currentTarget.className += ' active';
}


function openTab(evt, tab, t) {
    var i, tabindex, tabcontents;
    tabindex = document.getElementsByClassName('tabindex');
    for (i = 0; i < tabindex.length; i++) {
        tabindex[i].className = tabindex[i].className.replace(' active', '');
        tabindex[i].style.background = 'none'

    }

    tabcontents = document.getElementsByClassName('tabcontents');
    for (i = 0; i < tabcontents.length; i++) {
        tabcontents[i].style.display = 'none'
    }

    document.getElementById(tab).style.display = 'block';
    evt.currentTarget.className = 'tabindex active';
    document.getElementById(t).style.background = 'rgb(233, 162, 162)';
}

// 배운 것: 클릭함에 따라 다른 콘텐츠를 보이게 하는 것
// 서로 다른 탭을 선택했을 때, 각각 보이는 콘텐츠를 다르게 함
// 색깔을 바꿔보자 active tap의 테두리의 칼라가 나오도록