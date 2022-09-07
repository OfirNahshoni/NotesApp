function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }


function deleteProfile(profileId) {
  fetch("/delete-profile", {
    method: "POST",
    body: JSON.stringify({ profileId: profileId }),
  }).then((_res) => {
    window.location.href = "/profile";
  });
}



/**
 * Profile editing
 */

// Display an uplaoded image in placeholder
const input_file = document.getElementById("profile_image");
const preview_container = document.getElementById("imagePreview");
const preview_image = preview_container.querySelector(".image-preview__image");
const preview_default_text = preview_container.querySelector(".default-text-prompt");

// Add Event Listener for <input> element (when it is get changed)
input_file.addEventListener("change", function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        preview_default_text.style.display = "none"; // Hide the default text
        preview_image.style.display = "block"; // Show the image
        reader.addEventListener("load", function () {
            preview_image.setAttribute("src", this.result);
        });
        reader.readAsDataURL(file);
    } else {
        preview_default_text.style.display = null;
        preview_image.style.display = null;
        preview_image.setAttribute("src","");
    }
});

document.querySelectorAll(".drop-zone__input").forEach(inputElement => {
    const dropZoneElement = inputElement.closest(".drop-zone");

    dropZoneElement.addEventListener("click", ev => {
        inputElement.click();
    });

    inputElement.addEventListener("change", ev => {
        if (inputElement.files.length) {
            updateThumbnail(inputElement, inputElement.files[0]);
        }
    });

    // Event: drag over the drop zone box
    dropZoneElement.addEventListener("dragover", ev => {
        ev.preventDefault();
        dropZoneElement.classList.add("drop-zone--over");
    });

    // Event: canceling the drag over by pressing keyboard esc button or moving the dragged image out of the drop zone box
    ["dragleave", "dragend"].forEach(type => {
        dropZoneElement.addEventListener(type, ev => {
        dropZoneElement.classList.remove("drop-zone--over");
        });
    });

    // Event: dropping the image to the drop zone box (or uploading image by browsing the local machine)
    dropZoneElement.addEventListener("drop", ev => {
        ev.preventDefault();
        if (ev.dataTransfer.files.length) {
            inputElement.files = ev.dataTransfer.files;
            updateThumbnail(dropZoneElement, ev.dataTransfer.files[0]);
        }
        dropZoneElement.classList.remove("drop-zone--over");
    });



    function updateThumbnail(dropZoneElement, file) {
        // console.log(dropZoneElement);
        // console.log(file);
        let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");

        // Remove the prompt from the drop zone box
        if (dropZoneElement.querySelector(".drop-zone__prompt")) {
            dropZoneElement.querySelector(".drop-zone__prompt").remove();
        }

        // Create a thumbnail object if he is not exist (first time uploading an image)
        if (!thumbnailElement) {
            thumbnailElement = document.createElement("div");
            thumbnailElement.classList.add("drop-zone__thumb");
            dropZoneElement.appendChild(thumbnailElement);
        }

        thumbnailElement.dataset.label = file.name;

        // // Show image
        // if (file.type.startsWith("image/")) {
        //     const reader = new FileReader();
        //     reader.readAsDataURL(file);
        //     reader.onload = () => {
        //     thumbnailElement.style.backgroundImage = `url('${ reader.result }}')`;
        //     };
        // } else {
        //     thumbnailElement.style.backgroundImage = null;
        // }
    }
});