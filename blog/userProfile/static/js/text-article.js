const ImageTool = window.ImageTool;

$(document).on("ready", function () {
  $("#upload-article").html("Upload Article");
});

const editor = new EditorJS({
  tools: {
    header: Header,
    raw: RawTool,
    image: SimpleImage,
    table: Table,

    quote: {
      class: Quote,
      inlineToolbar: true,
      shortcut: "CMD+SHIFT+O",
      config: {
        quotePlaceholder: "Enter a quote",
        captionPlaceholder: "Quote's author",
      },
    },

    checklist: {
      class: Checklist,
      inlineToolbar: true,
    },
    list: {
      class: List,
      inlineToolbar: true,
    },
  },
});

$("#upload-article").on("click", function () {
  const date = getDateInText();
  const user_id = $(".userid").attr("id");
  const article_id = $(".codex-editor").attr("id");
  if (user_id) {
    editor
      .save()
      .then((outputData) => {
        postData("/profile/upload-article/", {
          blocks: outputData.blocks,
          publish_date: date,
          user_id: user_id,
          article_id: article_id,
        }).then((response) => {
          if (response.msg === "Article Uploaded") {
            $(".codex-editor").attr("id", response.id);
            showMessage("success", response.msg);
            $("#upload-article").html("Update Article");
          } else if (response.msg === "Article Updated") {
            showMessage("success", response.msg);
          } else {
            showMessage("error", response.msg);
          }
        });
      })
      .catch((error) => {
        console.log("Saving failed: ", error);
      });
  }
});
