function openDeleteModal(element) {

    let id = element.dataset.id;
    let title = element.dataset.title;

    document.getElementById("deleteModal").style.display = "flex";

    document.getElementById("deleteText").innerHTML =
        "Are you sure you want to delete <strong>" + title + "</strong>?";

    document.getElementById("deleteForm").action =
        "/delete_task/" + id + "/";
}
function closeDeleteModal(){

    document.getElementById("deleteModal").style.display = "none";

}