function clearForms() {
    $(":input")
      .not(":button, :submit, :reset, :hidden, :checkbox, :radio")
      .val("");
    $(":checkbox, :radio").prop("checked", false);
  }