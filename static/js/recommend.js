let svcnt = 1

function save(value) {
    const id = value
    if (svcnt % 2 == 1) {
        document.getElementById("save" + id).src = "../recommend/bookmark2.png";
    } else {
        document.getElementById("save" + id).src = "../recommend/bookmark1.png";
    }
    svcnt++;
}