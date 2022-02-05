let svcnt = 1

function save(value) {
    const id = value
    if (svcnt % 2 === 1) {
        document.getElementById("save" + id).src = "{% static 'images/bookmark2.png' %}";
    } else {
        document.getElementById("save" + id).src = "{% static 'images/bookmark1.png' %}";
    }
    svcnt++;
}
//
// // header 버튼 눌러서 페이지 이동
//
// function allWine() {
//
//     window.location.href = '/wine-all';
//
// }
//
// function myPick() {
//
//     window.location.href = '/my-pick';
// }
//
// function logout() {
//
//     window.location.href = '/logout';
//
// }


// 스크롤 내리면 header 사라짐

var lastScrollTop = 0;

$(window).scroll(function() {
    var scrollTop = $(this).scrollTop(); /* 스크롤바 수직 위치를 가져옵니다, 괄호 안에 값(value)이 있을 경우 수직 위치를 정합니다. */
    // scrollTop - 선택한 요소의 스크롤바 수직 위치를 반환하거나 스크롤바 수직 위치를 정하는 메소드

    if (scrollTop >= 20) { // 숫자에 따라 아래로 스크롤 했을 때 사라지는 영역의 크기가 바뀝니다.
        if ((scrollTop > lastScrollTop) && (lastScrollTop > 0)) { /* &&: AND, 두 값이 모두 참이어야 값이 출력 */
            /* 화면에 나오지 않을 때: top값을 마이너스로 요소가 보이지 않게 사용해야함 */
            $(".header-button").css("top", "-150px");
        } else {
            $(".header-button").css("top", "0px");
        }

        lastScrollTop = scrollTop;
    }
});